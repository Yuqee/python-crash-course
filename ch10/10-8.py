# 10-8. Cats and Dogs
def show_contents(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} is not found!")
    else:
        print(contents)

show_contents('cats.txt')
show_contents('dogs.txt')