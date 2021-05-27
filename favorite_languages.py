# RyanWaltersDev 05 25 2021 Dictionary example project

# Define dictionary favorite_languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

# Assign key-value pairs to new variable
jen_language = favorite_languages['jen'].title()
sarah_language = favorite_languages['sarah'].title()
edward_language = favorite_languages['edward'].title()
phil_language = favorite_languages['phil'].title()

# Print variables
print(f"Jen's favorite language is {jen_language}!")
print(f"Sarah's favorite language is {sarah_language}!")
print(f"Edward's favorite language is {edward_language}!")
print(f"Phil's favorite language is {phil_language}!")

# Use for loop to complete same task
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# Use for loop for keys only
for name in favorite_languages.keys():
    print(f"{name.title()}")

# Print message for keys in a list
friends = ['sarah', 'phil']
for name in favorite_languages.keys():
    print(f"{name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tOh hey {name.title()}! I see you love {language}!")

# Check for key in list
if 'bob' not in favorite_languages.keys():
    print("Bob, please take our poll!")

# Sort keys alphabetically
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll!")

# Pull values only and print
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Pull and print values no duplicate
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# List for poll TIY 6-6
poll_names = ['michael', 'sarah', 'jebidiah', 'phil', 'bob', 'jen', 'brookie']
for name in poll_names:
    if name not in favorite_languages.keys():
        print(f"{name.title()}, will you please take a moment for our poll?")
    else:
        print(f"Thank you {name.title()}! We have your poll answer.")

# END OF PROGRAM
