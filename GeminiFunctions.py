from google import genai
from google.genai import types
from models import JournalBrief
import subprocess

# Load the API key from 'apikey.var'
with open("apikey.var", "r", encoding="utf-8") as key_file:
    api_key = key_file.read().strip()

# Initialize the Gemini client with the loaded API key
client = genai.Client(api_key=api_key)

def get_journalctl_logs():
    # uses subprocess to fetch 50 lines of journalctl logs
    try:
        result = subprocess.run(
            ["journalctl", "-n", "50", "--no-pager"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error fetching journalctl logs: {e}")
        return None
    

def JournalctlGeminiJSON():
    log_contents = get_journalctl_logs()
    if not log_contents:
        print("No logs retrieved from journalctl.")
        return None
        
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