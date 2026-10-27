#access_check.py
#this program verifies user login access and role privileges.
MAX_FAILED = 5
rote = input("enter rote: ")
mfa_passed = input("enter mfa: ")
failed_attempts = int(input("enter failed_attempts: "))
mfa_ok = mfa_passed == "yes"
is_privileged = (rote == "admin") or (rote == "root")
can_log_in =mfa_ok and (failed_attempts < MAX_FAILED)
print(f"MFA OK: {mfa_ok}")
print(f"Privileged role: {is_privileged}")
print(f"Can log in: {can_log_in}")
