# 5. Write a script to remove values duplicates from dictionary.
# Feel free to hardcode your dictionary.


from pprint import pprint


my_dict = {
    'Wolwerine': 'adamantium', 'Hawk eye':'bow', 'Spider-man': 'web-shoters',
    'Black-Widow': 'karate','Thor': 'Mjolnir', 'Nick Fury': 'karate',
    'Doomsdey': 'anger','Green Arrow': 'bow', 'Hulk': 'anger'
}
pprint("Dictionary of all superheroes: " + str(my_dict))


temp = []
origin_dict = dict()
for key, val in my_dict.items():
	if val not in temp:
		temp.append(val)
		origin_dict[key] = val


pprint("Dictionary of superheroes with original powers : " + str(origin_dict))
