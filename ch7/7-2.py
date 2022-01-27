# 7-2. Restaurant Seating
message = input("How many people are there in your dinner group?")
message = int(message)
if(message > 8):
    print("\nPlease wait for a table.")
else:
    print("\nYour table is ready.")