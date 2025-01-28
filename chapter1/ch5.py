def count_vowels():
    string_input = input()
    count = 0
    for i in string_input.lower():
        if i == 'a':
            count += 1
        elif i == 'e':
            count += 1
        elif i == 'i':
            count += 1
        elif i == 'o':
            count += 1
        elif i == 'u':
            count += 1
    return(print(f'Number of vowels: {count}'))

count_vowels()