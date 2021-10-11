# excersice from: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random   #random library

def listcomprehensions():
    # general sintaxis = [EXPRESSION  FOR_LOOPS  CONDITIONALS]
    x = [1, 2, 3]
    y = [5, 10, 15]
    
    allproducts = [a*b for a in x for b in y]   # list comprehensions complicated
    customlist = [a*b for a in x for b in y if a*b%2 != 0]  # odd products list
    print(allproducts)
    print(customlist)

def exercise():
    a = random.sample(range(15), 10)     # random list generation, size 10
    b = random.sample(range(15), 15)     # random list generation, size 15
    
    c = list(set([index_a for index_a in a for index_b in b if index_a == index_b]))

    print("list a: ",a)
    print("list b: ",b)
    print("solution: ",c)

def run():
    exercise()
    

if __name__ == "__main__":      #entry point
    run()