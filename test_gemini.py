import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise Exception("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=api_key)

def test_gemini():
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content("Write a catchy tagline for a new indie band.")
    print(response.text)

if __name__ == "__main__":
    test_gemini()



# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# for m in genai.list_models():
#     print(m.name, " |  supports generateContent:", "generateContent" in m.supported_generation_methods)
