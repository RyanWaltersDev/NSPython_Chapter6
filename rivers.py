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

# Define dictionary TIY 6-12 adding more key values
rivers = {
    'chattahoochee': {
        'country': 'united states',
        'length': '430 miles',
        'source': 'blue ridge mountains',
        'mouth': ['flint river', 'apalachicola river'],
        },
    'mississippi': {
        'country': 'united states',
        'length': '2,318 miles',
        'source': 'lake itasca',
        'mouth': 'gulf of mexico',
        },
    'amazon': {
        'country': ['brazil', 'peru', 'colombia'],
        'length': '3,977 miles',
        'source': 'mantaro river',
        'mouth': 'atlantic ocean',
        },
    'nile': {
        'country': ['egypt', 'sudan'],
        'length': '4,132 miles',
        'source': ['blue nile river', 'white nile', 'atbarah'],
        'mouth': 'mediterranean sea',
        },
    'yangtze': {
        'country': 'china',
        'length': '3,915 miles',
        'source': 'qinghai',
        'mouth': 'east china sea',
        },
    'irtysh': {
        'country': ['russia', 'kazakhstan', 'china'],
        'length': '2,640 miles',
        'source': 'altai mountains',
        'mouth': 'ob river',
        },
    }

# Append empty list with keys and print
river_list = []
for river in rivers.keys():
    river = river.title()
    river_list.append(river)
print(f"\nToday, you will be learning about the", ", " .join(river_list[0:-1])
    + f", and {river_list[-1]} Rivers.")
print("Let's take a closer look!")

# For loop code block to print values in nested dictionary
for river, dictionary in rivers.items():
    print(f"\nBasic facts about the {river.title()} River.")
    for key, value in dictionary.items():
        if type(value) is list:
            value = [item.title() for item in value]
            print(f"\t{key.title()}:", ", " .join(value[0:-1]) 
                + f", and {value[-1]}")
        else:   
            print(f"\t{key.title()}: {value.title()}")

# END OF PROGRAM
