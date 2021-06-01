# RyanWaltersDev May 25 2021 -- TIY 6-1 and TIY 6-6

# Define dictionary
brooke_yost = {
    'first_name': 'brooke', 
    'last_name': 'yost', 
    'age': 23, 
    'location': 'milledgeville',
    'favorite color': 'cranberry',
    'favorite disney movie': 'aladdin',
    'booty': 'unquantifiable',
    }

# Assign variables for each key-value pair
first_name = brooke_yost['first_name'].title()
last_name = brooke_yost['last_name'].title()
age = brooke_yost['age']
location = brooke_yost['location'].title()
favorite_color = brooke_yost['favorite color'].title()
favorite_disney_movie = brooke_yost['favorite disney movie'].title()
booty_variable = brooke_yost['booty'].title()

# Print each value
print(f"Her first name is {first_name}.")
print(f"Her last name is {last_name}.")
print(f"She is {age} years old.")
print(f"She lives in {location}.")
print(f"Her favorite color is {favorite_color}.")
print(f"Her favorite Disney movie is {favorite_disney_movie}.")
print(f"Her booty is {booty_variable}.")
print("She made me say the last one.")

# Define multiple dictionaries TIY 6-7
brooke_yost = {
    'first name': 'brooke', 
    'last name': 'yost', 
    'age': 23,
    'hometown': 'norcross, georgia',
    'current location': 'milledgeville, georgia',
    'favorite color': 'cranberry',
    'favorite movie': 'big fish',
    }

ryan_walters = {
    'first name': 'ryan',
    'last name': 'walters',
    'age': 27,
    'hometown': 'philadelphia, pennsylvania',
    'current location': 'milledgeville, georgia',
    'favorite color': 'black',
    'favorite movie': 'akira',
    }

grey_newell = {
    'first name': 'grey',
    'last name': 'newell',
    'age': 28,
    'hometown': 'ellijay, georgia',
    'current location': 'smyrna, georgia',
    'favorite color': 'blue',
    'favorite movie': 'john wick'
    }

sarah_sorenson = {
    'first name': 'sarah',
    'last name': 'sorenson',
    'age': 29,
    'hometown': 'salt lake city, utah',
    'current location': 'smyrna, georgia',
    'favorite color': 'sparkly, no preference',
    'favorite movie': 'the shining',
    }

# Store dictionaries in list
friends = [brooke_yost, sarah_sorenson, grey_newell, ryan_walters]

# Loop through list
for friend in friends:
    print(f"\nHere's a few things we know about {friend['first name'].title()}.")
    for key, value in friend.items():
        if type(value) == int or type(value) == float:
            print(f"\t{key.title()}: {value}")
        else:
            print(f"\t{key.title()}: {value.title()}")

# END OF PROGRAM
