# Mathlingo Flask Back-end
This is the backend for mathlingo. It is python application `main.py` which sets up a flask server back-end.
This back-end will return a formatted JSON list of math questions as in the bottom of this `README.md`.

# 1. Prerequisites
Python	 3.10 – 3.12	Match the Docker/PA server runtime if you deploy.
git	any modern	To clone the repo.
API-Key model-4o Obtain a key through the OpenAI API

# 2. Installtion
Enter bash.
```
bash
```
Download repo and set up virtual environment.
```
git clone https://github.com/kenmbo/mathlingo-json.git
cd mathlingo-json
unzip mathlingo-json.zip
python3 -m venv ./.mathlingo-venv
source .mathlingo-venv/bin/activate
```
Install dependencies.
```
pip install -r requirements.txt
```
Create .env file (type you API key in this file)
```
touch .env
```
Type API key into the .env file
```
# .env
OPENAI_API_KEY=sk‑...
# Optional: change the default port
PORT=5000
```
Run local server.
```
python3 main.py
```
Click on the links provided in the terminal.
Usually you open FireFox/Chrome, and in the url to:
```
localhost:5000
```
The output should be just a JSON file containing quiz metadata.




----
Note: Alterantively for production, use 
```
gunicorn -b 0.0.0.0:5000 'main:app'
```

# Sample JSON File
The outputted code should look like this:
```
{
  "sat_questions": [
    {
      "difficulty": "medium",
      "math_subject": "Algebra",
      "question": "If 3x + 7 = 19, what is the value of x?",
      "answer_choice_list": [
        "A. 3",
        "B. 4",
        "C. 5",
        "D. 6"
      ],
      "answer": "B"
    },
    {
      "difficulty": "medium",
      "math_subject": "Geometry",
      "question": "What is the measure of each angle in an equilateral triangle?",
      "answer_choice_list": [
        "A. 45 degrees",
        "B. 60 degrees",
        "C. 90 degrees",
        "D. 120 degrees"
      ],
      "answer": "B"
    },
    {
      "difficulty": "medium",
      "math_subject": "Trigonometry",
      "question": "What is the value of sin(30 degrees)?",
      "answer_choice_list": [
        "A. 1/4",
        "B. 1/2",
        "C. √2/2",
        "D. √3/2"
      ],
      "answer": "B"
    },
    {
      "difficulty": "medium",
      "math_subject": "Algebra",
      "question": "What is the solution to the equation 2(x - 3) = 8?",
      "answer_choice_list": [
        "A. x = 2",
        "B. x = 4",
        "C. x = 5",
        "D. x = 7"
      ],
      "answer": "D"
    },
    {
      "difficulty": "medium",
      "math_subject": "Advanced Math",
      "question": "If f(x) = 2x^2 - 3x + 4, what is f(2)?",
      "answer_choice_list": [
        "A. 6",
        "B. 10",
        "C. 14",
        "D. 18"
      ],
      "answer": "C"
    },
    {
      "difficulty": "medium",
      "math_subject": "Problem-Solving and Data Analysis",
      "question": "If the average of four numbers is 24, what is their sum?",
      "answer_choice_list": [
        "A. 96",
        "B. 100",
        "C. 104",
        "D. 108"
      ],
      "answer": "A"
    },
    {
      "difficulty": "medium",
      "math_subject": "Geometry",
      "question": "What is the area of a circle with a radius of 7?",
      "answer_choice_list": [
        "A. 49π",
        "B. 14π",
        "C. 21π",
        "D. 28π"
      ],
      "answer": "A"
    },
    {
      "difficulty": "medium",
      "math_subject": "Trigonometry",
      "question": "What is the value of cos(60 degrees)?",
      "answer_choice_list": [
        "A. 1",
        "B. 1/2",
        "C. √3/2",
        "D. 0"
      ],
      "answer": "B"
    }
  ]
}
```
