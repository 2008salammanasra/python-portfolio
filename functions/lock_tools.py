#File name:lock_tools.py
#purpose: core functions for manging lock status and login attempts counter.

def is_locked(failed, max_tries=3):
    """ check if failed attempts reached max_tries."""
    if failed >= max_tries:
        return True
    else:
        return False

def tries_left(failed, max_tries=3):
    """Return remaining tries or 0 if locked."""
    if is_locked(failed, max_tries):
        return 0
    else:
        return max_tries - failed

def status(failed):
    """Return 'locked' or active status string."""
    if is_locked(failed):
        return "locked"
    else:
        left = tries_left(failed)
        return f"active ({left} tries left)"

#last 7 lines 
print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))