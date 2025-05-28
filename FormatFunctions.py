import GeminiFunctions

#This scripts takes all jsons and colors the titles according to severity, then prints.
def format_basic_ctl_json():
    ctloutput = GeminiFunctions.JournalctlGeminiJSON()
    if not ctloutput:
        print ("No output or status, check prompt.")
    else:
        # Print each field with appropriate formatting
        print("\033[1mGemini Interpreted Journalctl Output:\033[0m\n")
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
if __name__ == "__main__":
    format_basic_ctl_json()