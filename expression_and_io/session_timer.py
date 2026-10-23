total_seconds = int(input("Session length in seconds:"))
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"Session Iength: {minutes} miuntes and {seconds} seconds")
#test with 950 -> session length: 15 miuntes and 5 secands
#test with 60 -> seeion length: 1 miuntes and 0 seconds
#test with 59-> session length: 0 miuntes and 59 seconds
