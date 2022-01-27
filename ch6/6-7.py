# 6-7. People:
user1 = {'first_name': 'Yuqi', 'last_name': 'Liu', 'city': 'Chengdu'}
user2 = {'first_name': 'Kiki', 'last_name': 'Toyota', 'city': 'Tokoy'}
user3 = {'first_name': 'Rose', 'last_name': 'Button', 'city': 'New York'}

people = [user1, user2, user3]

for person in people:
    print("\nuser_info:")
    print(f"\tfirst_name: {person['first_name']}")
    print(f"\tlast_name: {person['last_name']}")
    print(f"\tcity: {person['city']}")