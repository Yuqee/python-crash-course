# 5-8. Hello Admin
usernames = ['mike', 'marry', 'joe', 'ann', 'admin']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")