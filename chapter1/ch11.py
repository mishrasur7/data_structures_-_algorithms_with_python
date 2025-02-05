
# def combine_lists(list1, list2):
#     combine_list = list1 + list2
#     list_length = len(combine_list)

#     for i in range(list_length):
#         for j in range(0, list_length - 1):
#             if combine_list[j] > combine_list[j+1]:
#                 temp = combine_list[j]
#                 combine_list[j] = combine_list[j+1]
#                 combine_list[j +1] = temp
#     return combine_list

def combine_lists(l1,l2):
    # Initialize variables
    i1 = i2 = 0
    output = []
    # Loop until one of the indices reach the end of its list
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            number = l1[i1]
            i1 += 1
        else:
            number = l2[i2]
            i2 += 1
        output.append(number)
    # Add the remaining of the uncompleted list to the output
    if i1 == len(l1):
        output.extend(l2[i2:])
    else:
        output.extend(l1[i1:])
    # Return the output
    return output
'''
This is a random test class for the built-in __del__ method 

class ClassSchedule:
   def __init__(self, course):
       self.course = course
  
   def __del__(self):
       print('You successfully deleted your schedule')

sched = ClassSchedule('Chemistry')
del sched

'''