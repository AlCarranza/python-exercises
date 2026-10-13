import re

def main():
    code = input("Enter the hexadecimal color: ")

    pattern = r"^#[a-bA-B0-9]{6}$"
    match = re.search(pattern, code)

    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid")

main()