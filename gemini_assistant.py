import os
import base64
import google.generativeai as genai
from java_learning_assistant import JavaLearningAssistant
from PIL import Image
import io

class GeminiJavaAssistant:
    def __init__(self):
        self.fallback_assistant = JavaLearningAssistant()
        self.api_key = os.environ.get('GEMINI_API_KEY')
        
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash')
            self.use_gemini = True
        else:
            self.use_gemini = False
            print("⚠️  No Gemini API key found. Using fallback assistant.")
    
    def chat(self, user_input, image_data=None):
        # Check if it's code validation
        if '{' in user_input and '}' in user_input and not image_data:
            return ', '.join(self.fallback_assistant.check_code(user_input))
        
        # Use Gemini if available
        if self.use_gemini:
            try:
                if image_data:
                    # Handle image analysis
                    image_bytes = base64.b64decode(image_data.split(',')[1])
                    image = Image.open(io.BytesIO(image_bytes))
                    
                    prompt = f"""You are a Java learning assistant. Analyze this image:

User question: {user_input if user_input else 'Analyze this Java code or diagram'}

Rules:
- If it's Java code, explain what it does
- Point out any errors or improvements
- If it's a diagram, explain the Java concept
- Be educational and helpful
- Provide code examples if relevant"""
                    
                    response = self.model.generate_content([prompt, image])
                    return response.text
                else:
                    # Text-only query
                    prompt = f"""You are a Java learning assistant. Answer this question about Java programming:

Question: {user_input}

Rules:
- Keep answers concise and educational
- Include code examples when relevant
- Focus on Java programming concepts
- If asked for examples, provide working Java code
- Be friendly and encouraging
- If it's not Java-related, politely redirect to Java topics"""

                    response = self.model.generate_content(prompt)
                    return response.text
            
            except Exception as e:
                print(f"Gemini API error: {e}")
                return self.fallback_assistant.chat(user_input)
        
        # Fallback to rule-based assistant
        return self.fallback_assistant.chat(user_input)
