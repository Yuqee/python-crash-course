# 6-6. Polling 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

pollers = ['jen', 'annie', 'phil', 'paul', 'edward', 'sam', 'sarah']

for poller in pollers:
    if poller in favorite_languages.keys():
        print(f"{poller.title()}, thank you for you cooperation!")
    else:
        print(f"{poller.title()}, please come to take the poll!")