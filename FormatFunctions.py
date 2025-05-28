import subprocess
import shutil
import textwrap
import GeminiFunctions

#This scripts takes all jsons and colors the titles according to severity, then prints.
def format_basic_ctl_json():
    ctloutput = GeminiFunctions.JournalctlGeminiJSON()
    if not ctloutput:
        print ("No output or status, check prompt.")
    else:
        # Print each field with appropriate formatting
        print("\033[1mGemini Interpreted Journalctl Output:\033[0m\n\n")
        for field, value in ctloutput.items():
            if value:
                if field == "major_errors":
                    print(f"\033[91mMajor errors:\033[0m {value}")
                elif field == "minor_errors":
                    print(f"\033[93mMinor errors:\033[0m {value}")
                elif field == "other_notes":
                    print(f"\033[94mOther things to be aware of:\033[0m {value}")
                elif field == "status":
                    print(f"\033[92mStatus:\033[0m {value}")
            else:
                print(f"\033[90m{field.replace('_', ' ').title()}:\033[0m No information available.")
            print("\n")
        print("\033[1mEnd of Gemini Interpreted Journalctl Output\033[0m\n")

# This script formats the output of GeminiFunctions.JournalctlGeminiJSON() using the 'boxes' command-line tool.      
def format_boxes_ctl_json():
    boxes_path = shutil.which("boxes")
    if not boxes_path:
        print("ERROR: 'boxes' command not found in PATH.")
        return

    ctloutput = GeminiFunctions.JournalctlGeminiJSON()
    if not ctloutput:
        print("No output or status, check prompt.")
        return

    all_boxes = ""
    wrap_width = 150  # typical terminal width for wrapping
    all_boxes +=("\033[1mGemini Interpreted Journalctl Output:\033[0m\n\n")
    for field, value in ctloutput.items():
        if value:
            color = ""
            if field == "major_errors":
                box_type = "critical"
                # No color, no extra linebreak
                title = f"##### {field.replace('_', ' ').title()} #####"
                wrapped_text = title + "\n" + textwrap.fill(str(value), width=wrap_width)
            elif field == "minor_errors":
                box_type = "warning"
                color = "\033[93m"  # Yellow
            elif field == "other_notes":
                box_type = "info"
                color = "\033[96m"  # Cyan
            elif field == "status":
                box_type = "info"
                color = "\033[92m"  # Green
            else:
                box_type = "info"
                color = "\033[0m"   # Default

            if field != "major_errors":
                reset = "\033[0m"
                title = f"{color}{field.replace('_', ' ').title()}{reset}\n"
                wrapped_text = title + "\n" + textwrap.fill(str(value), width=wrap_width)

            try:
                formatted_output = subprocess.run(
                    ["boxes", "-d", box_type, "-p", "h8v1"],
                    input=wrapped_text,
                    text=True,
                    capture_output=True
                )
                all_boxes += formatted_output.stdout + "\n"
            except Exception as e:
                print(f"ERROR running boxes for field '{field}': {e}")
        else:
            all_boxes += f"{field.replace('_', ' ').title()}: No information available.\n\n"

    try:
        final_output = subprocess.run(
            ["boxes", "-d", "ansi-double", "-p", "h8v1"],
            input=all_boxes,
            text=True,
            capture_output=True
        )
        print(final_output.stdout)
    except Exception as e:
        print(f"ERROR running final boxes: {e}")

#if __name__ == "__main__":
    #format_basic_ctl_json()
    #format_boxes_ctl_json()