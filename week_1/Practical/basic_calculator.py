"""
Task 4: Revisiting Python Programming
Whether you are a beginner programmer or have been coding for years; you should always
endeavour to improve your technical and problem-solving skills. It is time for you, your
programming partner, and your rubber ducky to get programming!

Problem Statement
Functions are tools for software developers which can be implemented into any software.
Create three functions with different uses.
1. Write a function to square a number.
2. Write a function which checks if any given number is odd or even.
3. Write a function which calculates the average in a list of numbers.

"""


def square_number(num):
    if isinstance(num, int):
        squared = num * num
        return num
    else:
        print('Please enter an interger')


def odd_even(num):
    if isinstance(num, int):
        if (num % 2) == 0:
            print(num, 'is even')
        else:
            print(num, 'is odd')
    else:
        print('Please enter an interger')


def average(list_of_num):
    if isinstance(list_of_num, list):
        are_num = True
        total = 0
        for index in list_of_num:
            total += index
            if not isinstance(index, int):
                are_num = False
        if are_num == True:
            total /= len(list_of_num)
            return total
        else:
            print('Please only use numbers in the list')
    else:
        print('Please enter a list of numbers')
