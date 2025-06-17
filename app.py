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
st.title("HSBA Copy Generator")

copy_type = st.selectbox("What do you need?", list(prompt_templates.keys()))

# Fetch input guidance for selected template
input_instructions = prompt_templates[copy_type]["instructions"]

# Show a mood selector
mood = st.selectbox(
    "Choose a mood or tone",
    ["Rebellious", "Rowdy", "Swaggering", "Earnest", "Hopeful", "Mellow", "Grateful"]
)

# Show guidance for details
st.caption(f"💡 What to include: {input_instructions}")
details = st.text_area("Details")

# Generate on button click
if st.button("Generate Copy"):
    try:
        example_file_path = f"examples/{copy_type.lower().replace(' ', '_')}.txt"
        with open(example_file_path) as f:
            examples = f.read()

        # Get the actual template string
        template = prompt_templates[copy_type]["template"]
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