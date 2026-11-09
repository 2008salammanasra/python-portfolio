MIN_LENGTH = 8

def border(width):
    """Prints a border line with dashes based on the text width. """
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Prints the given text inside a bordered box. """
    border(len(text))
    print(f"| {text} |")
    border(len(text))

def show_menu():
    """Displays the security toolkit main menu."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")


def port_range(port):
    """Returns the range classification ategory of agiven port number ."""
    if port < 0 or port > 65535:
        return "invalid"
    elif 0 <= port <= 1023:
        return "system"
    elif 1024 <= port <= 49151:
        return "user"
    else:
        return "dynamic"


def check_port():
    """Prompts for a port number and displays its range type in a box. """
    port = int(input("Port: "))
    range_type = port_range(port)
    show_box(f"Port {port}: {range_type}")


def password_problem(password, username):
    """Evaluates password strength and returns a descriptive problem string if invalid."""
    if len(password) < MIN_LENGTH:
        return "too short (at least 8)"
    if password == username:
        return "same as the username"
    return ""


def check_password():
    """Prompts for username and password then displays verification results."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem:
        show_box(f"Relected: {problem}")
    else:
        show_box("Password accepted")



def days_to_guess(digits, per_second):
    """Calculates the total whole days required to brute_force a PIN ."""
    return int((10**digits) / per_second / 86400)


def chech_pin():
    """Prompts for PIN details and displays the required guessing time."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")



#Main Program Logic
show_menu()
checks_done = 0

while True:
    choice = input("Choice(1, 2, 3, or q): ")
    if choice == "1":
        check_port()
        checks_done += 1
    elif choice =="2":
        check_password()
        checks_done +=1
    elif choice =="3":
        chech_pin()
        checks_done +=1
    elif choice == "q":
        show_box(f"checks done: {checks_done}")
        break
    else:
        print("Unknown choice. It is not counted.")
