ingredients = ["egg", "flour", "yeast", "salt", "water"]

def egg():
    how_many = input("How many eggs? ")
    in_grams = float(how_many) * 50
##    output = str(in_grams) + " grams of egg."
##    print(output)
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

runtime = 0
for listed in ask:
    if runtime >= 1: break
    if ingredients[0] in ask:
        eggies = egg()
        print("{} grams of egg.".format(eggies))
        pass
    if ingredients[1] in ask:
        flower = flour()
        print("{} grams of flour.".format(flower))
        pass
    if ingredients[2] in ask:
        yeet = yeast()
        print("{} grams of yeast.".format(yeet))
        pass
    if ingredients[3] in ask:
        salty = salt()
        print("{} grams of salt.".format(salty))
        pass
    if ingredients[4] in ask:
        aqua = water()
        print("{} grams of water.".format(aqua))
        pass
    runtime += 1
