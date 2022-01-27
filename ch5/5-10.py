# 5-10. Checking Usernames
current_users = ['mike', 'marry', 'joe', 'ann', 'john', 'carol']
new_users = ['mike', 'peter', 'kim', 'jane', 'Carol']

for i in range(0, len(current_users)):
    current_users[i] = current_users[i].lower()

for new_user in new_users:
    if new_user.lower() in current_users:
        print("You need to enter a new user name!")
    else:
        print(f"This name {new_user} is available.")