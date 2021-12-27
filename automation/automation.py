import re

def get_info(file_path):
    with open(f'{file_path}') as f:
        file_text = f.read()

    phone_pattern = r"(\d{3}[-]\d{3}[-]\d{4}|\(\d{3}\)\s*\d{3}[-]??\d{4})"
    email_pattern = r"[a-zA-Z0-9\-_\.]+@[a-zA-Z0-9\-_\.]+\.[a-zA-Z]{2,5}"

    phone_results = re.findall(phone_pattern, file_text)
    email_results = re.findall(email_pattern, file_text)

    sorted_phone_results = sorted(list(dict.fromkeys(phone_results)))
    sorted_email_results = sorted(list(dict.fromkeys(email_results)))

    with open('automation/phone_numbers.txt', 'w') as f:
        for number in sorted_phone_results:
            f.write(f"{str(number)}\n")

    with open('automation/emails.txt', 'w') as f:
        for email in sorted_email_results:
            f.write(f"{str(email)}\n")

if __name__ == "__main__":
    get_info('automation/potential-contacts.txt')
