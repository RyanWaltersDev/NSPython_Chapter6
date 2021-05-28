# RyanWaltersDev May 27 2021 -- Messin' with Nestin'!

# Define dictionaries
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

# Define nested list and print
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Define an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

# Modify first three of the list
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] == 'red'
        alien['speed'] = 'fast'
        alien['points'] ='15'

# Print first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Print length of list
print(f"The total number of aliens: {len(aliens)}.")

# END OF PROGRAM
