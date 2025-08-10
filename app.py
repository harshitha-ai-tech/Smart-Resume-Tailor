from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
#openai.api_key = os.getenv("OPENAIAPIKEY")
# API key line commented out for public repo to avoid exposing secret key

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

@app.route('/tailor', methods=['POST'])
def tailor_resume():
    data = request.json
    resume = data.get('resume')
    job_desc = data.get('job')

    prompt = f"""Tailor the following resume to match this job description by rewriting the content using matching skills, action words, and keywords. 
    Resume:\n{resume}
    Job Description:\n{job_desc}
    Output the new tailored resume.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    tailored_resume = response['choices'][0]['message']['content']
    return jsonify({"result": tailored_resume})

if __name__ == '__main__':
    app.run(debug=True)
