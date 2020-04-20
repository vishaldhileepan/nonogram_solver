#BEST ATTEMPT
import numpy as np
import random
import copy
import itertools
import time
import math
from sympy.utilities.iterables import multiset_permutations

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

def generate_all_permutations(inputs_arr):
    if check_inputs(inputs_arr):
        num_of_spaces = desired_length(inputs_arr)
        inputs_arr_copy = copy.deepcopy(inputs_arr)
        for _ in range(num_of_spaces):
            inputs_arr_copy.insert(random.randint(0, len(inputs_arr)), 0)
        all_permutations = list(multiset_permutations(inputs_arr_copy))
        remove_array = []
        for i in range(len(all_permutations)):
            valid_spacing = True
            for j in range(len(all_permutations[i])-1):
                if all_permutations[i][j]>0 and all_permutations[i][j+1]>0:
                    valid_spacing = False
            if not valid_spacing:
                remove_array.append(all_permutations[i])
        for incorrect_permutation in remove_array:
            all_permutations.remove(incorrect_permutation)
        for permutation in range(len(all_permutations)):
            new_arr = []
            for value in range(len(all_permutations[permutation])):
                if all_permutations[permutation][value] > 0:
                    for j in range(all_permutations[permutation][value]):
                        new_arr.append(1)
                else:
                    new_arr.append(0)
            all_permutations[permutation]=new_arr
        return all_permutations

def check_col(input_col, checking_col):
    split_col = ([list(group) for item, group in itertools.groupby(checking_col)])
    new_arr = []
    for i in range(len(split_col)):
        if np.sum(split_col[i])>0:
            new_arr.append(np.sum(split_col[i]))
    if input_col==new_arr:
        return 1
    else:
        return 0

def generate_solution(test_arr_0,test_arr_1,test_arr_2,test_arr_3,test_arr_4,test_col_0,test_col_1,test_col_2,test_col_3,test_col_4):
    new_num_correct = 0
    keeps = []
    solution_found = False
    all_permutations_0 = generate_all_permutations(test_arr_0)
    all_permutations_1 = generate_all_permutations(test_arr_1)
    all_permutations_2 = generate_all_permutations(test_arr_2)
    all_permutations_3 = generate_all_permutations(test_arr_3)
    all_permutations_4 = generate_all_permutations(test_arr_4)
    big_array = np.zeros([5,5])
    big_array[0,:]=generate_random_permutation(test_arr_0)
    big_array[1,:]=generate_random_permutation(test_arr_1)
    big_array[2,:]=generate_random_permutation(test_arr_2)
    big_array[3,:]=generate_random_permutation(test_arr_3)
    big_array[4,:]=generate_random_permutation(test_arr_4)

    while not solution_found:
        cols_correct = 0
        cols_correct += check_col(test_col_0,big_array[:,0])
        cols_correct += check_col(test_col_1,big_array[:,1])
        cols_correct += check_col(test_col_2,big_array[:,2])
        cols_correct += check_col(test_col_3,big_array[:,3])
        cols_correct += check_col(test_col_4,big_array[:,4])
        if cols_correct == 5:
            solution_found = True
            break
        elif time.time() > timeout:
            break
        five_best = []
        num_cols_0 = 0
        best_0 = 0
        num_cols_1 = 0
        best_1 = 0
        num_cols_2 = 0
        best_2 = 0
        num_cols_3 = 0
        best_3 = 0
        num_cols_4 = 0
        best_4 = 0
        for i in range(len(all_permutations_0)):
            num_cols_correct = 0
            big_array_new = copy.deepcopy(big_array)
            big_array_new[0,:]=all_permutations_0[i]
            num_cols_correct += check_col(test_col_0,big_array_new[:,0])
            num_cols_correct += check_col(test_col_1,big_array_new[:,1])
            num_cols_correct += check_col(test_col_2,big_array_new[:,2])
            num_cols_correct += check_col(test_col_3,big_array_new[:,3])
            num_cols_correct += check_col(test_col_4,big_array_new[:,4])
            if num_cols_correct>num_cols_0:
                num_cols_0=num_cols_correct
                best_0 = i
        five_best.append(num_cols_0)
        for i in range(len(all_permutations_1)):
            num_cols_correct = 0
            big_array_new = copy.deepcopy(big_array)
            big_array_new[1,:]=all_permutations_1[i]
            num_cols_correct += check_col(test_col_0,big_array_new[:,0])
            num_cols_correct += check_col(test_col_1,big_array_new[:,1])
            num_cols_correct += check_col(test_col_2,big_array_new[:,2])
            num_cols_correct += check_col(test_col_3,big_array_new[:,3])
            num_cols_correct += check_col(test_col_4,big_array_new[:,4])
            if num_cols_correct>num_cols_1:
                num_cols_1=num_cols_correct
                best_1 = i
        five_best.append(num_cols_1)
        for i in range(len(all_permutations_2)):
            num_cols_correct = 0
            big_array_new = copy.deepcopy(big_array)
            big_array_new[2,:]=all_permutations_2[i]
            num_cols_correct += check_col(test_col_0,big_array_new[:,0])
            num_cols_correct += check_col(test_col_1,big_array_new[:,1])
            num_cols_correct += check_col(test_col_2,big_array_new[:,2])
            num_cols_correct += check_col(test_col_3,big_array_new[:,3])
            num_cols_correct += check_col(test_col_4,big_array_new[:,4])
            if num_cols_correct>num_cols_2:
                num_cols_2=num_cols_correct
                best_2 = i
        five_best.append(num_cols_2)
        for i in range(len(all_permutations_3)):
            num_cols_correct = 0
            big_array_new = copy.deepcopy(big_array)
            big_array_new[3,:]=all_permutations_3[i]
            num_cols_correct += check_col(test_col_0,big_array_new[:,0])
            num_cols_correct += check_col(test_col_1,big_array_new[:,1])
            num_cols_correct += check_col(test_col_2,big_array_new[:,2])
            num_cols_correct += check_col(test_col_3,big_array_new[:,3])
            num_cols_correct += check_col(test_col_4,big_array_new[:,4])
            if num_cols_correct>num_cols_3:
                num_cols_3=num_cols_correct
                best_3 = i
        five_best.append(num_cols_3)
        for i in range(len(all_permutations_4)):
            num_cols_correct = 0
            big_array_new = copy.deepcopy(big_array)
            big_array_new[4,:]=all_permutations_4[i]
            num_cols_correct += check_col(test_col_0,big_array_new[:,0])
            num_cols_correct += check_col(test_col_1,big_array_new[:,1])
            num_cols_correct += check_col(test_col_2,big_array_new[:,2])
            num_cols_correct += check_col(test_col_3,big_array_new[:,3])
            num_cols_correct += check_col(test_col_4,big_array_new[:,4])
            if num_cols_correct>num_cols_4:
                num_cols_4=num_cols_correct
                best_4 = i
        five_best.append(num_cols_4)
        if five_best[1:] == five_best[:-1]:
            big_array[0,:]=generate_random_permutation(test_arr_0)
            big_array[1,:]=generate_random_permutation(test_arr_1)
            big_array[2,:]=generate_random_permutation(test_arr_2)
            big_array[3,:]=generate_random_permutation(test_arr_3)
            big_array[4,:]=generate_random_permutation(test_arr_4)
        else:
            best_move = np.argmax(five_best)
            if best_move == 0:
                big_array[0,:]=all_permutations_0[best_0]
            elif best_move == 1:
                big_array[1,:]=all_permutations_1[best_1]
            elif best_move == 2:
                big_array[2,:]=all_permutations_2[best_2]
            elif best_move == 3:
                big_array[3,:]=all_permutations_3[best_3]
            elif best_move == 4:
                big_array[4,:]=all_permutations_4[best_4]

    if solution_found:
        print(big_array)
    else:
        print('No solution found')

generate_solution([1,2],[2],[1,1],[1,1,1],[3],[3],[2],[2],[1,1],[1,3])
generate_solution([2,2],[1,2],[1,3],[1],[1],[4],[1,1],[1],[3],[3])
generate_solution([2],[3],[2],[1,2],[1,2],[2],[1],[2],[2,2],[2,2])
generate_solution([3],[1],[3],[3],[3],[1],[1],[1,3],[3],[4])
# 
# # import numpy as np
# import random
# import copy
# from itertools import groupby
# import time

# timeout = time.time() + 20*1

# def check_inputs(inputs_arr):
#     if np.sum(inputs_arr)+len(inputs_arr)-1<=5:
#         return True
#     else:
#         return False

# def desired_length(inputs_arr):
#     return (5 - np.sum(inputs_arr))

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

# def generate_solution(test_arr_0,test_arr_1,test_arr_2,test_arr_3,test_arr_4,test_col_0,test_col_1,test_col_2,test_col_3,test_col_4):
#     old_num_correct = 0
#     new_num_correct = 0
#     keeps = []
#     solution_found = False
#     big_array = np.zeros([5,5])
#     big_array[0,:]=generate_random_permutation(test_arr_0)
#     big_array[1,:]=generate_random_permutation(test_arr_1)
#     big_array[2,:]=generate_random_permutation(test_arr_2)
#     big_array[3,:]=generate_random_permutation(test_arr_3)
#     big_array[4,:]=generate_random_permutation(test_arr_4)

#     while True:
#         old_num_correct = new_num_correct
#         num_cols_correct = 0
#         for row in range(5):
#             if row not in keeps:
#                 if row == 0:
#                     big_array[0,:]=generate_random_permutation(test_arr_0)
#                 elif row == 1:
#                     big_array[1,:]=generate_random_permutation(test_arr_1)
#                 elif row == 2:
#                     big_array[2,:]=generate_random_permutation(test_arr_2)
#                 elif row == 3:
#                     big_array[3,:]=generate_random_permutation(test_arr_3)
#                 else:
#                     big_array[4,:]=generate_random_permutation(test_arr_4)
                    
#         num_cols_correct += check_col(test_col_0,big_array[:,0])
#         num_cols_correct += check_col(test_col_1,big_array[:,1])
#         num_cols_correct += check_col(test_col_2,big_array[:,2])
#         num_cols_correct += check_col(test_col_3,big_array[:,3])
#         num_cols_correct += check_col(test_col_4,big_array[:,4])

#         if num_cols_correct == 5:
#             solution_found = True
#             break
#         if time.time() > timeout:
#             break

#         new_num_correct = num_cols_correct

#         if new_num_correct>old_num_correct:
#             for i in range(new_num_correct-old_num_correct):
#                 new_random_row_to_keep = random.randint(0,4)
#                 while new_random_row_to_keep in keeps:
#                     new_random_row_to_keep = random.randint(0,4)
#                 keeps.append(new_random_row_to_keep)

#         elif new_num_correct<old_num_correct:
#             for i in range(old_num_correct-new_num_correct):
#                 keeps.pop(random.randrange(len(keeps))) 

#     if solution_found:
#         print(big_array)
#     else:
#         print('No solution found')

# generate_solution([1,2],[2],[1,1],[1,1,1],[3],[3],[2],[2],[1,1],[1,3])
# generate_solution([2,2],[1,2],[1,3],[1],[1],[4],[1,1],[1],[3],[3])
# generate_solution([2],[3],[2],[1,2],[1,2],[2],[1],[2],[2,2],[2,2])
# generate_solution([3],[1],[3],[3],[3],[1],[1],[1,3],[3],[4])

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

# # ATTEMPT AT 10X10
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
#         return True
#     else:
#         return False

# def generate_solution():
#     old_num_correct = 0
#     new_num_correct = 0
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
#         correct_columns = []
#         num_instances = np.zeros(10)
#         keeps = []

#         if check_col(test_col_0,big_array[:,0]):
#             correct_columns.append(0)
#             num_cols_correct+=1
#         if check_col(test_col_1,big_array[:,1]):
#             correct_columns.append(1)
#             num_cols_correct+=1
#         if check_col(test_col_2,big_array[:,2]):
#             correct_columns.append(2)
#             num_cols_correct+=1
#         if check_col(test_col_3,big_array[:,3]):
#             correct_columns.append(3)
#             num_cols_correct+=1
#         if check_col(test_col_4,big_array[:,4]):
#             correct_columns.append(4)
#             num_cols_correct+=1
#         if check_col(test_col_5,big_array[:,5]):
#             correct_columns.append(5)
#             num_cols_correct+=1
#         if check_col(test_col_6,big_array[:,6]):
#             correct_columns.append(6)
#             num_cols_correct+=1
#         if check_col(test_col_7,big_array[:,7]):
#             correct_columns.append(7)
#             num_cols_correct+=1
#         if check_col(test_col_8,big_array[:,8]):
#             correct_columns.append(8)
#             num_cols_correct+=1
#         if check_col(test_col_9,big_array[:,9]):
#             correct_columns.append(9)
#             num_cols_correct+=1

#         if num_cols_correct == 10:
#             solution_found = True
#             break
#         if time.time() > timeout:
#             break

#         new_num_correct = num_cols_correct

#         for j in range(len(correct_columns)):
#             i = correct_columns[j]
#             if big_array[0,i]==1:
#                 num_instances[0]+=1
#                 if 0 not in keeps:
#                     keeps.append(0)
#             if big_array[1,i]==1:
#                 num_instances[1]+=1
#                 if 1 not in keeps:
#                     keeps.append(1)
#             if big_array[2,i]==1:
#                 num_instances[2]+=1
#                 if 2 not in keeps:
#                     keeps.append(2)
#             if big_array[3,i]==1:
#                 num_instances[3]+=1
#                 if 3 not in keeps:
#                     keeps.append(3)
#             if big_array[4,i]==1:
#                 num_instances[4]+=1
#                 if 4 not in keeps:
#                     keeps.append(4)
#             if big_array[5,i]==1:
#                 num_instances[5]+=1
#                 if 5 not in keeps:
#                     keeps.append(5)
#             if big_array[6,i]==1:
#                 num_instances[6]+=1
#                 if 6 not in keeps:
#                     keeps.append(6)
#             if big_array[7,i]==1:
#                 num_instances[7]+=1
#                 if 7 not in keeps:
#                     keeps.append(7)
#             if big_array[8,i]==1:
#                 num_instances[8]+=1
#                 if 8 not in keeps:
#                     keeps.append(8)
#             if big_array[9,i]==1:
#                 num_instances[9]+=1
#                 if 9 not in keeps:
#                     keeps.append(9)

#         if len(keeps)>=8:
#             keeps=[]
#             for i in range(len(num_instances)):
#                 if num_instances[i]>=4:
#                     keeps.append(i)

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
        
#         print('num correct is', new_num_correct)
#         print('keeping rows', keeps)
#         print('num instances', num_instances)

#     if solution_found:
#         print(big_array)
#     else:
#         print('No solution found')

# generate_solution()

# import numpy as np
# import random
# import copy
# import itertools
# import time
# import math
# from sympy.utilities.iterables import multiset_permutations

# timeout = time.time() + 60*1

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

# def generate_all_permutations(inputs_arr):
#     if check_inputs(inputs_arr):
#         num_of_spaces = desired_length(inputs_arr)
#         inputs_arr_copy = copy.deepcopy(inputs_arr)
#         for _ in range(num_of_spaces):
#             inputs_arr_copy.insert(random.randint(0, len(inputs_arr)), 0)
#         all_permutations = list(multiset_permutations(inputs_arr_copy))
#         remove_array = []
#         for i in range(len(all_permutations)):
#             valid_spacing = True
#             for j in range(len(all_permutations[i])-1):
#                 if all_permutations[i][j]>0 and all_permutations[i][j+1]>0:
#                     valid_spacing = False
#             if not valid_spacing:
#                 remove_array.append(all_permutations[i])
#         for incorrect_permutation in remove_array:
#             all_permutations.remove(incorrect_permutation)
#         for permutation in range(len(all_permutations)):
#             new_arr = []
#             for value in range(len(all_permutations[permutation])):
#                 if all_permutations[permutation][value] > 0:
#                     for j in range(all_permutations[permutation][value]):
#                         new_arr.append(1)
#                 else:
#                     new_arr.append(0)
#             all_permutations[permutation]=new_arr
#         return all_permutations

# def check_col(input_col, checking_col):
#     split_col = ([list(group) for item, group in itertools.groupby(checking_col)])
#     new_arr = []
#     for i in range(len(split_col)):
#         if np.sum(split_col[i])>0:
#             new_arr.append(np.sum(split_col[i]))
#     if input_col==new_arr:
#         return 1
#     else:
#         return 0

# def generate_solution(test_arr_0,test_arr_1,test_arr_2,test_arr_3,test_arr_4,test_arr_5,test_arr_6,test_arr_7,test_arr_8,test_arr_9,test_col_0,test_col_1,test_col_2,test_col_3,test_col_4,test_col_5,test_col_6,test_col_7,test_col_8,test_col_9):
#     test_arr_0 = [7]
#     test_arr_1 = [7]
#     test_arr_2 = [7]
#     test_arr_3 = [3]
#     test_arr_4 = [4]
#     test_arr_5 = [1,1]
#     test_arr_6 = [2,1,1,3]
#     test_arr_7 = [1,3]
#     test_arr_8 = [2,2]
#     test_arr_9 = [3,2]
#     test_col_0 = [1,1]
#     test_col_1 = [2,1]
#     test_col_2 = [5]
#     test_col_3 = [7,2]
#     test_col_4 = [3,2]
#     test_col_5 = [3,2,1]
#     test_col_6 = [3]
#     test_col_7 = [3,3]
#     test_col_8 = [3,4]
#     test_col_9 = [4]
#     new_num_correct = 0
#     keeps = []
#     solution_found = False
#     all_permutations_0 = generate_all_permutations(test_arr_0)
#     all_permutations_1 = generate_all_permutations(test_arr_1)
#     all_permutations_2 = generate_all_permutations(test_arr_2)
#     all_permutations_3 = generate_all_permutations(test_arr_3)
#     all_permutations_4 = generate_all_permutations(test_arr_4)
#     all_permutations_5 = generate_all_permutations(test_arr_5)
#     all_permutations_6 = generate_all_permutations(test_arr_6)
#     all_permutations_7 = generate_all_permutations(test_arr_7)
#     all_permutations_8 = generate_all_permutations(test_arr_8)
#     all_permutations_9 = generate_all_permutations(test_arr_9)
#     big_array = np.zeros([10,10])
#     big_array[0,:]=generate_random_permutation(test_arr_0)
#     big_array[1,:]=generate_random_permutation(test_arr_1)
#     big_array[2,:]=generate_random_permutation(test_arr_2)
#     big_array[3,:]=generate_random_permutation(test_arr_3)
#     big_array[4,:]=generate_random_permutation(test_arr_4)
#     big_array[5,:]=generate_random_permutation(test_arr_5)
#     big_array[6,:]=generate_random_permutation(test_arr_6)
#     big_array[7,:]=generate_random_permutation(test_arr_7)
#     big_array[8,:]=generate_random_permutation(test_arr_8)
#     big_array[9,:]=generate_random_permutation(test_arr_9)
#     old_cols_correct = 0
#     new_cols_correct = 0
#     while not solution_found:
#         old_cols_correct = new_cols_correct
#         print('big array IS', big_array)
#         cols_correct = 0
#         cols_correct += check_col(test_col_0,big_array[:,0])
#         cols_correct += check_col(test_col_1,big_array[:,1])
#         cols_correct += check_col(test_col_2,big_array[:,2])
#         cols_correct += check_col(test_col_3,big_array[:,3])
#         cols_correct += check_col(test_col_4,big_array[:,4])
#         cols_correct += check_col(test_col_5,big_array[:,5])
#         cols_correct += check_col(test_col_6,big_array[:,6])
#         cols_correct += check_col(test_col_7,big_array[:,7])
#         cols_correct += check_col(test_col_8,big_array[:,8])
#         cols_correct += check_col(test_col_9,big_array[:,9])
#         new_cols_correct = cols_correct
#         if cols_correct == 10:
#             solution_found = True
#             break
#         elif time.time() > timeout:
#             break
#         five_best = []
#         num_cols_0 = 0
#         best_0 = 0
#         num_cols_1 = 0
#         best_1 = 0
#         num_cols_2 = 0
#         best_2 = 0
#         num_cols_3 = 0
#         best_3 = 0
#         num_cols_4 = 0
#         best_4 = 0
#         num_cols_5 = 0
#         best_5 = 0
#         num_cols_6 = 0
#         best_6 = 0
#         num_cols_7 = 0
#         best_7 = 0
#         num_cols_8 = 0
#         best_8 = 0
#         num_cols_9 = 0
#         best_9 = 0
#         for i in range(len(all_permutations_0)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[0,:]=all_permutations_0[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_0:
#                 num_cols_0=num_cols_correct
#                 best_0 = i
#         five_best.append(num_cols_0)
#         for i in range(len(all_permutations_1)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[1,:]=all_permutations_1[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_1:
#                 num_cols_1=num_cols_correct
#                 best_1 = i
#         five_best.append(num_cols_1)
#         for i in range(len(all_permutations_2)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[2,:]=all_permutations_2[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_2:
#                 num_cols_2=num_cols_correct
#                 best_2 = i
#         five_best.append(num_cols_2)
#         for i in range(len(all_permutations_3)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[3,:]=all_permutations_3[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_3:
#                 num_cols_3=num_cols_correct
#                 best_3 = i
#         five_best.append(num_cols_3)
#         for i in range(len(all_permutations_4)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[4,:]=all_permutations_4[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_4:
#                 num_cols_4=num_cols_correct
#                 best_4 = i
#         five_best.append(num_cols_4)
#         for i in range(len(all_permutations_5)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[5,:]=all_permutations_5[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_5:
#                 num_cols_5=num_cols_correct
#                 best_5 = i
#         five_best.append(num_cols_5)
#         for i in range(len(all_permutations_6)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[6,:]=all_permutations_6[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_6:
#                 num_cols_6=num_cols_correct
#                 best_6 = i
#         five_best.append(num_cols_6)
#         for i in range(len(all_permutations_7)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[7,:]=all_permutations_7[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_7:
#                 num_cols_7=num_cols_correct
#                 best_7 = i
#         five_best.append(num_cols_7)
#         for i in range(len(all_permutations_8)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[8,:]=all_permutations_8[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_8:
#                 num_cols_8=num_cols_correct
#                 best_8 = i
#         five_best.append(num_cols_8)
#         for i in range(len(all_permutations_9)):
#             num_cols_correct = 0
#             big_array_new = copy.deepcopy(big_array)
#             big_array_new[9,:]=all_permutations_9[i]
#             num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#             num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#             num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#             num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#             num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#             num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#             num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#             num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#             num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#             num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#             if num_cols_correct>num_cols_9:
#                 num_cols_9=num_cols_correct
#                 best_9 = i
#         five_best.append(num_cols_9)
#         if cols_correct >= 8 and new_cols_correct == old_cols_correct:
#             list_of_pairs = list(itertools.combinations(range(10), 2))
#             first_to_swap = None
#             second_to_swap = None
#             first_index = None
#             second_index = None
#             most_cols_correct = 0
#             for i in range(len(list_of_pairs)):
#                 pair_cols_correct = 0
#                 big_array_copy = copy.deepcopy(big_array)
#                 if 0 in list_of_pairs[i]:
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_0)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[0,:]=all_permutations_0[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols = num_cols_correct
#                             index = i
#                     big_array_copy[0,:]=all_permutations_0[index]
#                 if 1 in list_of_pairs[i]:
#                     # big_array_copy[1,:]=generate_random_permutation(test_arr_1)
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_1)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[1,:]=all_permutations_1[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols =num_cols_correct
#                             index = i
#                     big_array_copy[1,:]=all_permutations_1[index]
#                 if 2 in list_of_pairs[i]:
#                     # big_array_copy[2,:]=generate_random_permutation(test_arr_2)
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_2)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[2,:]=all_permutations_2[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols=num_cols_correct
#                             index = i
#                     big_array_copy[2,:]=all_permutations_2[index]
#                 if 3 in list_of_pairs[i]:
#                     # big_array_copy[3,:]=generate_random_permutation(test_arr_3)
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_3)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[3,:]=all_permutations_3[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols=num_cols_correct
#                             index = i
#                     big_array_copy[3,:]=all_permutations_3[index]
#                 if 4 in list_of_pairs[i]:
#                     # big_array_copy[4,:]=generate_random_permutation(test_arr_4)
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_4)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[4,:]=all_permutations_4[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols=num_cols_correct
#                             index = i
#                     big_array_copy[4,:]=all_permutations_4[index]
#                 if 5 in list_of_pairs[i]:
#                     # big_array_copy[5,:]=generate_random_permutation(test_arr_5)
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_5)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[5,:]=all_permutations_5[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols=num_cols_correct
#                             index = i
#                     big_array_copy[5,:]=all_permutations_5[index]
#                 if 6 in list_of_pairs[i]:
#                     # big_array_copy[6,:]=generate_random_permutation(test_arr_6)
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_6)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[6,:]=all_permutations_6[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols=num_cols_correct
#                             index = i
#                     big_array_copy[6,:]=all_permutations_6[index]
#                 if 7 in list_of_pairs[i]:
#                     # big_array_copy[7,:]=generate_random_permutation(test_arr_7)
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_7)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[7,:]=all_permutations_7[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols=num_cols_correct
#                             index = i
#                     big_array_copy[7,:]=all_permutations_7[index]
#                 if 8 in list_of_pairs[i]:
#                     # big_array_copy[8,:]=generate_random_permutation(test_arr_8)
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_8)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[8,:]=all_permutations_8[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols=num_cols_correct
#                             index = i
#                     big_array_copy[8,:]=all_permutations_8[index]
#                 if 9 in list_of_pairs[i]:
#                     # big_array_copy[9,:]=generate_random_permutation(test_arr_9)
#                     num_cols = 0
#                     index = 0
#                     for i in range(len(all_permutations_9)):
#                         num_cols_correct = 0
#                         big_array_new = copy.deepcopy(big_array)
#                         big_array_new[9,:]=all_permutations_9[i]
#                         num_cols_correct += check_col(test_col_0,big_array_new[:,0])
#                         num_cols_correct += check_col(test_col_1,big_array_new[:,1])
#                         num_cols_correct += check_col(test_col_2,big_array_new[:,2])
#                         num_cols_correct += check_col(test_col_3,big_array_new[:,3])
#                         num_cols_correct += check_col(test_col_4,big_array_new[:,4])
#                         num_cols_correct += check_col(test_col_5,big_array_new[:,5])
#                         num_cols_correct += check_col(test_col_6,big_array_new[:,6])
#                         num_cols_correct += check_col(test_col_7,big_array_new[:,7])
#                         num_cols_correct += check_col(test_col_8,big_array_new[:,8])
#                         num_cols_correct += check_col(test_col_9,big_array_new[:,9])
#                         if num_cols_correct>num_cols:
#                             num_cols=num_cols_correct
#                             index = i
#                     big_array_copy[9,:]=all_permutations_9[index]
#                 pair_cols_correct += check_col(test_col_0,big_array_copy[:,0])
#                 pair_cols_correct += check_col(test_col_1,big_array_copy[:,1])
#                 pair_cols_correct += check_col(test_col_2,big_array_copy[:,2])
#                 pair_cols_correct += check_col(test_col_3,big_array_copy[:,3])
#                 pair_cols_correct += check_col(test_col_4,big_array_copy[:,4])
#                 pair_cols_correct += check_col(test_col_5,big_array_copy[:,5])
#                 pair_cols_correct += check_col(test_col_6,big_array_copy[:,6])
#                 pair_cols_correct += check_col(test_col_7,big_array_copy[:,7])
#                 pair_cols_correct += check_col(test_col_8,big_array_copy[:,8])
#                 pair_cols_correct += check_col(test_col_9,big_array_copy[:,9])
#                 if pair_cols_correct > most_cols_correct:
#                     most_cols_correct = pair_cols_correct
#                     first_to_swap = big_array_copy[list_of_pairs[i][0],:]
#                     second_to_swap = big_array_copy[list_of_pairs[i][1],:]
#                     first_index = list_of_pairs[i][0]
#                     second_index = list_of_pairs[i][1]
#             big_array[first_index,:]=first_to_swap
#             big_array[second_index,:]=second_to_swap
#         if five_best[1:] == five_best[:-1]:
#             big_array[0,:]=generate_random_permutation(test_arr_0)
#             big_array[1,:]=generate_random_permutation(test_arr_1)
#             big_array[2,:]=generate_random_permutation(test_arr_2)
#             big_array[3,:]=generate_random_permutation(test_arr_3)
#             big_array[4,:]=generate_random_permutation(test_arr_4)   
#             big_array[5,:]=generate_random_permutation(test_arr_5)
#             big_array[6,:]=generate_random_permutation(test_arr_6)
#             big_array[7,:]=generate_random_permutation(test_arr_7)
#             big_array[8,:]=generate_random_permutation(test_arr_8)
#             big_array[9,:]=generate_random_permutation(test_arr_9)
#         else:
#             best_move = np.argmax(five_best)
#             if best_move == 0:
#                 big_array[0,:]=all_permutations_0[best_0]
#             elif best_move == 1:
#                 big_array[1,:]=all_permutations_1[best_1]
#             elif best_move == 2:
#                 big_array[2,:]=all_permutations_2[best_2]
#             elif best_move == 3:
#                 big_array[3,:]=all_permutations_3[best_3]
#             elif best_move == 4:
#                 big_array[4,:]=all_permutations_4[best_4]
#             elif best_move == 5:
#                 big_array[5,:]=all_permutations_5[best_5]
#             elif best_move == 6:
#                 big_array[6,:]=all_permutations_6[best_6]
#             elif best_move == 7:
#                 big_array[7,:]=all_permutations_7[best_7]
#             elif best_move == 8:
#                 big_array[8,:]=all_permutations_8[best_8]
#             elif best_move == 9:
#                 big_array[9,:]=all_permutations_9[best_9]

#         print('columns  correct are', cols_correct)

#     if solution_found:
#         print(big_array)
#         print('solutions found are', cols_correct)
#     else:
#         print('No solution found')

# generate_solution(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)