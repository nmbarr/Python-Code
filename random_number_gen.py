import random

def infinite_seq():
    while True:
        yield random.uniform(0, 100)

# Hello, infinite loop!
for num in infinite_seq():
    print(num)
