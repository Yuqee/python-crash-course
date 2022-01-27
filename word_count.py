# def word_count(filename):
#     try:
#         with open(filename,encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print("Sorry, there is no such file.")
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file{filename} has about {num_words} words.")

# filename = 'Alice.txt'
# word_count(filename)

def word_count(filename):
    try:
        with open(filename,encoding='ISO-8859-1') as f:
            contents = f.read()
    except FileNotFoundError:
        print("Sorry, there is no such file.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file{filename} has about {num_words} words.")

# filenames = ['Alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
#     word_count(filename)
filename = 'little_women.txt'
word_count(filename)
