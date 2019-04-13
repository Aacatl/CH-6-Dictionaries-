#example alien 

aliens = []

for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] == 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:
    print(alien)
print("...")

#Pizza.py return 
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + language.title())

#Dictionary in a dictionary 

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
}

#6-7 People 

ehecatl = {'first_name': 'Ehecatl', 'last_name': 'Campos', 'age':20, 'city': 'Costa Mesa'}

aacatl = {'first_name': 'Aacatl', 'last_name': 'Campos', 'age':20, 'city': 'Costa Mesa'}

manuel = {'first_name': 'Manuel', 'last_name': 'Campos', 'age':59, 'city': 'Costa Mesa'}


people = [aacatl, manuel, ehecatl]

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    print("\nPerson's name is: " + full_name.title() + ".")
    print("Age: " + str(person['age']))
    print("City: " + person['city'].title())


