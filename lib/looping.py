#!/usr/bin/env python3

def happy_new_year():
    for i in range(10 , -1, -1):
        print  (i)
    if i < 1:
        print ("Happy New Year!")

def square_integers(int_list):
    squared = list()
    for int in int_list:
        sqr = int*int
        squared.append(sqr)
       
    return squared



def fizzbuzz():
    for i in range(1, 101):
      
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")

        elif i % 3 == 0:
            print ("Fizz")

        elif i % 5 == 0:
            print ("Buzz")

        else:
            print (i)


