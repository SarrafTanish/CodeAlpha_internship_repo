
import re
import sys
import os

# Regex pattern that matches most standard email address formats
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")


def extract_emails(input_file: str, output_file: str) -> None:
    if not os.path.isfile(input_file):
        print(f"Error: input file does not exist -> {input_file}")
        return

    # 1. Read the whole text file
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    # 2. Find every email-shaped substring
    found_emails = EMAIL_PATTERN.findall(text)

    # 3. Remove duplicates while keeping the original order
    unique_emails = list(dict.fromkeys(found_emails))

    # 4. Write the results to the output file, one email per line
    with open(output_file, "w", encoding="utf-8") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"Found {len(found_emails)} email(s), {len(unique_emails)} unique.")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        in_file, out_file = sys.argv[1], sys.argv[2]
    else:
        in_file = input("Enter path to input .txt file: ").strip()
        out_file = input("Enter path for output .txt file: ").strip()

    extract_emails(in_file, out_file)
