#port_classifier.py
#classifies network ports into standard categories and identifies common services like ssh or http.
port = int(input("Enter your port:"))
if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535")
elif 0 <=  port <= 1023:
    print("Range: system")
if port == 22:
    print("Service: ssh")
elif port == 80:
    print("Service: http")
elif port == 443:
    print("Service: https")
elif 1024 <= port <= 49151:
    print("Range: user")
elif 49152 <= port <= 65535:
    print("Range: dynamic or private")
