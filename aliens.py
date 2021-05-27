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
    new_alien = {'color': 'green', 'points': '5'}
    aliens.append(new_alien)

# Print first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Print length of list
print(f"The total number of aliens: {len(aliens)}.")

# END OF PROGRAM
