import json
from java_learning_assistant import JavaLearningAssistant

assistant = JavaLearningAssistant()

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    user_input = body.get('message', '')
    
    if '{' in user_input and '}' in user_input:
        issues = assistant.check_code(user_input)
        response = ', '.join(issues)
    else:
        response = assistant.chat(user_input)
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'response': response})
    }
