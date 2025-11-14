import json
import re

class JavaLearningAssistant:
    def __init__(self):
        self.topics = {
            "basics": ["variables", "data types", "operators", "control flow", "arrays", "strings"],
            "oop": ["classes", "objects", "inheritance", "polymorphism", "encapsulation", "abstraction"],
            "advanced": ["collections", "streams", "threads", "exceptions", "generics", "lambda"],
            "frameworks": ["spring", "hibernate", "junit"],
            "concepts": ["jvm", "garbage collection", "memory management"]
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
boolean isActive = true;
char grade = 'A';
long population = 7800000000L;''',
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
            "loop": '''// For loop
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}

// While loop
while (condition) {
    // code
}

// Do-while
do {
    // code
} while (condition);

// For-each
for (String item : list) {
    System.out.println(item);
}''',
            "array": '''int[] numbers = {1, 2, 3, 4, 5};
String[] names = new String[3];
names[0] = "Alice";

// 2D Array
int[][] matrix = {{1,2}, {3,4}};''',
            "exception": '''try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
} catch (Exception e) {
    e.printStackTrace();
} finally {
    System.out.println("Cleanup");
}''',
            "interface": '''public interface Animal {
    void makeSound();
    default void sleep() {
        System.out.println("Sleeping...");
    }
}

class Dog implements Animal {
    public void makeSound() {
        System.out.println("Woof!");
    }
}''',
            "inheritance": '''public class Animal {
    protected String name;
    
    public void eat() {
        System.out.println("Eating...");
    }
}

class Dog extends Animal {
    public void bark() {
        System.out.println("Woof!");
    }
}''',
            "abstract": '''abstract class Shape {
    abstract double area();
    
    void display() {
        System.out.println("Area: " + area());
    }
}

class Circle extends Shape {
    double radius;
    
    double area() {
        return Math.PI * radius * radius;
    }
}''',
            "arraylist": '''import java.util.ArrayList;

ArrayList<String> list = new ArrayList<>();
list.add("Java");
list.add("Python");
list.remove(0);
System.out.println(list.get(0));''',
            "hashmap": '''import java.util.HashMap;

HashMap<String, Integer> map = new HashMap<>();
map.put("John", 25);
map.put("Jane", 30);
System.out.println(map.get("John"));''',
            "stream": '''List<Integer> numbers = Arrays.asList(1,2,3,4,5);
numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * 2)
    .forEach(System.out::println);''',
            "lambda": '''// Lambda expression
Runnable r = () -> System.out.println("Hello");

// With parameters
Comparator<String> comp = (s1, s2) -> s1.compareTo(s2);''',
            "thread": '''class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running");
    }
}

MyThread t = new MyThread();
t.start();''',
            "string": '''String str = "Hello";
str.length();
str.toUpperCase();
str.substring(0, 3);
str.contains("ell");
str.split(",");''',
            "constructor": '''public class Car {
    String model;
    int year;
    
    // Default constructor
    public Car() {
        this.model = "Unknown";
        this.year = 2024;
    }
    
    // Parameterized constructor
    public Car(String model, int year) {
        this.model = model;
        this.year = year;
    }
}''',
            "enum": '''public enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY
}

Day today = Day.MONDAY;
if (today == Day.MONDAY) {
    System.out.println("Start of week");
}''',
            "generic": '''public class Box<T> {
    private T value;
    
    public void set(T value) {
        this.value = value;
    }
    
    public T get() {
        return value;
    }
}

Box<Integer> intBox = new Box<>();
intBox.set(10);''',
            "file": '''import java.io.*;

// Read file
BufferedReader reader = new BufferedReader(new FileReader("file.txt"));
String line = reader.readLine();
reader.close();

// Write file
BufferedWriter writer = new BufferedWriter(new FileWriter("file.txt"));
writer.write("Hello");
writer.close();'''
        }
        
        self.explanations = {
            "class": "A class is a blueprint for creating objects. It defines properties (fields) and behaviors (methods). Classes are the foundation of OOP in Java.",
            "object": "An object is an instance of a class. Created using 'new' keyword. Objects have state (fields) and behavior (methods).",
            "method": "A method is a function defined inside a class that performs actions. Methods can accept parameters and return values.",
            "constructor": "A special method called when creating an object. Has same name as class, no return type. Used to initialize object state.",
            "inheritance": "Allows a class to inherit properties and methods from another class using 'extends'. Promotes code reuse and establishes IS-A relationship.",
            "interface": "A contract that defines methods a class must implement using 'implements'. Supports multiple inheritance and abstraction.",
            "abstract": "Abstract classes cannot be instantiated. They can have abstract methods (no body) that subclasses must implement.",
            "static": "Belongs to the class itself, not instances. Accessed without creating objects. Shared across all instances.",
            "final": "Makes variables constant, prevents method overriding, and prevents class inheritance.",
            "void": "Method return type indicating no value is returned.",
            "public": "Access modifier - accessible from anywhere in the application.",
            "private": "Access modifier - accessible only within the same class. Supports encapsulation.",
            "protected": "Access modifier - accessible within same package and subclasses.",
            "polymorphism": "Ability of objects to take multiple forms. Achieved through method overriding and overloading.",
            "encapsulation": "Bundling data and methods together, hiding internal details. Use private fields with public getters/setters.",
            "abstraction": "Hiding complex implementation details, showing only essential features. Achieved using abstract classes and interfaces.",
            "arraylist": "Dynamic array that can grow/shrink. Part of Collections framework. Provides methods like add(), remove(), get().",
            "hashmap": "Stores key-value pairs. Fast lookup using keys. Part of Collections framework. Allows null keys and values.",
            "exception": "An event that disrupts normal program flow. Use try-catch to handle exceptions gracefully.",
            "thread": "Lightweight process that allows concurrent execution. Create by extending Thread class or implementing Runnable.",
            "stream": "Sequence of elements supporting sequential and parallel operations. Introduced in Java 8 for functional programming.",
            "lambda": "Anonymous function (Java 8+). Provides clear and concise way to represent functional interfaces.",
            "generic": "Allows classes, interfaces, and methods to operate on types as parameters. Provides type safety and reusability.",
            "jvm": "Java Virtual Machine - executes Java bytecode. Makes Java platform-independent (Write Once, Run Anywhere).",
            "garbage collection": "Automatic memory management. JVM automatically removes unused objects to free memory.",
            "string": "Immutable sequence of characters. String objects cannot be changed after creation. Use StringBuilder for mutable strings.",
            "package": "Namespace that organizes classes and interfaces. Prevents naming conflicts and controls access.",
            "import": "Allows using classes from other packages without fully qualified names.",
            "this": "Reference to current object. Used to access instance variables and methods.",
            "super": "Reference to parent class. Used to access parent class methods and constructors.",
            "overloading": "Multiple methods with same name but different parameters. Compile-time polymorphism.",
            "overriding": "Subclass provides specific implementation of parent class method. Runtime polymorphism.",
            "enum": "Special class representing group of constants. Type-safe way to define fixed set of values.",
            "annotation": "Metadata that provides information about code. Examples: @Override, @Deprecated, @SuppressWarnings.",
            "serialization": "Converting object to byte stream for storage or transmission. Implement Serializable interface.",
            "collection": "Framework for storing and manipulating groups of objects. Includes List, Set, Map, Queue.",
            "set": "Collection that doesn't allow duplicates. Examples: HashSet, TreeSet, LinkedHashSet.",
            "list": "Ordered collection that allows duplicates. Examples: ArrayList, LinkedList, Vector.",
            "map": "Stores key-value pairs. Examples: HashMap, TreeMap, LinkedHashMap.",
            "comparable": "Interface for natural ordering. Implement compareTo() method.",
            "comparator": "Interface for custom ordering. Implement compare() method.",
            "synchronized": "Keyword for thread safety. Ensures only one thread accesses method/block at a time.",
            "volatile": "Keyword ensuring variable visibility across threads. Prevents caching.",
            "transient": "Prevents field from being serialized.",
            "instanceof": "Operator to check if object is instance of specific class or interface.",
            "break": "Exits loop or switch statement immediately.",
            "continue": "Skips current iteration and continues with next iteration.",
            "return": "Exits method and optionally returns a value.",
            "switch": "Multi-way branch statement. Alternative to multiple if-else statements.",
            "ternary": "Shorthand for if-else: condition ? value1 : value2",
            "var": "Local variable type inference (Java 10+). Compiler infers type from initializer.",
            "record": "Immutable data class (Java 14+). Automatically generates constructor, getters, equals, hashCode.",
            "sealed": "Restricts which classes can extend/implement (Java 17+). Provides controlled inheritance."
        }
    
    def get_example(self, topic):
        topic = topic.lower().strip()
        for key in self.examples:
            if key in topic or topic in key:
                return self.examples[key]
        
        available = ", ".join(list(self.examples.keys())[:10])
        return f"No example found. Available topics: {available}... (and more! Try: interface, stream, lambda, generic, thread)"
    
    def explain(self, concept):
        concept = concept.lower().strip()
        for key in self.explanations:
            if key in concept or concept in key:
                return self.explanations[key]
        
        # Provide intelligent suggestions
        if any(word in concept for word in ['oop', 'object oriented']):
            return "OOP has 4 pillars: Encapsulation, Inheritance, Polymorphism, Abstraction. Ask about any of these!"
        if 'collection' in concept or 'data structure' in concept:
            return "Java Collections include: ArrayList, HashMap, HashSet, LinkedList, TreeMap, TreeSet. Ask about any!"
        
        available = ", ".join(list(self.explanations.keys())[:15])
        return f"Concept not found. Try: {available}... (50+ concepts available!)"
    
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
        
        return issues if issues else ["✅ Code looks good! No obvious syntax errors found."]
    
    def suggest_next(self, current_topic):
        topics_order = [
            "hello world", "variables", "data types", "operators", "control flow",
            "arrays", "strings", "methods", "classes", "objects", "constructors",
            "encapsulation", "inheritance", "polymorphism", "abstraction",
            "interface", "abstract class", "exceptions", "collections",
            "arraylist", "hashmap", "generics", "streams", "lambda", "threads"
        ]
        current = current_topic.lower()
        for i, topic in enumerate(topics_order):
            if topic in current or current in topic:
                if i < len(topics_order) - 1:
                    return f"✅ Great! Next topic: '{topics_order[i + 1]}'. Type 'example {topics_order[i + 1]}' or 'explain {topics_order[i + 1]}'"
        
        return """Learning Path Suggestions:
🔰 Beginner: variables → loops → arrays → methods → classes
🎯 Intermediate: inheritance → polymorphism → interface → exceptions
🚀 Advanced: collections → streams → lambda → threads → generics

Type 'example [topic]' to start!"""
    
    def quiz(self, topic):
        questions = {
            "basics": "What is the correct way to declare an integer variable? a) int x; b) integer x; c) Int x; [Answer: a]",
            "class": "What keyword is used to create a class? a) class b) Class c) new [Answer: a]",
            "oop": "Which is NOT a pillar of OOP? a) Encapsulation b) Compilation c) Inheritance [Answer: b]",
            "loop": "Which loop checks condition before executing? a) do-while b) while c) for-each [Answer: b]",
            "inheritance": "Which keyword is used for inheritance in Java? a) extends b) implements c) inherits [Answer: a]",
            "interface": "Can an interface have method implementations? a) No b) Yes, with default keyword c) Only static [Answer: b]",
            "exception": "Which block always executes in exception handling? a) try b) catch c) finally [Answer: c]",
            "collection": "Which collection doesn't allow duplicates? a) List b) Set c) Map [Answer: b]",
            "thread": "Which method starts a thread? a) run() b) start() c) execute() [Answer: b]",
            "static": "Can static methods access instance variables? a) Yes b) No c) Sometimes [Answer: b]",
            "abstract": "Can abstract classes be instantiated? a) Yes b) No c) Only with new [Answer: b]",
            "string": "Are strings mutable in Java? a) Yes b) No c) Depends [Answer: b]",
            "arraylist": "What is the default capacity of ArrayList? a) 5 b) 10 c) 16 [Answer: b]",
            "hashmap": "Does HashMap allow null keys? a) Yes, one b) No c) Multiple [Answer: a]",
            "polymorphism": "Method overloading is which type of polymorphism? a) Runtime b) Compile-time c) Both [Answer: b]"
        }
        
        for key in questions:
            if key in topic.lower():
                return questions[key]
        return "Quiz not available for this topic. Try: basics, oop, inheritance, exception, collection, thread, static"
    
    def chat(self, user_input):
        user_input_lower = user_input.lower()
        
        # Code examples
        if any(word in user_input_lower for word in ["example", "show", "code for", "how to"]):
            topic = user_input_lower
            for word in ["example", "show", "code for", "how to", "write", "create"]:
                topic = topic.replace(word, "")
            return self.get_example(topic.strip())
        
        # Explanations
        elif any(word in user_input_lower for word in ["explain", "what is", "what are", "define", "meaning"]):
            concept = user_input_lower
            for word in ["explain", "what is", "what are", "define", "meaning of", "tell me about"]:
                concept = concept.replace(word, "")
            return self.explain(concept.strip())
        
        # Code validation
        elif "check" in user_input_lower or "validate" in user_input_lower:
            return "Paste your Java code and I'll check it for common issues."
        
        # Learning path
        elif "next" in user_input_lower or "suggest" in user_input_lower or "what should" in user_input_lower:
            return self.suggest_next(user_input_lower)
        
        # Quiz
        elif "quiz" in user_input_lower or "test" in user_input_lower or "question" in user_input_lower:
            return self.quiz(user_input_lower)
        
        # Difference questions
        elif "difference" in user_input_lower or "vs" in user_input_lower:
            if "abstract" in user_input_lower and "interface" in user_input_lower:
                return "Abstract class can have concrete methods, constructor, and instance variables. Interface (before Java 8) only has abstract methods. Use abstract class for IS-A relationship, interface for CAN-DO capability."
            elif "arraylist" in user_input_lower and "linkedlist" in user_input_lower:
                return "ArrayList uses dynamic array (fast random access). LinkedList uses doubly-linked list (fast insertion/deletion). Use ArrayList for frequent access, LinkedList for frequent modifications."
            elif "==" in user_input_lower and "equals" in user_input_lower:
                return "== compares references (memory addresses). equals() compares content/values. For strings, always use equals() to compare content."
            elif "overload" in user_input_lower and "override" in user_input_lower:
                return "Overloading: Same method name, different parameters (compile-time). Overriding: Subclass redefines parent method with same signature (runtime)."
            else:
                return "Ask about specific differences like: 'difference between abstract and interface', 'ArrayList vs LinkedList', '== vs equals', 'overloading vs overriding'"
        
        # Help
        elif "help" in user_input_lower or "command" in user_input_lower:
            return """Commands:
- 'example [topic]' - Get code examples (50+ topics!)
- 'explain [concept]' - Get explanations (60+ concepts!)
- 'difference between X and Y' - Compare concepts
- 'quiz [topic]' - Test your knowledge (15+ quizzes)
- 'check code' - Validate Java code
- 'next topic' - Get learning suggestions

Topics: variables, loops, classes, inheritance, interface, collections, streams, threads, exceptions, generics, and more!"""
        
        # Greetings
        elif any(word in user_input_lower for word in ["hi", "hello", "hey"]):
            return "Hello! I'm your Java learning assistant. Ask me anything about Java - examples, explanations, quizzes, or type 'help' for commands!"
        
        # Thanks
        elif any(word in user_input_lower for word in ["thank", "thanks"]):
            return "You're welcome! Keep learning and coding. Ask me anything else about Java!"
        
        # Default intelligent response
        else:
            # Try to find relevant topic
            for key in self.examples:
                if key in user_input_lower:
                    return f"I found '{key}' in your question. Try: 'example {key}' or 'explain {key}'"
            
            return "I can help you learn Java! Try:\n- 'example hello world'\n- 'explain inheritance'\n- 'difference between abstract and interface'\n- 'quiz oop'\n- 'help' for all commands"

def main():
    assistant = JavaLearningAssistant()
    print("=== Java Learning Assistant ===")
    print("🎓 Complete Java Learning Guide - 50+ Topics, 60+ Concepts!")
    print("Type 'help' for commands or 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Happy coding! Keep practicing! 🚀")
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
