# 8-12. Sandwiches
def make_sandwiches(*types):
    print("Making a sandwich of the following type:")
    for ty in types:
        print(ty)

make_sandwiches('pepperoni')
make_sandwiches('mushrooms', 'extra cheese')
make_sandwiches('hot sauce', 'ham', 'smoked turkey', 'apple pie')