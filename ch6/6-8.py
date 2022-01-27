# 6-8. Pets
pet1 = {'kind': 'cat', 'owner': 'Helen Brown'}
pet2 = {'kind': 'dog', 'owner': 'Peter Parka'}
pet3 = {'kind': 'snake', 'owner': 'Susan Pinkman'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\npet_info:")
    print(f"\tkind: {pet['kind']}")
    print(f"\towner: {pet['owner']}")