from google import genai
from google.genai import types
from models import JournalBrief

# Load the API key from 'apikey.var'
with open("apikey.var", "r", encoding="utf-8") as key_file:
    api_key = key_file.read().strip()

# Initialize the Gemini client with the loaded API key
client = genai.Client(api_key=api_key)


def JournalctlGeminiJSON():
    #Placeholder for journalctl log fetching
    with open("test.txt", "r", encoding="utf-8") as file:
        log_contents = file.read()
        
    #Uses predefined specific prompt
    with open("prompts/journalctl.txt", "r", encoding="utf-8") as prompt_file:
        prompt_template = prompt_file.read()

    # Combine the prompt template with the log contents
    prompt = f"{prompt_template}\n\nLogs:\n{log_contents}"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0,
            response_mime_type="application/json",
            response_schema=JournalBrief
        )
    )
    # print("DEBUG TEXT:", response.text, "\nDEBUG OVER\n")  # Debugging line to check the raw response text

    response = response.parsed

    # Filter out empty or None fields
    filtered_response = {field_name: value for field_name, value in response if value}
    return filtered_response
    
# For debug:
#if __name__ == "__main__": 
    # print("debugging: ", JournalctlGeminiJSON())