pets = []

pet = {
    'animal type': 'dog',
    'name': 'ozzy',
    'owner': 'aacatl',
    'weight': 21,
    'eats': 'everything',
}
pets.append(pet)

pet = {
    'animal type': 'hamster',
    'name': 'lucy',
    'owner': 'Q',
    'weight': 2,
    'eats': 'leaves',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'bruce',
    'owner': 'Q',
    'weight': 25,
    'eats': 'shoes',
}
pets.append(pet)
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

