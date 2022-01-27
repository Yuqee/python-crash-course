# 3-7. Shrinking Guest List

guests = ['Billion', 'Carol', 'Rita']
print(f"{guests[0]}, {guests[1]}, {guests[2]}, I found a larger table!")
guests.insert(0, 'Amy')
guests.insert(2, 'Kerry')
guests.append('Mary')
print(f"Come for dinner, {guests[0]}.")
print(f"Come for dinner, {guests[1]}.")
print(f"Come for dinner, {guests[2]}.")
print(f"Come for dinner, {guests[3]}.")
print(f"Come for dinner, {guests[4]}.")
print(f"Come for dinner, {guests[5]}.")

print("Oops, I can only invite only two people!")

print(f"Sorry, {guests.pop()}, I can't invite you.")
print(f"Sorry, {guests.pop()}, I can't invite you.")
print(f"Sorry, {guests.pop()}, I can't invite you.")
print(f"Sorry, {guests.pop()}, I can't invite you.")

print(f"You are still invited, {guests[0]}.")
print(f"You are still invited, {guests[1]}.")

guests.remove('Amy');
guests.remove('Billion');

print(guests)
