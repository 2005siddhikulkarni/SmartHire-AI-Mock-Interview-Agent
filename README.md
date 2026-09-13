# 🤖 SmartHire – AI Mock Interview Agent

A **Python-based AI Mock Interview Agent** that conducts technical interviews using **Llama 3 and Ollama**. The system evaluates candidate answers using prompt engineering, provides detailed feedback, calculates performance scores, maintains interview history, and generates a final interview report.

---

## 🚀 Features

* 🤖 AI-powered technical interview evaluation
* 🧠 Llama 3 integration using Ollama
* ✍️ Prompt engineering for structured answer evaluation
* 📊 Answer scoring from 0–10
* 📝 Technical evaluation and feedback
* 🔍 Identification of missing technical points
* 💡 Improved answer generation
* 🎯 Interview improvement suggestions
* 📚 Topic-wise interview mode
* 🗂️ Interview history tracking
* 📈 Question-wise and overall performance scoring
* 📄 Automated final interview report
* ⚠️ Exception handling for LLM communication

---

## 🛠️ Technologies Used

* **Python**
* **Llama 3**
* **Ollama**
* **REST API**
* **Prompt Engineering**
* **Requests**
* **Object-Oriented Programming**
* **Exception Handling**

---

## 📂 Project Structure

```text
SmartHire-AI-Agent/
│
├── main.py
├── interview_agent.py
├── llm_engine.py
├── questions.py
├── report_generator.py
│
└── reports/
    └── interview_report.txt
```

### File Description

| File                  | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| `main.py`             | Main application and interview flow                                |
| `interview_agent.py`  | Core AI interview agent, evaluation, scoring and report generation |
| `llm_engine.py`       | Connects Python application with Llama 3 through Ollama API        |
| `questions.py`        | Technical interview question bank                                  |
| `report_generator.py` | Saves generated interview reports                                  |
| `reports/`            | Stores generated interview reports                                 |

---

## 🔄 How It Works

```text
Start Application
       ↓
Enter Student Name
       ↓
Select Interview Mode
       ↓
Full Interview / Topic-wise Interview
       ↓
Display Technical Question
       ↓
Enter Candidate Answer
       ↓
Generate Structured Prompt
       ↓
Send Prompt to Llama 3
       ↓
Receive AI Evaluation
       ↓
Extract Score
       ↓
Store Interview History
       ↓
Calculate Overall Performance
       ↓
Generate Final Report
       ↓
Save Report
```

---

## 🧠 AI Evaluation

For every candidate response, the AI evaluates:

* **Score:** Rating out of 10
* **Evaluation:** Correct, partially correct, or incorrect
* **Missing Points:** Important technical concepts missing from the answer
* **Improved Answer:** Better student-friendly answer
* **Interview Suggestion:** Practical improvement suggestion

The project creates a structured prompt containing the candidate name, topic, question, and answer before sending it to Llama 3.

---

## 📚 Interview Topics

The question bank can contain technical questions from areas such as:

* Python
* OOP
* Data Structures
* Machine Learning
* Deep Learning
* Data Science
* NLP
* Generative AI
* AI Agents
* SQL
* Projects

The application supports both **full interview** and **topic-wise interview** modes.

---

## ⚙️ Requirements

Install Python and the required Python package:

```bash
pip install requests
```

You also need to install **Ollama** and have the **Llama 3 model** available locally.

---

## ▶️ How to Run

### 1. Run the application

```bash
python main.py
```

---

## 💻 Interview Modes

### 1. Full Interview

Runs the complete interview using the available question bank.

### 2. Topic-wise Interview

Allows the candidate to select a specific technical topic and practice questions from that topic.

### 3. Exit

Closes the application.

---

## 📊 Performance Report

After completing the interview, the system generates a report containing:

* Student name
* Total questions
* Total score
* Average score
* Overall performance
* Question-wise analysis
* Candidate answers
* AI-generated evaluations
* Individual scores

The report is saved in the `reports` folder.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Build a practical **AI Agent** using Python.
2. Integrate a locally running **Large Language Model**.
3. Apply **Prompt Engineering** for structured responses.
4. Automate technical interview evaluation.
5. Provide personalized feedback to candidates.
6. Track interview performance.
7. Generate an automated interview report.

---

## 🔮 Future Enhancements

* Voice-based interviews
* Web-based Streamlit interface
* Resume-based question generation
* Adaptive difficulty levels
* Speech-to-text integration
* Candidate performance visualization
* Question generation using LLMs
* Persistent database for interview history
* Multiple LLM/model support

---

## 👩‍💻 Author

**Siddhi Milind Kulkarni**

Python Developer | AI/ML Engineer Fresher

GitHub: [2005siddhikulkarni](https://github.com/2005siddhikulkarni)

---

## ⭐ Acknowledgement

Developed as part of practical learning and project development in **Python, Data Science, Machine Learning, Generative AI, and Large Language Models**.
