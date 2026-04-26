# SmartPrep AI 📚

> Learn Smarter, Faster, Better

## Overview

SmartPrep AI is an AI-powered study assistant designed to help students learn more effectively. It transforms lengthy study notes into concise summaries, generates quiz questions for self-assessment, and explains complex concepts in simple language.

## Problem Statement

Students often spend significant time summarizing notes, creating practice questions, and understanding difficult concepts. This process can be time-consuming and inefficient.

## Solution

SmartPrep AI automates the learning process by instantly converting study material into:

* Concise summaries
* Practice quiz questions
* Simplified explanations

## Features

* 📌 Automatic note summarization
* 📝 AI-generated quiz questions
* 💡 Simple explanations for complex topics
* 🌐 Clean and user-friendly web interface
* ⚡ Fast AI responses powered by Groq API

## Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python, Flask
* **AI Integration:** Groq API
* **Environment Management:** Python Dotenv

## Project Structure

```text
smartprep-ai/
│── app.py
│── requirements.txt
│── .env
│── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/smartprep-ai.git
```

2. Navigate to the project directory:

```bash
cd smartprep-ai
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

5. Run the application:

```bash
python app.py
```

6. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## How It Works

1. Paste your study notes into the input box.
2. Click the **Generate** button.
3. Receive:

   * A concise summary
   * Quiz questions
   * A simplified explanation

## Future Enhancements

* File upload support (PDF, DOCX)
* Personalized study plans
* Flashcard generation
* Multi-language support
* Voice-based learning assistance

## Use Cases

* Exam preparation
* Quick revision
* Self-assessment through quizzes
* Simplifying complex topics

## Contributors

* Roshni Katikala

## License

This project is licensed under the MIT License.

---

⭐ If you like this project, consider giving it a star on GitHub!