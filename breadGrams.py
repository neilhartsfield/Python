def egg():
    how_many = input("How many eggs? ")
    in_grams = float(how_many) * 50
    return in_grams

def flour():
    how_many = input("How many cups of flour? ")
    in_grams = float(how_many) * 136
    return in_grams

def salt():
    how_many = input("How many tsp of salt? ")
    in_grams = float(how_many) * 5.9
    return in_grams

def yeast():
    how_many = input("How many tsp of yeast? ")
    in_grams = float(how_many) * 3.1
    return in_grams

def water():
    how_many = input("How many cups of water? ")
    in_grams = float(how_many) * 236.58
    return in_grams


ask = input("Please list all ingredients: ").strip().lower()

# Map the user input strings directly to the functions that should be called
ingredient_map = {'egg': egg, 'flour': flour, 'yeast': yeast, 'salt': salt, 'water': water}
user_ingredients = ask.split()  # give me a list of words


# Iterate over the ingredients the user requested
for ingred in user_ingredients:
    # Use the word to look up in the map the corresponding function, and call it
    in_grams = ingredient_map[ingred]()
    print("{} grams of {}.".format(in_grams, ingred))
