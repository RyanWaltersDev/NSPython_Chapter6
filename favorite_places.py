# RyanWaltersDev Jun 1 2021 -- TIY 6-9

# Define dictionary
favorite_places = {
    'brooke': ['chatahootchee river', 'houstons', 'disney cruise'],
    'ryan': ['st. augustine', 'the tabernacle'],
    'grey': ['berlin'],
    }

# For loop dictionary
for name, locations in favorite_places.items():
    if len(locations) == 1:
        print(f"\n{name.title()}'s favorite place is:")
        for location in locations:
            print(f"\t{location.title()}")
    else:
        print(f"\nA few of {name.title()}'s favorite places are:")
        for location in locations:
            print(f"\t{location.title()}")

# END OF PROGRAM
