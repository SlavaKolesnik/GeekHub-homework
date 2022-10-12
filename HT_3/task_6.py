#6. Write a script to get the maximum and minimum VALUE in a dictionary.


from pprint import pprint
from termcolor import cprint

super_dict = {
    'Wolwerine': 'adamantium', 'Hawk eye': 'bow', 'Spider-man': 'web-shoters',
        'Black-Widow': 'karate','Thor': 'mjolnir', 'Nick Fury': 'karate',
            'Doomsdey': 'anger','Green Arrow': 'Bow', 'Hulk': 'anger'
}

key_max = max(super_dict.keys(), key=(lambda k: super_dict[k]))
key_min = min(super_dict.keys(), key=(lambda k: super_dict[k]))
res = super_dict


cprint('original dict', color='cyan')
pprint(super_dict)
print('Maximum Value: ', super_dict[key_max])
print('Minimum Value: ', super_dict[key_min])
