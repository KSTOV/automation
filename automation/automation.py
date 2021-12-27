import re

def get_info(file_path):
    with open(f'{file_path}') as f:
        file_text = f.read()

    phone_pattern = r"\d{3}-\d{3}-\d{4}"
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    results = re.findall(pattern, file_text)

    print(results)

if __name__ == "__main__":
    get_info('./potential-contacts.txt')
