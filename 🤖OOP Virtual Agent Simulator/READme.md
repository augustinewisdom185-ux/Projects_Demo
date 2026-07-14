# 🤖 ECHO: Self-Learning AI ChatBot Simulator

A smart, object-oriented virtual assistant built in Python that dynamically references a local knowledge base to answer user inquiries. If the assistant encounters an unknown question, it triggers an interactive learning pipeline to expand its memory file permanently.

This updated version introduces a stylized console interface boot sequence, input standardization updates, and protected crash-prevention overrides.

---

## 🚀 Key Architectural Features

- **Stylized Console Interface:** Utilizes a nested function closure (`print_banner()`) inside the runtime engine to render a custom ASCII art splash banner upon script activation.
- **Dynamic Local Memory Engine:** References and manages data using a robust, structured JSON format template (`{"Conversation": []}`) mapped directly to the local file system.
- **Hierarchical Inheritance Engine:** Utilizes an abstraction layer class structure (`Agent` parent matrix) to dynamically inherit system parameter tags like `self.name` down to downstream child models via `super().__init__(name)`.
- **Text Standardization Patch:** Implements localized `.strip().lower()` input sanitization filters to ensure questions match entries securely, regardless of casing or trailing spaces.
- **Interceptive Live Computations:** Utilizes system-level chronological tracking via Python's native `datetime` module to bypass database checks and generate real-time local hardware time calculations accurately.
- **Fail-Safe Exception Handling:** Features dedicated exception monitors, including defensive patches for `JSONDecodeError` and a graceful shutdown handler for `KeyboardInterrupt` actions to prevent system corruption during user data entry.

---

## 🛠️ JSON Data Storage Matrix Layout

The persistent database records knowledge sets automatically using uniform dictionary collections appended inside a standardized list array wrapper within your `Knowledge_file.json` folder structure:

```json
{
    "Conversation": [
        {
            "question": "what is python?",
            "answer": "Python is a clean object-oriented programming language."
        }
    ]
}
```

---

## 📦 How to Execute the Simulator

1. Clone or copy the program source code files into your local directory space.
2. Initialize the application container by triggering the terminal runner script:
   ```bash
   python chatbot.py
   ```
3. Look for the custom `ECHO` boot screen interface in your terminal console.
4. Input specific queries such as `what is the time?` or `time` to output live clock responses.
5. Exit runtime loops securely at any prompt threshold by feeding the terminator utility command: `quit`

---

## 📈 Future Architecture Roadmap
- [ ] **Decoupled KnowledgeBase Utility Module:** Extract data file operations from the structural loop into an independent class system.
- [ ] **Persistent Interaction Memory Logger:** Set up a separate logging system that tracks chronological histories using time-stamped log file profiles.
- [ ] **Advanced Text Processing Optimization:** Add validation to protect records against completely blank space values or punctuation errors.
