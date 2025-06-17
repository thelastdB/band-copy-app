import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# load prompt templates
from prompt_templates import prompt_templates

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise Exception("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=api_key)


# Load Gemini
model = genai.GenerativeModel("gemini-1.5-flash")

# Mapping from copy type to example file
example_files = {
    "Show Announcement": "show_announcement.txt",
    "New Music Promo": "new_music_promo.txt",
    "Email Blurb": "email_blurb.txt",
}

# Streamlit UI
st.title("Band Copy Generator")

copy_type = st.selectbox("What do you need?", list(example_files.keys()))
details = st.text_area("Details (date, location, vibe, etc.)")

mood = st.selectbox(
    "Choose a mood or tone",
    ["Rebellious", "Rowdy", "Swaggering", "Earnest", "Hopeful", "Mellow", "Grateful"]
)

if st.button("Generate Copy"):
    try:
        example_file_path = f"examples/{copy_type.lower().replace(' ', '_')}.txt"
        with open(example_file_path) as f:
            examples = f.read()

        template = prompt_templates[copy_type]
        prompt = template.format(
            mood=mood.lower(),
            examples=examples,
            details=details.strip()
        )

        response = model.generate_content(prompt)
        st.markdown("### ✏️ Generated Copy")
        st.write(response.text)

    except FileNotFoundError:
        st.error(f"Example file not found for {copy_type}. Make sure a corresponding file exists in /examples.")
