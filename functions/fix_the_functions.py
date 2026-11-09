#1. runtime: removed print_header() call from here and moved it to the bottom because the function was not defined yet.
def print_header():
    """Display the report header."""
    print("=" * 30) 
    print("LOGIN REPORT")
    print("=" * 30) 

def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        total = failed * minutes
        #semantic: added return total here so the function returns the calculated value instead of always returning 0.
        return total
    return 0 

def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


#==================== Main Program Execution ====================

#calling the header function after it has been defined 
print_header()

#runtime: changed keyword argument from user to username to match the parameter name defined in login_line.
print(login_line(username="sara", failed=4))

#semantic: wrapped the function call inside a print() function so that omars data is actually displayed in the output.
print(login_line("omar", 1 ))