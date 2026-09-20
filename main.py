# CodeAlpha Internship
# Task 3: Task Automation with Python
# Email Address Extractor

import re


def extract_emails(input_file, output_file):
    """Extract email addresses from a text file and save them."""

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Find email addresses using regular expression
        emails = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            text
        )

        # Remove duplicate email addresses
        emails = list(dict.fromkeys(emails))

        with open(output_file, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")

        print("\nEmail extraction completed successfully!")
        print(f"Total email addresses found: {len(emails)}")
        print(f"Emails saved to: {output_file}")

    except FileNotFoundError:
        print(f"\nError: {input_file} was not found.")

    except Exception as error:
        print(f"\nAn error occurred: {error}")


def main():
    print("=" * 50)
    print("          EMAIL ADDRESS EXTRACTOR")
    print("=" * 50)

    input_file = "input.txt"
    output_file = "emails.txt"

    extract_emails(input_file, output_file)


if __name__ == "__main__":
    main()