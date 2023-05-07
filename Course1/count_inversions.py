'''
Coursera - Algorithms Specialization, Stanford - Programming Assignment - Course 1 Week 2
Serena Rosignoli, 2023


The file 'sort_array.txt' contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

 Your task is to compute the number of inversions in the file given, where the ithith row of the file indicates the ithith entry of an array.

  Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising.  Then post your best test cases to the discussion forums to help your fellow students!]
'''

import numpy as np

def merge_and_count(b,c):
    res_arr, inv_count = [], 0
    while len(b) > 0 or len(c) > 0:
        if len(b) > 0 and len(c) > 0:
            if b[0] < c[0]:
                res_arr.append(b[0])
                b = b[1:]
            else:
                res_arr.append(c[0])
                c = c[1:]
                inv_count += len(b)
        elif len(b) > 0:
            res_arr.append(b[0])
            b = b[1:]
        elif len(c) > 0:
            res_arr.append(c[0])
            c = c[1:]

    return res_arr, inv_count

def sort_and_count(a):

    arr_len = len(a)

    # base_case
    if arr_len <= 1:
        return a, 0

    b,x = sort_and_count(a[:int((arr_len/2))])
    c,y = sort_and_count(a[int((arr_len/2)):])
    d,z = merge_and_count(b,c)

    return d, x+y+z

# Make a toy array
toy_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Read file in a 1-D array
with open('array.txt') as file:
    input_array = file.readlines()

array = [int(a.replace("\n", "")) for a in input_array]

# Considering the toy array, which has the largets possible number of inversions. The number of inversions should be (n(n-1)/2).
# If n = 10, n_inversions = 45
print("\nTesting using", toy_array)
print("Expecting:", 45)
print ("Returned:", sort_and_count(toy_array)[1])
