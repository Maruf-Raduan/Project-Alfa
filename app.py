from flask import Flask, request, jsonify, send_from_directory
from java_learning_assistant import JavaLearningAssistant

app = Flask(__name__)
assistant = JavaLearningAssistant()

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    
    if '{' in user_input and '}' in user_input:
        issues = assistant.check_code(user_input)
        response = ', '.join(issues)
    else:
        response = assistant.chat(user_input)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
