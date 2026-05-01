import streamlit as st
import requests

API_KEY = "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"

st.set_page_config(page_title="AI Career Assistant", page_icon="🤖")

st.title("🤖 AI Career Assistant")
st.info("💡 Ask about AI jobs, skills, projects, or interviews.")
st.success("🚀 Get AI Career Guidance like a Pro Engineer")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("🧹 Clear Chat"):
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


def generate_prompt(user_input, history):
    context = " ".join([m["content"] for m in history[-4:]])

    return f"""
You are an expert AI Career Coach helping users get jobs in AI/ML.

Conversation:
{context}

User Question:
{user_input}

Instructions:
- Give exactly 3–5 bullet points
- If user asks for "questions", ONLY return questions (not advice)
- If user asks for guidance, return steps
- Be direct and specific
- Avoid generic advice
- Focus on AI/ML domain

Answer:
"""


def call_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert AI Career Coach. Be practical, concise, and avoid generic advice."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            return "⚠️ Error: Unable to fetch response. Please try again."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


user_input = st.chat_input("Ask about AI jobs, skills, projects, or interviews...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = generate_prompt(user_input, st.session_state.messages)

    with st.spinner("Thinking... 🤔"):
        ai_response = call_ai(prompt)

    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    with st.chat_message("assistant"):
        st.subheader("🤖 AI Response:")
        st.markdown(ai_response)

st.markdown("---")
st.caption("⚡ Powered by Real AI (LLM)")
st.markdown("Built by Vishwam 🚀 | AI Engineer in Progress")