PORT_BITS = 16
IPV4_BITS = 32
possible_ports = 2 ** PORT_BITS
highest_port = (2 ** PORT_BITS) - 1
possible_ipv4 = 2 ** IPV4_BITS
print(f"Number of possible ports: {possible_ports}")
print(f"Highest port number: {highest_port}")
print(f"Number of possible IPv4 addreses: {possible_ipv4}")
#RFC 9293: in the tcp header source port and destination port are 16 bits each
#RFC 791: addresses are fixed length of four octets 32 bits
