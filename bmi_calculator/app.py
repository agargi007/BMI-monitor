import os
import re
from flask import Flask, render_template, request
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

app = Flask(__name__)

import re

def numbered_tips_to_html(text):
    # Extract the intro (before the tips)
    split = re.split(r'1\.', text, maxsplit=1)
    intro = split[0].strip()
    tips_block = "1." + split[1] if len(split) > 1 else ""

    # Find all numbered tips (e.g., 1. ... 2. ... 3. ...)
    tips = re.findall(r'\d+\.\s*(.*?)((?=\d+\.)|$)', tips_block, re.DOTALL)
    if tips:
        html_list = "<ol>"
        for tip, _ in tips:
            html_list += f"<li>{tip.strip()}</li>"
        html_list += "</ol>"
        return f"<p>{intro}</p>{html_list}"
    else:
        return f"<p>{text.strip()}</p>"

def get_bmi_feedback_from_gemini(bmi, weight, height):
    prompt = (
        f"A user has a BMI of {bmi}, weight {weight} kg, and height {height} m. "
        "Tell them their BMI category, what it means for their health, and give 3 helpful tips to improve or maintain their BMI. "
        "Make the response friendly and easy to understand."
    )
    response = model.generate_content(prompt)
    return numbered_tips_to_html(response.text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = round(weight / (height ** 2), 2)
        ai_feedback = get_bmi_feedback_from_gemini(bmi, weight, height)
        return render_template('result.html', bmi=bmi, ai_feedback=ai_feedback)
    return render_template('index.html')

if __name__ == '__main__':
    import threading
    import webbrowser
    threading.Timer(1.5, lambda: webbrowser.open('http://127.0.0.1:5000')).start()
    app.run(debug=True)
