import re

password = input("Enter your password: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[!@#$%^&*]", password)):

    print("Valid Password")
else:
    print("Invalid Password")
    print("Password must contain:")
    print("1. At least 8 characters")
    print("2. One uppercase letter")
    print("3. One digit")
    print("4. One special character")