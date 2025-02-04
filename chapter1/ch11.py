def combine_lists(list1, list2):
    combine_list = list1 + list2
    list_length = len(combine_list)

    for i in range(list_length):
        for j in range(0, list_length - 1):
            if combine_list[j] > combine_list[j+1]:
                temp = combine_list[j]
                combine_list[j] = combine_list[j+1]
                combine_list[j +1] = temp
    return combine_list
