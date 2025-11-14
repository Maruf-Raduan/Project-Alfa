import json
import re

class JavaLearningAssistant:
    def __init__(self):
        self.topics = {
            "basics": ["variables", "data types", "operators", "control flow"],
            "oop": ["classes", "objects", "inheritance", "polymorphism", "encapsulation"],
            "advanced": ["collections", "streams", "threads", "exceptions"]
        }
        
        self.examples = {
            "hello world": '''public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}''',
            "variables": '''int age = 25;
String name = "John";
double price = 19.99;
boolean isActive = true;''',
            "class": '''public class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() { return name; }
    public int getAge() { return age; }
}''',
            "loop": '''for (int i = 0; i < 10; i++) {
    System.out.println(i);
}

while (condition) {
    // code
}''',
            "array": '''int[] numbers = {1, 2, 3, 4, 5};
String[] names = new String[3];
names[0] = "Alice";''',
            "exception": '''try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
} finally {
    System.out.println("Cleanup");
}'''
        }
        
        self.explanations = {
            "class": "A class is a blueprint for creating objects. It defines properties (fields) and behaviors (methods).",
            "object": "An object is an instance of a class. Created using 'new' keyword.",
            "method": "A method is a function defined inside a class that performs actions.",
            "constructor": "A special method called when creating an object, same name as class.",
            "inheritance": "Allows a class to inherit properties and methods from another class using 'extends'.",
            "interface": "A contract that defines methods a class must implement using 'implements'.",
            "static": "Belongs to the class itself, not instances. Accessed without creating objects.",
            "void": "Method return type indicating no value is returned.",
            "public": "Access modifier - accessible from anywhere.",
            "private": "Access modifier - accessible only within the same class."
        }
    
    def get_example(self, topic):
        topic = topic.lower().strip()
        for key in self.examples:
            if key in topic or topic in key:
                return self.examples[key]
        return "No example found. Try: hello world, variables, class, loop, array, exception"
    
    def explain(self, concept):
        concept = concept.lower().strip()
        for key in self.explanations:
            if key in concept or concept in key:
                return self.explanations[key]
        return "Concept not found. Try: class, object, method, constructor, inheritance, interface, static"
    
    def check_code(self, code):
        issues = []
        if not re.search(r'public\s+class\s+\w+', code):
            issues.append("Missing public class declaration")
        if 'main' in code and not re.search(r'public\s+static\s+void\s+main', code):
            issues.append("main method should be: public static void main(String[] args)")
        if code.count('{') != code.count('}'):
            issues.append("Mismatched braces")
        if code.count('(') != code.count(')'):
            issues.append("Mismatched parentheses")
        
        return issues if issues else ["Code looks good!"]
    
    def suggest_next(self, current_topic):
        topics_order = ["hello world", "variables", "operators", "control flow", 
                       "arrays", "methods", "classes", "objects", "inheritance", 
                       "exceptions", "collections"]
        current = current_topic.lower()
        for i, topic in enumerate(topics_order):
            if current in topic:
                if i < len(topics_order) - 1:
                    return f"Next: Learn about '{topics_order[i + 1]}'"
        return "Try exploring: OOP concepts, Collections, or Streams"
    
    def quiz(self, topic):
        questions = {
            "basics": "What is the correct way to declare an integer variable? a) int x; b) integer x; c) Int x;",
            "class": "What keyword is used to create a class? a) class b) Class c) new",
            "oop": "Which is NOT a pillar of OOP? a) Encapsulation b) Compilation c) Inheritance",
            "loop": "Which loop checks condition before executing? a) do-while b) while c) for-each"
        }
        
        for key in questions:
            if key in topic.lower():
                return questions[key]
        return "Quiz not available for this topic"
    
    def chat(self, user_input):
        user_input = user_input.lower()
        
        if "example" in user_input or "show" in user_input:
            topic = user_input.replace("example", "").replace("show", "").strip()
            return self.get_example(topic)
        
        elif "explain" in user_input or "what is" in user_input:
            concept = user_input.replace("explain", "").replace("what is", "").strip()
            return self.explain(concept)
        
        elif "check" in user_input:
            return "Paste your Java code and I'll check it for common issues."
        
        elif "next" in user_input or "suggest" in user_input:
            return self.suggest_next(user_input)
        
        elif "quiz" in user_input or "test" in user_input:
            return self.quiz(user_input)
        
        elif "help" in user_input:
            return """Commands:
- 'example [topic]' - Get code examples
- 'explain [concept]' - Get explanations
- 'check code' - Validate Java code
- 'next topic' - Get learning suggestions
- 'quiz [topic]' - Test your knowledge"""
        
        else:
            return "I can help you learn Java! Try: 'example hello world', 'explain class', 'quiz basics', or 'help'"

def main():
    assistant = JavaLearningAssistant()
    print("=== Java Learning Assistant ===")
    print("Type 'help' for commands or 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Happy coding!")
            break
        
        if not user_input:
            continue
        
        # Check if it's code to validate
        if '{' in user_input and '}' in user_input:
            issues = assistant.check_code(user_input)
            print(f"Assistant: {', '.join(issues)}\n")
        else:
            response = assistant.chat(user_input)
            print(f"Assistant: {response}\n")

if __name__ == "__main__":
    main()
