user = "analyst"
role = "viewer"
failed = 3
port = 22
print("user == analyst ? i predict true.")
print(user == "analyst")
print("\n failed >= 3 i predict true ")
print(failed >= 3)
print("\n role !='viewer' ? i predict false")
print(role != "viewer")
print("\n5> failed > 2 ? i predict true ")
print(5 > failed > 2)
print("\n role=='viewer'and user!= 'admin' i predict true ")
print(role == "viewer" and user != "admin" )
print("\n not(port != 22) i predict true ")
print(not(port != 22))
print("\n port > 50 or user == 'admin' i predict false ")
print(port >50 or user == "admin" )
print("\n user != 'analyst' or port >=15 ? i pretict true")
print(user != "analyst" or port >=15 )

