# 6-12. Extensions
aliens = []
for alien_number in range(15):
    if alien_number < 6:
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    elif alien_number < 11:
        new_alien = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
    else:
        new_alien = {'color': 'red', 'points': 15, 'speed': 'fast'}
    aliens.append(new_alien)

for alien in aliens:
    print(alien)