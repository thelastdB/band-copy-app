import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

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

if st.button("Generate Copy"):
    example_file = example_files[copy_type]
    example_path = os.path.join("examples", example_file)
    
    # Safety check: file exists
    if os.path.exists(example_path):
        with open(example_path, "r") as f:
            example_text = f.read()
    else:
        example_text = "(No example text found for this copy type.)"
    prompt = f"""
    You're writing in the voice of an indie alt-country band. Here's an example of our past copy:

    "{example_text}"

    Now write a new {copy_type} based on the following details:
    {details}
    """
    
    response = model.generate_content(prompt)
    st.markdown("### ✏️ Generated Copy")
    st.write(response.text)