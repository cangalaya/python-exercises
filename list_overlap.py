"""
Exercises from: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
"""
import random

def generate_random_list(size_list):
    return [random.randint(1,20) for i in range(size_list)]

def run():
    a = generate_random_list(20)
    b = generate_random_list(25)
    
    c = list(set([i for i in a if i in b]))     # list(set()) remove duplicate items
    print("list a:", a)
    print("list b:", b)
    print("solution:", c)


if __name__ == "__main__":
    run()