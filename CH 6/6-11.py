cities = {
    'costa mesa' = ['country': 'united states of america', 'population': '113,825' , 'fact': 'it is boring'],
    'morelia' = ['country': 'mexico', 'population': '597,511' , 'fact': 'i own 17 houses there'],
    'hong kong' = ['country': 'china', 'population': '7.392 million', 'fact': 'has a bunch of skyscrapers']
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

print("\n" + city.title() + " is in " + country + ".")
print("  It has a population of about " + str(population) + ".")
print("  The " + mountains + " mountains are nearby.")