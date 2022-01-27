# 10-10. Common Words
with open('Alice.txt') as f:
    contents = f.read()

num = contents.lower().count("the")
print(num)

num = contents.lower().count("the ")
print(num)