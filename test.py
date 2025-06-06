from google import genai
from API_KEY import API_KEY  # Assuming you have a file named API_KEY.py with a variable API_KEY

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)