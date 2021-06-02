# RyanWaltersDev May 25 2021 -- TIY 6-2

# Define Dictionary
favorite_number = {
    'juan': 55,
    'graham': 69,
    'grey': 8,
    'vivek': 666,
    'will': 7,
    }

# Assign variables
juan_number = favorite_number['juan']
graham_number = favorite_number['graham']
grey_number = favorite_number['grey']
vivek_number = favorite_number['vivek']
will_number = favorite_number['will']

# Print variables
print(f"Juan's favorite number is {juan_number}!")
print(f"Graham's favorite number is {graham_number}!")
print(f"Grey's favorite number is {grey_number}!")
print(f"Vivek's favorite number is {vivek_number}!")
print(f"Will's favorite number is {will_number}!")

# TIY 6-10 modifications
favorite_number = {
    'juan': [55],
    'graham': [69, 420],
    'grey': [8, 99],
    'vivek': [666, 42, 710],
    'will': [7],
    }

for name, numbers in favorite_number.items():
    if len(numbers) == 1:
        print(f"\n{name.title()} has only one favorite number, which is:")
        for number in numbers:
            print(f"\t{number}")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"\t{number}")

# END OF PROGRAM
