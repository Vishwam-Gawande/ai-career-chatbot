# 🤖 AI Career Assistant

An AI-powered chatbot that provides **career guidance for AI/ML roles** including skills, interview prep, and project ideas.

🔗 **Live App:** https://ai-career-chatbot-4a5fxpmrm2gnpuvmkvt4fe.streamlit.app/

---

## 🧠 What This Project Does

This application uses a **real LLM (Large Language Model)** to:

- Answer AI career-related questions
- Generate interview questions
- Suggest skills and learning paths
- Provide actionable career guidance

Unlike rule-based chatbots, this system generates **dynamic, intelligent responses** using AI.

---

## ⚙️ Tech Stack

- Python
- Streamlit (UI)
- OpenRouter API (LLM access)
- Requests (API calls)

---

## 🔥 Key Features

- 💬 Chat-based UI (like ChatGPT)
- 🧠 Context-aware responses (uses conversation history)
- 🎯 Prompt engineering for controlled outputs
- ⚡ Real AI integration (LLM, not hardcoded logic)
- 🔐 Secure API handling using Streamlit Secrets
- 🧹 Clear chat functionality
- ⏳ Loading spinner for better UX

---

## 🧠 How It Works

1. User asks a question
2. System builds a structured prompt using:
   - User input
   - Previous conversation (memory)
3. Prompt is sent to LLM via API
4. AI generates a response
5. Response is displayed in chat UI

---

## 🧪 Example Questions

- What skills are required for AI Engineer?
- Give AI interview questions
- How to build AI projects?
- How to get a job in AI?

---

## ⚠️ Challenges Solved

- Handling API errors (401 authentication issues)
- Secure API key management (no exposure in code)
- Controlling vague AI responses using prompt engineering
- Managing conversation memory effectively

---

## 📈 What I Learned

- Difference between using AI vs building AI systems
- How LLM APIs work in real-world applications
- Prompt engineering for better output control
- Debugging real production issues
- Deploying AI apps to production (Streamlit Cloud)

---

## 👨‍💻 Author

**Vishwam Gawande**  
AI Engineer (in progress 🚀)

---

## ⭐ Future Improvements

- Add user authentication
- Save chat history (database)
- Multi-model support
- Voice-based interaction
- Resume-based career advice

---

## ⚡ Powered By

Real AI (LLM) via OpenRouter