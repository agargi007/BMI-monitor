BMI Calculator with AI-Powered Health Suggestions


Overview
This project is a modern web-based Body Mass Index (BMI) calculator built with Python, Flask, HTML/CSS, and Google Gemini API. Users enter their weight and height, and the app calculates their BMI, then leverages Gemini’s AI to provide personalized, easy-to-understand health suggestions and tips based on the result.

Features
BMI Calculation: Instantly computes BMI from user input (weight and height).

AI Health Suggestions: Uses Google Gemini API to generate personalized, actionable health and wellness tips based on the user’s BMI.

Modern Web UI: Clean, responsive interface styled with CSS for usability and accessibility.

Attractive Results: AI suggestions are formatted as a vertical numbered list for readability.

Secure API Key Handling: Uses environment variables to keep your Gemini API key safe.

Technology Stack
Backend: Python 3, Flask web framework

Frontend: HTML5, CSS3 (with custom styling)

AI Integration: Google Gemini API (via google-generativeai Python SDK)

Deployment: Localhost (can be deployed to any Flask-compatible platform)

How It Works
User Input:
The user enters their weight (kg) and height (m) into a simple web form.

BMI Calculation:
The backend calculates BMI using the formula:

B
M
I
=
weight (kg)
(
height (m)
)
2
BMI= 
(height (m)) 
2
 
weight (kg)
 
AI-Powered Feedback:
The app sends the BMI, weight, and height to the Gemini API using a prompt like:

“A user has a BMI of 22.5, weight 70 kg, and height 1.77 m. Tell them their BMI category, what it means for their health, and give 3 helpful tips to improve or maintain their BMI. Make the response friendly and easy to understand.”

Model Selection:
The app uses the model name as provided by the Gemini API, e.g., "models/gemini-1.5-pro-latest" or "models/gemini-1.5-pro-002".
The model name must match one available for your API key (see below).

Formatting AI Output:
The AI’s Markdown-style numbered tips are converted into an HTML ordered list (<ol><li>...</li></ol>) so each tip appears on its own line, making the advice easy to read.

Result Display:
The BMI result and AI suggestions are shown on a modern, centered results page.

Google Gemini API Integration
API Key:
You must obtain a Gemini API key from Google AI Studio or your Google Cloud Console.

Environment Variable:
The API key is set as an environment variable:

On Windows PowerShell:

text
$env:GEMINI_API_KEY="your_actual_api_key"
On Linux/macOS:

text
export GEMINI_API_KEY="your_actual_api_key"
Model Name:
Use the full model name as shown by the Gemini API.
Example supported models (as of May 2025):

"models/gemini-1.5-pro-latest"

"models/gemini-1.5-pro-002"

"models/gemini-1.5-flash-latest"

"models/gemini-2.0-flash"
You can check available models for your API key by visiting:

text
https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_GEMINI_API_KEY


Project Structure
text
bmi_calculator/
│
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    └── style.css
Key Files
app.py: Main Flask app; handles user input, BMI calculation, Gemini API calls, and formatting of AI output.

templates/index.html: Input form for weight and height.

templates/result.html: Displays the BMI and AI suggestions.

static/style.css: Styles the app for a modern, clean look.

Example Gemini Model API Call
python
import google.generativeai as genai

genai.configure(api_key="your_api_key")
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
response = model.generate_content("Your prompt here.")
print(response.text)
Security Notes
Never commit your API key to version control.

Always use environment variables or secret management for API keys.
References & Inspiration
[Google Gemini API Documentation]

[BMI Gemini Project Example]

[Flask BMI Calculator Projects on GitHub]

[IBM API Gateway Gemini Integration]
