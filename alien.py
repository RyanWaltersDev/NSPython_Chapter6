# RyanWaltersDev May 13 2021 -- Simple dictionary example project

# Initial dictionary
alien_0 = {'color': 'green', 'points': 5}

# Print values
print(alien_0['color'].title())
print(alien_0['points'])

# Assign value of points key to variable
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Redefine dictionary and then add new key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Start with empty dictionary
alien_0 = {}

alien_0['color']  = 'green'
alien_0['points'] = 5
print(alien_0)

# Modify value in dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Track position of alien that moves different speeds
alien_0 = {'x_position': 0, 'y_position': 5, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Remove key-value pair
alien_0 = {'color': 'a', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#END OF PROGRAM
