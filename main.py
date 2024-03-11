import re

text = "mofroiteiruppe-3933@gmail.com, 2779576, +380975642349, Pinchuk Yelyzaveta Serhiivna"

email_pattern = r"([a-z0-9._%+-]+@[a-z0-9._%+-]+\.[a-z0-9._\-]{3})"
home_phone_pattern = r"(\d{7})"
phone_pattern = r"\+?\d{9,13}"
name_pattern = r"(([A-Z][a-z]{1,19}\s){2}[A-Z][a-z]{1,19})"

email_matches = re.findall(email_pattern, text)
home_phone_matches = re.findall(home_phone_pattern, text)
phone_matches = re.findall(phone_pattern, text)
name_matches = re.findall(name_pattern, text)

print(f"Email addresses: {email_matches}")
print(f"Home phone numbers: {home_phone_matches}")
print(f"Phone numbers: {phone_matches}")
print(f"Name of the client: {name_matches}")
