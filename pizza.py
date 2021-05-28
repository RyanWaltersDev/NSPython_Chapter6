# RyanWaltersDev May 28 2021 -- List within a dictionary

# Store information about pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['spinach', 'tomato', 'extra cheese',]
    }

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following "
    "toppings:")
for topping in pizza['toppings']:
    print("\t" + topping.title())

# END OF PROGRAM
