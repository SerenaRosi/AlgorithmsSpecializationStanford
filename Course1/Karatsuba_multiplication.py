'''
Coursera - Algorithms Specialization, Stanford - Programming Assignment - Course 1 Week 1
Serena Rosignoli, 2023


In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.
To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers.
You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some small test cases of your own devising.
Then post your best test cases to the discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2.
Does this make your life easier?  Does it depend on which algorithm you're implementing?]

'''

from math import ceil, floor
#math.ceil(x) Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
#math.floor(x) Return the floor of x as a float, the largest integer value less than or equal to x.

def karatsuba(x,y):
    # Base case. Stop recursion if either one of the input is a single-digit value
    if x < 10 and y < 10:
        return x*y

    # Get the input with highest length
    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)

    # Extract the first 'm' digits from x. A beautiful example of how to exploit built-in Python functions for second-scopes.
    # The input x is divided by 10**m, returning a float, the floor function only gets the smallest integer value.
    # e.g. x= 1234, m=2, 1234/100 = 12.34, floor(12.34) = 12
    a  = floor(x / 10**m)
    c = floor(y / 10**m)

    # Extract the second 'm' digits from x. A beautiful example of how to exploit built-in Python functions for second-scopes.
    # The input x is divided by 10**m, returning a float, the modulus (%) function returns the remainder of dividing x by 10**m
    # e.g. x= 1234, m=2, 1234/100 = 12.34, 1234 % 100 = 34
    b = x % (10**m)
    d = y % (10**m)

    #recursive steps
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d) - ac - bd

    return int(ac*(10**(m*2)) + abcd*(10**m) + bd)

# Check if the algorithm is well implemented by using the assert funcion of Python.
# If the condition returns False, AssertionError is raised
a, b = 15, 23
assert karatsuba(a, b) == a * b
c, d = 12052, 12
assert karatsuba(c, d) == c * d

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(karatsuba(x, y))
