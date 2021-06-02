# RyanWaltersDev Jun 1 2021 -- TIY 6.11

# Define dictionary
cities = {
    'atlanta': {
        'country': 'united states',
        'population': 'approx: 6 million',
        'fun fact': 'the hartsield-jackson airport is the busiest'
            ' in the world.',
        },
    'istanbul': {
        'country': 'turkey',
        'population': 'approx 15 million',
        'fun fact': 'istanbul is the only city on two different continents, '
            'europe and asia.'
        },
    'cairo': {
        'country': 'egypt',
        'population': 'approx 10 million',
        'fun fact': 'cairo is the only city in the world that still has '
            'one of the ancient wonders.'
        },
    }

# For loop to print facts about countries
for city, dictionary in cities.items():
    print(f"\nHere's what we know about {city.title()}.")
    for key, value in dictionary.items():
        print(f"\t{key.title()}: {value.title()}")


# END OF PROGRAM
