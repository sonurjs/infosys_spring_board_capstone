import streamlit as st
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

st.set_page_config(
    page_title="AI Learning Buddy Sonu",
    page_icon="🎓"
)

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🎓 AI Learning Buddy Sonu")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if not topic.strip():
        st.warning("Please enter a topic.")
        st.stop()

    if option == "Explain Concept":
        prompt = f"Explain {topic} in simple language for a beginner."

    elif option == "Real-Life Example":
        prompt = f"Give one simple real-life example of {topic}."

    elif option == "Generate Quiz":
        prompt = f"""
        Create 5 multiple-choice questions on {topic}.

        Each question should have:
        - 4 options (A, B, C, D)
        - Correct answer
        - Short explanation
        """

    else:
        prompt = topic

    try:
        with st.spinner("Generating response..."):
            response = model.generate_content(prompt)

        st.success("Response Generated")
        st.write(response.text)

    except ResourceExhausted:
        st.error("❌ Gemini API quota exceeded. Please try again later or use another API key.")

    except Exception as e:
        st.error(f"Error: {e}")
