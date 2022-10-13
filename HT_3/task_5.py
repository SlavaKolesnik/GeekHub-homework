# 5. Write a script to remove values duplicates from dictionary.
# Feel free to hardcode your dictionary.


from pprint import pprint


my_dict = {
    'Wolwerine': 'adamantium',
    'Hawk eye':'bow',
    'Spider-man': 'web-shoters',
    'Black-Widow': 'karate',
    'Thor': 'Mjolnir',
    'Nick Fury': 'karate',
    'Doomsdey': 'anger',
    'Green Arrow': 'bow',
    'Hulk': 'anger'
}


new_dict = {value: key for key, value in my_dict.items()}
reverse_dict = dict(zip(new_dict.values(), new_dict.keys()))


pprint("Dictionary of all superheroes: " + str(my_dict))
pprint("Dictionary of superheroes with original powers : " + str(reverse_dict))
