import re

emails = ["navanee@gmail.com", "gokul@gmail.com", "sanjay@yahoo.com", "balaji@hotmail.com", "sakthi@gcom", "mano@yahooom", "keshavgmail.com", "arunho@tmailm"]

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def filter_emails(emails):
    valid_emails = []
    invalid_emails = []

    for email in emails:
        if validate_email(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    return valid_emails, invalid_emails

valid_emails, invalid_emails = filter_emails(emails)

print("Valid email addresses:")
for email in valid_emails:
    print(email)

print("\nInvalid email addresses:")
for email in invalid_emails:
    print(email)
