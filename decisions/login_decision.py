#login_decision.py
#simulates auser login system with account lockout and credential validation.
MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"
Username = input("Enter your username:")
Failed_attempts = int(input("enter failed attempts:"))
Password = input("Enter your password:")
if Failed_attempts >= MAX_FAILED:
    print("Account locked.")
elif Username != KNOWN_USER:
    print("unknown user.")
elif Password != STORED_PASSWORD:
    print(f"Access denied. Attempts left: {MAX_FAILED-Failed_attempts-1}")
else:
    print("Access granted")
