# Smart Resume Tailor

Smart Resume Tailor is a Flask web app that uses OpenAI’s GPT-4 to customize your resume based on job descriptions. It rewrites your resume with relevant skills and keywords to help you stand out in job applications.

## Features

- AI-powered resume tailoring  
- REST API endpoint for easy integration  
- Secure API key management with `.env`  
- CORS enabled for frontend connectivity  

## Setup Instructions

### Prerequisites

- Python 3.7+  
- OpenAI API key  
- pip package manager  

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resume-tailor.git
   cd resume-tailor
   
Create and activate a virtual environment (optional but recommended):
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Create a .env file and add your OpenAI API key:
OPENAI_API_KEY=your_api_key_here
Running the App
Start the Flask server:
python app.py
The server will run at http://127.0.0.1:5000/.

Usage:
{
  "resume": "Your resume text here...",
  "job": "Job description text here..."
}
Response:

{
  "result": "Tailored resume text..."
}
