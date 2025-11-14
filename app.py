from flask import Flask, request, jsonify, send_from_directory
from gemini_assistant import GeminiJavaAssistant
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
assistant = GeminiJavaAssistant()

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    image_data = data.get('image', None)
    
    if '{' in user_input and '}' in user_input and not image_data:
        issues = assistant.fallback_assistant.check_code(user_input)
        response = ', '.join(issues)
    else:
        response = assistant.chat(user_input, image_data)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
