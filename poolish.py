import argparse

# Command line version of breadGram using argparse
# Quickly convert common breadmaking measurements into grams for a uniform recipe by weight.
# Author: Neil Hartsfield

def yeast(args):
    args.in_grams = args.yeast * 3.1
    return args.in_grams

def egg(args):
    args.in_grams = args.egg * 50
    return args.in_grams

def flour(args):
    args.in_grams = args.flour * 136
    return args.in_grams

def salt(args):
    args.in_grams = args.salt * 5.9
    return args.in_grams

def water(args):
    args.in_grams = args.water * 236.58
    return args.in_grams

def main():
    parser = argparse.ArgumentParser(description='Convert common breadmaking measurements into grams.')

    parser.add_argument(
        '-w', '--water', type=float,
        help='amount of water in cups'
        )
    parser.add_argument(
        '-f', '--flour', type=float,
        help='amount of flour in cups'
        )
    parser.add_argument(
        '-y', '--yeast', type=float,
        help='amount of yeast in tsp',
        )
    parser.add_argument(
        '-s', '--salt', type=float,
        help='amount of salt in tsp',
        )
    parser.add_argument(
        '-e', '--egg', type=float,
        help='amount of eggies',
        )
    
    args = parser.parse_args()

    if args.yeast:
        print("{} grams of yeast.".format(yeast(args)))
    if args.egg:
        print("{} grams of egg.".format(egg(args)))
    if args.flour:
        print("{} grams of flour.".format(flour(args)))
    if args.salt:
        print("{} grams of salt.".format(salt(args)))
    if args.water:
        print("{} grams of water.".format(water(args)))

if __name__ == '__main__':
    main()



