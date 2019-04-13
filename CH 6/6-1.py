#Dictionaries
#Example
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])

#Modifying Dictionaries Example

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

#Person

Person = {'first_name': 'Ehecatl', 'last_name': 'Campos', 'age':20, 'city': 'Costa Mesa'}
print(Person['first_name'])
print(Person['last_name'])
print(Person['age'])
print(Person['city'])