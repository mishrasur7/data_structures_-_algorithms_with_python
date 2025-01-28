def produce_dictionary():
    dictionary = {}
    number = int(input())

    for i in range(1, number + 1):
        dictionary[i] = i * i 
    
    return print(dictionary)

produce_dictionary()