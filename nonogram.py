import numpy as np
import random
import copy
from itertools import groupby
import time

test_arr_0 = [1,2]
test_arr_1 = [2]
test_arr_2 = [1,1]
test_arr_3 = [1,1,1]
test_arr_4 = [3]

test_col_0 = [3]
test_col_1 = [2]
test_col_2 = [2]
test_col_3 = [1,1]
test_col_4 = [1,3]

timeout = time.time() + 20*1

def check_inputs(inputs_arr):
    if np.sum(inputs_arr)+len(inputs_arr)-1<=5:
        return True
    else:
        return False

def desired_length(inputs_arr):
    return (5 - np.sum(inputs_arr))

def generate_random_permutation(inputs_arr):
    if check_inputs(inputs_arr):
        num_of_spaces = desired_length(inputs_arr)
        valid_spacing = False
        while not valid_spacing:
            valid_spacing = True
            inputs_arr_copy = copy.deepcopy(inputs_arr)
            for _ in range(num_of_spaces):
                inputs_arr_copy.insert(random.randint(0, len(inputs_arr)), 0)
            for i in range(len(inputs_arr_copy)-1):
                if inputs_arr_copy[i]>0 and inputs_arr_copy[i+1]>0:
                    valid_spacing = False
        inputs_arr = inputs_arr_copy
        new_arr = []
        for i in inputs_arr:
            if i > 0:
                for j in range(i):
                    new_arr.append(int(1))
            else:
                new_arr.append(0)
        new_arr = np.asarray(new_arr)
    return new_arr

def check_col(input_col, checking_col):
    split_col = ([list(group) for item, group in groupby(checking_col)])
    new_arr = []
    for i in range(len(split_col)):
        if np.sum(split_col[i])>0:
            new_arr.append(np.sum(split_col[i]))
    if input_col==new_arr:
        return 1
    else:
        return 0

def generate_solution():
    old_num_correct = 0
    new_num_correct = 0
    keeps = []
    solution_found = False
    big_array = np.zeros([5,5])
    big_array[0,:]=generate_random_permutation(test_arr_0)
    big_array[1,:]=generate_random_permutation(test_arr_1)
    big_array[2,:]=generate_random_permutation(test_arr_2)
    big_array[3,:]=generate_random_permutation(test_arr_3)
    big_array[4,:]=generate_random_permutation(test_arr_4)

    while True:
        old_num_correct = new_num_correct
        num_cols_correct = 0
        for row in range(5):
            if row not in keeps:
                if row == 0:
                    big_array[0,:]=generate_random_permutation(test_arr_0)
                elif row == 1:
                    big_array[1,:]=generate_random_permutation(test_arr_1)
                elif row == 2:
                    big_array[2,:]=generate_random_permutation(test_arr_2)
                elif row == 3:
                    big_array[3,:]=generate_random_permutation(test_arr_3)
                else:
                    big_array[4,:]=generate_random_permutation(test_arr_4)
        num_cols_correct += check_col(test_col_0,big_array[:,0])
        num_cols_correct += check_col(test_col_1,big_array[:,1])
        num_cols_correct += check_col(test_col_2,big_array[:,2])
        num_cols_correct += check_col(test_col_3,big_array[:,3])
        num_cols_correct += check_col(test_col_4,big_array[:,4])

        if num_cols_correct == 5:
            solution_found = True
            break
        if time.time() > timeout:
            break

        new_num_correct = num_cols_correct

        if new_num_correct>old_num_correct:
            for i in range(new_num_correct-old_num_correct):
                new_random_row_to_keep = random.randint(0,4)
                while new_random_row_to_keep in keeps:
                    new_random_row_to_keep = random.randint(0,4)
                keeps.append(new_random_row_to_keep)

        elif new_num_correct<old_num_correct:
            for i in range(old_num_correct-new_num_correct):
                keeps.pop(random.randrange(len(keeps))) 

    if solution_found:
        print(big_array)
    else:
        print('No solution found')

generate_solution()

#ATTEMPT AT 10X10
# import numpy as np
# import random
# import copy
# from itertools import groupby
# import time

# test_arr_0 = [7]
# test_arr_1 = [7]
# test_arr_2 = [7]
# test_arr_3 = [3]
# test_arr_4 = [4]
# test_arr_5 = [1,1]
# test_arr_6 = [2,1,1,3]
# test_arr_7 = [1,3]
# test_arr_8 = [2,2]
# test_arr_9 = [3,2]

# test_col_0 = [1,1]
# test_col_1 = [2,1]
# test_col_2 = [5]
# test_col_3 = [7,2]
# test_col_4 = [3,2]
# test_col_5 = [3,2,1]
# test_col_6 = [3]
# test_col_7 = [3,3]
# test_col_8 = [3,4]
# test_col_9 = [4]

# timeout = time.time() + 100*1

# def check_inputs(inputs_arr):
#     if np.sum(inputs_arr)+len(inputs_arr)-1<=10:
#         return True
#     else:
#         return False

# def desired_length(inputs_arr):
#     return (10 - np.sum(inputs_arr))

# def generate_random_permutation(inputs_arr):
#     if check_inputs(inputs_arr):
#         num_of_spaces = desired_length(inputs_arr)
#         valid_spacing = False
#         while not valid_spacing:
#             valid_spacing = True
#             inputs_arr_copy = copy.deepcopy(inputs_arr)
#             for _ in range(num_of_spaces):
#                 inputs_arr_copy.insert(random.randint(0, len(inputs_arr)), 0)
#             for i in range(len(inputs_arr_copy)-1):
#                 if inputs_arr_copy[i]>0 and inputs_arr_copy[i+1]>0:
#                     valid_spacing = False
#         inputs_arr = inputs_arr_copy
#         new_arr = []
#         for i in inputs_arr:
#             if i > 0:
#                 for j in range(i):
#                     new_arr.append(int(1))
#             else:
#                 new_arr.append(0)
#         new_arr = np.asarray(new_arr)
#     return new_arr

# def check_col(input_col, checking_col):
#     split_col = ([list(group) for item, group in groupby(checking_col)])
#     new_arr = []
#     for i in range(len(split_col)):
#         if np.sum(split_col[i])>0:
#             new_arr.append(np.sum(split_col[i]))
#     if input_col==new_arr:
#         return 1
#     else:
#         return 0

# def generate_solution():
#     old_num_correct = 0
#     new_num_correct = 0
#     keeps = []
#     solution_found = False
#     big_array = np.zeros([10,10])
#     big_array[0,:]=generate_random_permutation(test_arr_0)
#     big_array[1,:]=generate_random_permutation(test_arr_1)
#     big_array[2,:]=generate_random_permutation(test_arr_2)
#     big_array[3,:]=generate_random_permutation(test_arr_3)
#     big_array[4,:]=generate_random_permutation(test_arr_4)
#     big_array[5,:]=generate_random_permutation(test_arr_0)
#     big_array[6,:]=generate_random_permutation(test_arr_1)
#     big_array[7,:]=generate_random_permutation(test_arr_2)
#     big_array[8,:]=generate_random_permutation(test_arr_3)
#     big_array[9,:]=generate_random_permutation(test_arr_4)

#     while True:
#         old_num_correct = new_num_correct
#         num_cols_correct = 0
#         for row in range(10):
#             if row not in keeps:
#                 if row == 0:
#                     big_array[0,:]=generate_random_permutation(test_arr_0)
#                 elif row == 1:
#                     big_array[1,:]=generate_random_permutation(test_arr_1)
#                 elif row == 2:
#                     big_array[2,:]=generate_random_permutation(test_arr_2)
#                 elif row == 3:
#                     big_array[3,:]=generate_random_permutation(test_arr_3)
#                 elif row == 4:
#                     big_array[4,:]=generate_random_permutation(test_arr_4)
#                 elif row == 5:
#                     big_array[5,:]=generate_random_permutation(test_arr_5)
#                 elif row == 6:
#                     big_array[6,:]=generate_random_permutation(test_arr_6)
#                 elif row == 7:
#                     big_array[7,:]=generate_random_permutation(test_arr_7)
#                 elif row == 8:
#                     big_array[8,:]=generate_random_permutation(test_arr_8)
#                 else:
#                     big_array[9,:]=generate_random_permutation(test_arr_9)

#         num_cols_correct += check_col(test_col_0,big_array[:,0])
#         num_cols_correct += check_col(test_col_1,big_array[:,1])
#         num_cols_correct += check_col(test_col_2,big_array[:,2])
#         num_cols_correct += check_col(test_col_3,big_array[:,3])
#         num_cols_correct += check_col(test_col_4,big_array[:,4])
#         num_cols_correct += check_col(test_col_4,big_array[:,5])
#         num_cols_correct += check_col(test_col_4,big_array[:,6])
#         num_cols_correct += check_col(test_col_4,big_array[:,7])
#         num_cols_correct += check_col(test_col_4,big_array[:,8])
#         num_cols_correct += check_col(test_col_4,big_array[:,9])

#         if num_cols_correct == 10:
#             solution_found = True
#             break
#         if time.time() > timeout:
#             break

#         new_num_correct = num_cols_correct

#         if new_num_correct>old_num_correct:
#             for i in range(new_num_correct-old_num_correct):
#                 new_random_row_to_keep = random.randint(0,9)
#                 while new_random_row_to_keep in keeps:
#                     new_random_row_to_keep = random.randint(0,9)
#                 keeps.append(new_random_row_to_keep)

#         elif new_num_correct<old_num_correct:
#             for i in range(old_num_correct-new_num_correct):
#                 keeps.pop(random.randrange(len(keeps))) 
        
#         print('num correct is', new_num_correct)

#     if solution_found:
#         print(big_array)
#     else:
#         print('No solution found')

# generate_solution()