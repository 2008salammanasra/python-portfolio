#password_check.py
#Functions to validate password length and ensure it differs from username

def long_enough(password, minimum=8):
    """Check if password length is at least the minimum required."""
    if len(password) >= minimum:
        return True
    else:
        return False

def differs_from_username(password, username):
    """Check if password and username are different."""
    if password != username:
        return True
    else:
        return False

def password_ok(password, username):
    """return true only if both validation checks pass."""
    if long_enough(password) and differs_from_username(password, username):
        return True
    else:
        return False

#Main program
if __name__ == "__main__":
   user = input("enter username: ")
   pwd = input("enter password: ")

   if password_ok(pwd, user):
       print("Password accepted.")
   else:
       print("Password rejected.")
       
