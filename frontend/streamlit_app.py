import streamlit as st
import requests
import os

# -----------------------------
# 🧠 Config
# -----------------------------
st.set_page_config(
    page_title="MedChat AI Assistant",
    page_icon="💊",
    layout="centered",
)

# ✅ Use Render environment variable for the backend API
# Change this key to match what you’ll set in Render (FASTAPI_URL)
BACKEND_URL = os.getenv("FASTAPI_URL", "http://127.0.0.1:8000/chat/")

# -----------------------------
# 💡 Sidebar - App Info
# -----------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=80)
    st.title("MedChat AI 💬")
    st.write("A virtual medical assistant that provides basic health guidance and possible medication suggestions.")
    st.markdown("---")
    st.caption("⚠️ Disclaimer: This chatbot does not replace professional medical consultation.")

# -----------------------------
# 🎨 UI Design
# -----------------------------
st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 1px solid #ccc;
        padding: 8px;
    }
    div.stButton > button {
        background-color: #0099ff;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        font-weight: 600;
    }
    div.stButton > button:hover {
        background-color: #007acc;
        color: #f8f8f8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🩺 MedChat AI Assistant")
st.write("Describe your symptoms and get a preliminary analysis with possible medication suggestions.")

# -----------------------------
# 🧍 Patient Info Form
# -----------------------------
with st.form("medchat_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
    with col2:
        sex = st.selectbox("Sex", ["Male", "Female", "Other"])

    message = st.text_area("Describe your symptoms (e.g., headache, fever, sore throat)...", height=100)
    submitted = st.form_submit_button("Ask MedChat")

# -----------------------------
# 🚀 Backend Call
# -----------------------------
if submitted:
    if not message.strip():
        st.warning("Please describe your symptoms before submitting.")
    else:
        with st.spinner("Analyzing your symptoms..."):
            try:
                payload = {"age": age, "sex": sex.lower(), "message": message}
                response = requests.post(BACKEND_URL, json=payload, timeout=60)
                if response.status_code == 200:
                    data = response.json()
                    ai_analysis = data.get("ai_analysis", "No analysis provided.")
                    medication = data.get("prescribed_medication", "No recommendation provided.")

                    st.success("✅ Medical Assessment")
                    st.markdown(f"**AI Analysis:**\n\n{ai_analysis}")
                    st.markdown(f"**💊 Prescribed Medication:**\n\n{medication}")
                else:
                    st.error(f"Server error: {response.text}")
            except Exception as e:
                st.error(f"Could not connect to backend: {e}")

# -----------------------------
# 🧾 Footer
# -----------------------------
st.markdown("---")
st.caption("Powered by FastAPI ⚡ + Streamlit 🌐 + Gemini AI 🧠")
st.caption("Developed by MIKAN Codex")
