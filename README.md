
# 🤖 Automated Test Case Generator (Generative AI Project)

## ✨ Project Overview

The **Automated Test Case Generator** is a **Generative AI–based system** designed to streamline the **Software Quality Assurance (QA) workflow**.

This project uses the **Google Gemini API** to automatically generate **software test cases** from project documentation such as:

* 📄 User stories
* 📑 Software requirements
* 🔗 API documentation

Using the **natural language understanding capabilities of Generative AI**, the system can generate **structured and contextual test cases** that include:

* ✅ Test Steps
* 🎯 Expected Results
* ⚠ Severity Levels

This project demonstrates how **Generative AI can assist QA engineers** by automatically creating high-quality test scenarios based on textual project inputs.

---

# 🧠 Core Architecture: Generative AI with Gemini API

The system is powered by the **Google Gemini API**, which enables advanced **natural language processing and test case generation**.

### ⚙️ Workflow

1️⃣ **Input Documentation**

The system accepts project documentation such as:

* Requirement documents
* User stories
* Feature descriptions

---

2️⃣ **Prompt Processing**

The documentation is converted into a **structured prompt** and sent to the **Google Gemini API**.

Example prompt:

```
Generate functional, negative, and boundary test cases 
for the login feature based on the following requirements.
```

---

3️⃣ **AI-Based Test Case Generation**

The **Google Gemini model** processes the prompt and generates:

* Functional test cases
* Negative test cases
* Boundary test cases

with **clear steps and expected outcomes**.

---

# ⚙️ Features

## 🤖 AI-Powered Test Case Generation

Automatically generates test cases using **Generative AI models**.

Generated outputs include:

* Functional Tests
* Negative Tests
* Boundary Tests

---

## ⚡ Fast QA Workflow

Reduces manual effort for **QA engineers** by automating test case generation from textual requirements.

---

## 📑 Structured Output

The system produces test cases in structured formats such as:

* JSON
* Markdown
* YAML

This allows easy integration with **test management tools**.

Example Output:

```json
{
  "test_case": "Login with valid credentials",
  "steps": [
    "Enter valid username",
    "Enter valid password",
    "Click login button"
  ],
  "expected_result": "User should be redirected to dashboard",
  "severity": "High"
}
```

---

# 🛠 Technologies Used

### 🐍 Python

Core programming language used for system development.

### 🤖 Generative AI

Powered by the **Google Gemini API for intelligent test case generation.

### 🌐 FastAPI / Django

Backend framework used for building the API or web interface.

### 📊 JSON / Markdown

Used for structured output of generated test cases.

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YourUsername/Automated-Test-Case-Generator.git
cd Automated-Test-Case-Generator
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Setup Environment Variables

Create a `.env` file and store your **Gemini API key**.

Example:

```
GEMINI_API_KEY=your_api_key
```

You can get the API key from:

🔗 [https://ai.google.dev/](https://ai.google.dev/)

---

## 4️⃣ Run the Application

Start the backend server.

Example using **FastAPI**:

```bash
uvicorn app:app --reload
```

Or using **Django**:

```bash
python manage.py runserver
```

## 5️⃣ Generate Test Cases

After starting the server, you can generate test cases by:

* 🌐 Using the web interface
* 🔗 Sending requests to the API endpoint

The system will use **Google Gemini** to generate structured test cases based on the provided documentation.

# 📂 Project Repository
https://github.com/YourUsername/Automated-Test-Case-Generator


