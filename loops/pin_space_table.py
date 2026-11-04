#filename: pin_space_table.py
#description: calculates the total combinations and time required to brute_force pin from 4 to 8 digits at 10 guesses per second.
GUESSES_PER_SECOND = 10

for digits in range(4, 9):
    combinations = 10 ** digits

    total_seconds = combinations // GUESSES_PER_SECOND
    minutes = total_seconds // 60
    days = minutes // 1440

    print(f"{digits} digits: {combinations} PINs, {minutes} minutes, {days} days")
    