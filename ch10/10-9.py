# 10-9. Silent Cats and Dogs
def show_contents(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

show_contents('cats.txt')
show_contents('dogs.txt')