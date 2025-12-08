# generator/views.py (Partial Update: Focus on API Logic)

from django.shortcuts import render
from django.conf import settings
from .forms import TestCaseForm
import json
import requests
import google.genai as genai # New library import
from google.genai.errors import APIError # Import for error handling

# --- NEW API Configuration ---
GEMINI_API_KEY = getattr(settings, 'GEMINI_API_KEY', None)

def Test_generator_view(request):
    
    generated_test_cases = None
    error_message = None
    TEMPLATE_NAME = 'index.html' 
    
    if request.method == 'POST':
        form = TestCaseForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            # --- NEW TOKEN CHECK ---
            if not GEMINI_API_KEY or GEMINI_API_KEY == 'YOUR_GEMINI_API_KEY_HERE':
                error_message = "Configuration Error: Gemini API Key is missing. Please update settings.py."
                form = TestCaseForm(request.POST) 
                return render(request, TEMPLATE_NAME, {'form': form, 'error_message': error_message})


            system_prompt = (
                "You are an expert QA Engineer. Your task is to generate detailed, executable test cases "
                "for the provided input (code or requirements). The output MUST be a strict JSON array, "
                "where each object has the keys: 'Test ID', 'Scenario', 'Steps', and 'Expected Result'. "
                "DO NOT include any text, notes, or markdown formatting (like ```json) outside the JSON array block."
            )
            
            user_prompt = f"Generate test cases for the following:\n\n---\n{user_input}\n---"

            try:
                client = genai.Client(api_key=GEMINI_API_KEY)
                # 1. Call the Gemini API using gemini-2.5-flash
                # Note: We use gemini-2.5-flash for fast, structured output.
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[user_prompt],
                    config={"system_instruction": system_prompt}
                )
                raw_response_text = response.text.strip()
                
                # 2. Robust JSON Cleanup (Removing potential markdown fences like ```json)
                if raw_response_text.startswith('```'):
                    raw_content = raw_response_text.split('```json', 1)[-1].split('```', 1)[0].strip()
                else:
                    raw_content = raw_response_text.strip()
                
                # Further cleanup to ensure we only parse the JSON array
                start_index = raw_content.find('[')
                if start_index != -1:
                    raw_content = raw_content[start_index:].strip()
                
                generated_test_cases = json.loads(raw_content)

            except APIError as e:
                error_message = f"Gemini API Error: {e}"
            except json.JSONDecodeError:
                error_message = f"LLM Output Error: Failed to parse output as strict JSON. Raw output: {raw_response_text[:300]}..."
            except Exception as e:
                error_message = f"An unexpected error occurred: {e}"
        # ... (rest of the view, including the final render)
    
    else:
        form = TestCaseForm()
        
    context = {
        'form': form,
        'generated_test_cases': generated_test_cases,
        'error_message': error_message
    }
    
    return render(request, TEMPLATE_NAME, context)