#filename: port_report.py
# description: prompts for a start and end port. loops through the range to classify each port bassed on IANA ranges. and displays the total count.

start_port = int(input("start port: "))
end_port = int(input("end port:"))
ports_checked = 0

for port in range(start_port, end_port + 1):
    if port <= 1023:
        category = "system"
    elif port <= 49151:
        category = "usre"
    else:
        category = "dynamic"

    print(f"{port}: {category}")
    ports_checked += 1
print(f"Port checked: {ports_checked}")
