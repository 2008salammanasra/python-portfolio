#filename: pin_tries.py
# وظيفته: التحقق من الرمز السري بحد اقصى 3 محاولات وقفل البطاقة في حال الفشل
MAX_TRIES = 3
CORRECT_PIN = "2580"
tries = 0
while tries < MAX_TRIES:
    user_pin = input("PIN: ")
    tries += 1

    if user_pin == CORRECT_PIN:
        print("Access granted.")
        break
    else:
        tries_left = MAX_TRIES -tries
        print(f"Wrong PIN. Tries left:{tries_left}")

if tries == MAX_TRIES and user_pin != CORRECT_PIN:
    print("Card blocked.")