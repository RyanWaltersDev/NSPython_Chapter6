# RyanWaltersDev June1 2021 -- TIY 6-8

# Define dictionaries

bonzo = {
    'name': 'bonzo',
    'full name': 'dexter garbonzo yost',
    'animal': 'cat',
    'color': 'orange',
    'age': 1,
    'owner': 'brooke & ryan'
    }

chichi = {
    'name': 'chi chi',
    'full name': 'chihiro',
    'animal': 'cat',
    'color': 'tabby',
    'age': 1,
    'owner': 'brooke & ryan',
    }

biscuit = {
    'name': 'biscuit',
    'full name': 'biscuit',
    'animal': 'dog (jack russell terrier)',
    'color': 'white',
    'age': 10,
    'owner': 'dixon & jules',
    }

danny = {
    'name': 'danny',
    'full name': 'danerys targaryan',
    'animal': 'dog (pitbull)',
    'color': 'gray',
    'age': 7,
    'owner': 'grey & sarah'
    }

auggie = {
    'name': 'auggie',
    'full name': "sir augustine, duke of ponte vedra",
    'animal': 'dog (pug-a-poo)',
    'color': 'black',
    'age': 12,
    'owner': 'dad'
    }

# Store in list
pets = [bonzo, chichi, biscuit, danny, auggie]

# Loop through list
for pet in pets:
    print(f"\nHere is what we know about {pet['name'].title()}.")
    for key, value in pet.items():
        if type(value) == int or type(value) == float:
            print(f"{key.title()}: {value}")
        else:
            print(f"{key.title()}: {value.title()}")

# END OF PROGRAM
