import re

EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'


def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)


def is_valid_email(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None


sample_text = """
You can contact Priya at priya_25@yahoo.com.
For support, email helpdesk@techworld.com.
College queries can be sent to student_07@mit.edu.in.
"""


emails = find_emails(sample_text)

print("Emails found:")
for email in emails:
    print(email)

print("\nTotal emails found:", len(emails))


test_emails = [
    "priya_25@yahoo.com",
    "helpdesk@techworld.com",
    "student_07@mit.edu.in",
    "@missing-local.com",
    "student@.com",
    "student@college"
]

print("\nEmail Validation:")

for email in test_emails:
    if is_valid_email(email):
        print(email, "-> VALID")
    else:
        print(email, "-> INVALID")