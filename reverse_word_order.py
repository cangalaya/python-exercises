def reverse_string(sentence):
    list_words = sentence.split()
    reverse_list_words = list_words[::-1]   # you can use slices or .reversed() string's metod
    reverse_list_words = [i + " " for i in reverse_list_words]
    reverse_string = "".join(reverse_list_words)[:-1]   # convert string and eliminate the final space
    return reverse_string

def string_input(message):
    string_in = input(message + ": ")
    if string_in.isnumeric():
        raise ValueError("No se permite el ingreso de números.")
    else:
        return string_in

def run():
    sentence = string_input("Digite una frase")
    print("La frase invertida es:", reverse_string(sentence))

if __name__ == "__main__":
    run()