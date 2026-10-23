username = input("username: ")
#fix 1:runtime bug -converted input to integer to allow mathematical operations
total_seconds = int(input("session length in seconds: "))
#fix 2: semantic bug - changed / to // to get whole minutes without decimals
minutes = total_seconds // 60
secands = total_seconds % 60
print("=" * 30)
#fix 3: sematic bug - added 'f' before the string to make it proper f-string
print(f"User: {username}")
#fix 4:runtime bug - converted 'minutes' to a string using str() to allow concatenation
print("session:"+ str(minutes)+ "min" + str(secands) + "s")
print("=" *30)
