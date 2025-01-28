# method 1 
def sort_characters():
    string_input = input()
    input_list = list(string_input)

    for i in range(len(input_list)):
        for j in range(0, len(input_list) - i - 1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return print(''.join(input_list))

sort_characters()

# method 2

def sort_character():
    string_input = input()
    return print(''.join(sorted(string_input)))

sort_character()


