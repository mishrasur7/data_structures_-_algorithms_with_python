def num_collections_sum():
    sum = 0
    while True:
        user_input = input()
        try:
            number = float(user_input)
            if number == 0:
                print(f'The grand total is {sum}')
            sum += number
            print(f'The total is {sum}')
        except ValueError:
            print("That wasn't a number.")


num_collections_sum()