'''
Coursera - Algorithms Specialization, Stanford - Programming Assignment - Course 1 Week 2
Serena Rosignoli, 2023

The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order.
The integer in the ithith row of the file gives you the ithith entry of an input array.
Your task is to COMPUTE THE TOTAL NUMBER OF COMPARISONS used to sort the given input file by QuickSort.

As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.
You should not count comparisons one-by-one.
Rather, when there is a recursive call on a subarray of length m, you should simply add m−1 to your running total of comparisons.
(This is because the pivot element is compared to each of the other m−1 elements in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons.  For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).

DIRECTIONS FOR THIS PROBLEM:
For the first part of the programming assignment, you should always use the first element of the array as the pivot element.

HOW TO GIVE US YOUR ANSWER:
Type the numeric answer in the space provided.
So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / other punctuation marks. You have 5 attempts to get the correct answer.
(We do not require you to submit your code, so feel free to use the programming language of your choice, just type the numeric answer in the following space.)
'''

PIVOT_FIRST = 1
PIVOT_FINAL = 2
PIVOT_MEDIAN = 3

comparisons = 0


def swap(ar, i, j):
    t = ar[i]
    ar[i] = ar[j]
    ar[j] = t


def is_median(ar, i, j, k):
    '''
    Determines whether ar[i] is a median
    of ar[i], ar[j] and ar[k].
    '''
    return (ar[i] < ar[j] and ar[i] > ar[k]) or\
           (ar[i] > ar[j] and ar[i] < ar[k])


def _quickSort(ar, l, r, pivot):

    global comparisons

    # Base case
    if l >= r:
        return

    # Picking the pivot element
    p = 0
    if pivot == PIVOT_FIRST:
        p = ar[l]
    elif pivot == PIVOT_FINAL:
        p = ar[r]
        swap(ar, l, r)
    elif pivot == PIVOT_MEDIAN:
        m = l + ((r-l) >> 1)
        if is_median(ar, l, m, r):
            p = ar[l]
        elif is_median(ar, m, l, r):
            p = ar[m]
            swap(ar, l, m)
        else:
            p = ar[r]
            swap(ar, l, r)

    # Updating the comparisons counter
    comparisons += (r-l)

    # Partition (see lectures)
    i = l+1
    for j in range(l+1, r+1):
        if ar[j] < p:
            swap(ar, i, j)
            i += 1
    swap(ar, l, i-1)

    # Recursive calls
    _quickSort(ar, l, i-2, pivot)
    _quickSort(ar, i, r, pivot)



def quickSort(ar, pivot):
    '''
    Sorts the array in place using
    the given pivot picking strategy
    (PIVOT_FIRST/PIVOT_FINAL/PIVOT_MEDIAN).

    Expected running time is O(n*log(n)).
    '''
    _quickSort(ar, 0, len(ar)-1, pivot)



def main():

    global comparisons

    #test
    input_array = [1,3,5,2,4,6]
    quickSort(input_array, PIVOT_FIRST)
    print(input_array)

    # Assignment data
    f = open('QuickSort.txt', 'r')
    lst = []

    # (!) Better approach to reading lines than in PA1
    for line in f.readlines():
        lst.append(int(line))


    # Task 1
    input_array = lst[:] # make a copy
    comparisons = 0
    quickSort(input_array, PIVOT_FIRST)
    print(comparisons)

    # Task 2
    input_array = lst[:] # make a copy
    comparisons = 0
    quickSort(input_array, PIVOT_FINAL)
    print(comparisons)

    # Task 3
    input_array = lst[:] # make a copy
    comparisons = 0
    quickSort(input_array, PIVOT_MEDIAN)
    print(comparisons)


if __name__ == '__main__':
    main()
