import random

def first_last_element(list_elements):
    result = []
    result.append(list_elements[0])
    result.append(list_elements[len(list_elements)-1])
    return result

def run():
    a = random.sample(range(10), 10)    # random list generation
    result = first_last_element(a)      # first and last elements
    print("list:", a)
    print("first and last elements:", result)


if __name__ == "__main__":
    run()