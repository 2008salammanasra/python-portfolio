score = 0
Failed_attempts = int(input("failed:")) 
Login_hour = int(input("enter login hour:")) #(0-23)
New_device = input("is the device new")#(yes\no)
if Failed_attempts >= 3:
    score = score + 40
if Login_hour < 6:
    score = score + 30
if New_device == "yes":
    score = score + 30
if score >= 70:
    print(f"Risk score:{score} (HIGH)")
elif score >= 30:
    print(f"Risk score: {score} (MEDIUM)")
else :
    print(f"risk score: {score} (LOW)")
