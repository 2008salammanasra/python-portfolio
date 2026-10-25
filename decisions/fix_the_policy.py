# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

if len(password) < MIN_LENGTH: #syntaxError,missing a colon (:) at the if statement , and send message error
    print("- Too short.")
if password == username: #semanticError, using (elif) chains the username check to the length check, if the password is too short , the program skips checking if it matches the username
    print("- Same as the username.")

if len(password) >= 16: # (lines 13-15 ) semanticError, incorrect order of condition (unreachable code)
    strength = "long"
elif len(password) >= MIN_LENGTH: # any password with a length of 16 or more will trigger the (>= 12) condition first , making the (>= 16) long classification unreachabl.fix: check for (>= 16) first then check for (>= MAX_LEENGTH)
    strength = "acceptable"
else:
    strength = "short"

print(f"Length: {len(password)} ({strength})")#semanticError ,placing the print statement inside the else block means it will only execute when the password is short, leaving valid or long passwords with no output at all
