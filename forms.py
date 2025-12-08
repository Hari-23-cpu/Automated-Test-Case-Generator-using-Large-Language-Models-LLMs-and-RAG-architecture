from django import forms

class TestCaseForm(forms.Form):
    
    user_input = forms.CharField(
        label='Paste the Code or Requirements',
        widget=forms.Textarea(attrs={
            'rows':15,
            'placeholder':'Paste your source code ,user stories, or functional requirements here...',
            'class':'form-textarea'
        })
    )

