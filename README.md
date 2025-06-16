# 🤖 AI Chatbot using FastAPI & Gemini API

This is a simple AI chatbot application built with **FastAPI** on the backend, using **Google's Gemini API** for AI-generated responses. It includes a lightweight HTML frontend for real-time chatting.

---

## 🚀 Features

- ⚡ FastAPI backend with RESTful `/chat` endpoint
- 🤖 Integration with Gemini (Google Generative AI)
- 🌐 Simple HTML/CSS frontend for chatting
- 🔄 Real-time response using JavaScript `fetch()`

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python 3.12)
- **Frontend:** HTML + CSS + JavaScript
- **AI API:** Google Generative AI (Gemini)
- **Hosting:** Local (can be extended to Docker, Render, etc.)

## ⚙️ Setup Instructions

### 1. Clone the repo

git clone https://github.com/18Prashanth/ChatBot.git
cd ChatBot

### 2. Create & activate virtual environment

python -m venv venv
venv\Scripts\activate # On Windows

# or

source venv/bin/activate # On macOS/Linux

### 3. Install dependencies

pip install -r requirements.txt

### 4. Set your Gemini API key

GEMINI_API_KEY=your_api_key_here

### 5. Run the server

uvicorn main:app --reload

```

```
