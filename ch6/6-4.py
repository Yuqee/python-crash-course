# 6-4. Glossary 2
glossary = {
    'list': 'A list is a collection of items in a particular order.',
    'dictionary': 'A dictionary can store an almost limitless amount of inform'\
    'ation.',
    'set': 'A set is a collection in which each item must be uique.',
    'string': 'A string is a series of characters.',
    'else': 'The else block is a catch all bolck.',
    'colormap': 'A colormap is a series of colors in a gradient that moves fro'\
    'm a starting to an ending color.'
    }

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")