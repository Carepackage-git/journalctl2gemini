# journalctl2gemini

**journalctl2gemini** is a CLI toolchain for interpreting Linux system logs using Google's Gemini AI, transforming raw `journalctl` output into structured JSON summaries, and presenting them in customizable, human-friendly formats.

## How it works

1. **Collect logs:**  
   The tool fetches recent logs from `journalctl`.

2. **AI interpretation:**  
   The logs are sent to Gemini, which analyzes and summarizes them, highlighting major errors, minor issues, status, and other notes.

3. **Structured output:**  
   Gemini's response is parsed into JSON, making it easy to process programmatically.

4. **Flexible formatting:**  
   The JSON summary can be formatted in various ways for the CLI—plain text, colorized output, or boxed/pretty-printed styles.

## Example usage

- Get a quick, AI-powered summary of your system logs.
- Pipe the output into your own scripts or monitoring tools.
- Present logs in a clear, readable format for troubleshooting or reporting.
- See `FormatFunctions.py` for included formatting examples.

## Setup

1. **Create a Python virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install requirements:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key:**  
   Create a file named `apikey.var` in the project folder.  
   This file should contain **only** your Gemini API key.

4. **Run the tool:**  
   - For formatted CLI output, call functions from `FormatFunctions.py`.
   - For raw JSON output, call functions from `GeminiFunctions.py`.

## Requirements

- Python 3.8+
- Access to Gemini API
- `boxes` utility (for advanced CLI formatting)
- Linux system with `journalctl`.`Boxes` is needed if you use formatting examples.

## Why?

I am lazy. :)
