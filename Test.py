from google import genai

# Load the API key from 'apikey.var'
with open("apikey.var", "r", encoding="utf-8") as key_file:
    api_key = key_file.read().strip()

# Initialize the Gemini client with the loaded API key
client = genai.Client(api_key=api_key)


with open("test.txt", "r", encoding="utf-8") as file:
    log_contents = file.read()
    
prompt = f"""
Given the following journalctl log output, analyze it and respond using this exact format:

Major errors: [summary and suggested fix]
Minor errors: [summary and suggested fix]
Other things to be aware of: [summary or notes]
Status: [summary of the system's current state. Fx. current state of script runs, services, etc.]

In case of security issues or major faults, ignore structure and write MAJOR WARNING:
Keep each section to two sentences maximum.

Logs:
{log_contents}
"""


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print(response.text)