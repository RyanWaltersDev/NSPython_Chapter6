# RyanWaltersDev May 27 2021 -- TIY 6-5

# Define dictionary
rivers = {
    'chattahoochee': 'united states',
    'amazon': 'brazil',
    'nile': 'egypt',
    }

# For loop to print rivers
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Rivers(keys) only
for river in rivers.keys():
    print(f"{river.title()}")

# Countries(values) only
for country in rivers.values():
    print(f"{country.title()}")

# END OF PROGRAM
