MAX_LOGIN_ATTEMPTS = 5
username = input("username: ")
failed_attempts =int(input("failed attempts: "))
attempts_left = MAX_LOGIN_ATTEMPTS - failed_attempts
line = "="*30
print(line)
print("LOGIN REPORT")
print(line)
print(f"User:\t\t{username}")
print(f"Failed\t\t{failed_attempts}")
print(f"Attempts Left:\t\t{attempts_left}")