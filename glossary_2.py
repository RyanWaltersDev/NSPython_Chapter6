# RyanWaltersDev May 27 2021 -- TIY 6-4 Glossary Upgrade

# Define Dictionary
programming_words = {
    'dictionary': 'a list of key-value pairs',
    'variable': 'contains a value',
    'print()': 'prints your message to the terminal',
    'for loop': 'loops through a list and performs a function for each item',
    '.title()': 'a method that capitalizes the variable when printed',
    '.items()': 'a method that returns a list of key-value pairs as tuples',
    'del': 'deletes an item or variable',
    'list': 'containes items and assigns them a variable',
    'sorted()': 'a fucntion that alphabetizes a list or dictionary',
    'set()': 'creates a set, which is a list that does not contain duplicates',
    }

# For loop to print definitions
for term, definition in programming_words.items():
    print(f"{term}: {definition}.")

# END OF PROGRAM
