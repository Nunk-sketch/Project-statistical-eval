from google import genai
from API_KEY import API_KEY  # Assuming you have a file named API_KEY.py with a function API_KEY that returns the api key as a string
import datetime

client = genai.Client(api_key=API_KEY())

prompt_1 = "Skriv et essay på dansk. Du bestemmer selv emnet."
response_1 = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt_1
)
content = f"Prompt: {prompt_1}\n\nAnswer: {response_1.text}"

prompt_2 = f"List the English words in this text as a python list: {response_1}"
response_2 = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt_2
)
print(response_2.text)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"output/output_{timestamp}.txt"
with open(filename, "w") as file:
    file.write(content)