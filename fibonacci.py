def get_integer(message):
    return int(input(message+ ": "))

def fibonacci(number):
    if number < 3:
        return "fibonacci number invalid"
    list_fibonnaci = [1,1]      # fist list
    while len(list_fibonnaci) < number:
        next_number = list_fibonnaci[len(list_fibonnaci)-2] + list_fibonnaci[len(list_fibonnaci)-1]
        list_fibonnaci.append(next_number)
    return list_fibonnaci

def run():
    number_fibonacci = get_integer("Cuantos número fibonacci desea tener")
    print(fibonacci(number_fibonacci))

if __name__ == "__main__":
    run()