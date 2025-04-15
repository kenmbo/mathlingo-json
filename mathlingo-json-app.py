from openai import OpenAI
import json
from flask import Flask, jsonify

#================
# Set up OpenAI API client
path = "api_key"
with open(path, "r") as f:
    api_key = f.read().strip()

client = OpenAI(
    api_key = api_key
)

#================
# Formatting the prompt for OpenAPI to read
def createPrompt(num_questions=10):
    # createPrompt(): Create a prompt for OpenAI API to read
    prompt = f"""Return valid JSON output. 
    You are creating {num_questions} practice multiple-choice questions based on the SAT math section.
    First, choose a random subject for the 'subject' column. The subjects are: 'Algebra', 'Advanced Math', 'Problem-Solving and Data Analysis', 'Math word problems', 'Geometry', or 'Trigonometry'.
    Then come up with a question prompt onto the 'question' column, and then four answer options into the 'answer_choice_list' column list. 
    Only one option must be correct.
    The correct option's corresponding letter will be in the 'answer' column. """
    return prompt

# example_json is the structure I want the JSON to be as.
example_json = {
	"sat_questions":[
	{
        "math_subject": "Subject",
		"question": "Question prompt line.",
		"answer_choice_list": ["A. Option A.", "B. Option B.", "C. Option C.", "D. Option D."],
		"answer": "A",
	}
	]
}

def createJSON(num_questions=10):
    # createJSON(): Call openAI
    prompt = createPrompt(num_questions)
    chat_completion = client.chat.completions.create(
    	model = "gpt-4o-mini",
    	response_format={"type": "json_object"},
    	messages = [
            {
                "role":"system",
                "content":"Return valid JSON code. The data schema should look like this:" + json.dumps(example_json)
            },
            {
                "role":"system",
                "content":prompt
            }
        ]
    )
    return chat_completion.choices[0].message.content


app = Flask(__name__)
@app.route('/')
def data_endpoint():
    data = createJSON(4)
    try:
        json.loads(data)
        return data, {'Content-Type': 'application/json'}
    except ValueError:
       return jsonify({"message": "Invalid JSON"}), 400

if __name__ == '__main__':
    app.run()
