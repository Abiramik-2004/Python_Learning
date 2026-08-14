Compiler
--------
A Compiler is a software tool that converts an entire High-Level Language (HLL) program into Object Code, and then generates Machine Code (Binary/Executable) before execution.

Compilation Process
-------------------
Source Code (.java/.c)
    │
    ▼
Compiler
    │
    ▼
Object Code (.obj)
    │
    ▼
Machine Code / Binary (.exe)

Characteristics
---------------
● Converts the entire program at once
● Generates Object Code first
● Produces a Binary/Executable file
● Executes faster because compilation is done only once
● Errors are reported after compiling the complete program

Example Languages
-----------------
● C
● C++
● Java (compiles to Bytecode, then JVM executes it)

Performance Example
-------------------
Program Size Compilation Time
1,000 Lines of Code (1 KLOC) 2–3 time units (approx.)

Interpreter
-----------
An Interpreter is a software tool that converts a High-Level Language (HLL) directly into
Machine Instructions and executes the program line by line.

Interpretation Process
-----------------------
Source Code (.py)
    │
    ▼
Interpreter
    │
    ▼
Execute Line by Line

Characteristics
----------------
● Converts one line at a time
● No separate object code is generated
● Stops immediately when an error occurs
● Easier for debugging
● Execution is comparatively slower
Example Languages
● Python
● JavaScript
● Ruby

Performance Example
--------------------
Program Size Interpretation Time
1,000 Lines of Code (1 KLOC) ~1000 time units (illustrative)

Compiler vs Interpreter
-----------------------
Feature Compiler Interpreter
Translation Entire program Line by line
Object Code Generated Not generated separately
Speed Faster Slower
Error Detection After compilation Immediately at the error line
Executable File Yes No
Examples C, C++, Java Python, JavaScript, Ruby

Popular Technologies Using Python
----------------------------------
Python is widely used in:
● 🤖 Artificial Intelligence (AI)
● 🧠 Machine Learning (ML)
● 📊 Data Science
● 📈 Data Analytics
● 💬 Chatbots
● 🤖 AI Agents
● 🌐 Web Development (Flask, Django)
● 🔒 Cyber Security
● ☁️ Cloud Automation

Python Installation
-------------------
Step 1
Visit the official website:
https://www.python.org
Step 2
Click Downloads.
Step 3
Download the latest stable version for your operating system.
Step 4
Run the installer.
✅ Check "Add Python to PATH"
Click Install Now.
Step 5
Verify the installation.
Open Command Prompt (CMD) and type:
python --version
or
python -V
Example Output
Python 3.14.5

How Python Executes a Program
------------------------------
Suppose you write:
print("Python")
Save it as:
sample.py

Execution flow:
---------------
sample.py
    │
    ▼
Python Interpreter
    │
    ▼
Python Virtual Machine (PVM)
    │
    ▼
Bytecode (.pyc)
    │
    ▼
Output

Python
-------
Python Execution Architecture
Python Program (.py)
│
▼
Python Interpreter
│
▼
Compiler
(Generates Bytecode)
│
▼
.pyc (Bytecode)
│
▼
Python Virtual Machine (PVM)
│
▼
Machine Instructions
│
▼
Output

Note: Python is often called an interpreted language, but internally it first compiles
the source code into Bytecode (.pyc) and then the Python Virtual Machine (PVM)
interprets that bytecode.
IPO Model in Python
Input
The user writes a Python program.
Example:
print("Hello")

Processing
----------
● Python Interpreter reads the source code.
● Converts it into Bytecode (.pyc).
● The Python Virtual Machine (PVM) executes the bytecode.
Output
Hello