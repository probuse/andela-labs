# The andela-labs2 repository
    This contains two files the following files.
    
### The car_oop.py
    This contains a class Car with different attributes like:
        * name of car
        * model of car
        * type of car
        * number of wheels that a car has
        * number of doors that a car has
        * speed
    Note that the above attributes may not apply to any car, they are just attributes of a car according to the test case.
    
### The test_car_oop.py
    This is just to test the car_oop.py file so that it does what we want.
    It is implemented using unittest
    
### fizz_buzz.py
    Contains a function fizz_buzz that returns 'Fizz' when the argument which is a number is divisible by 3
    The function returns 'Buzz' if the argument is divisible by 5
    The function returns 'FizzBuzz' if the argument is divisible by both 3 and 5
    When the number(argument) is not divisible by 3 or 5, the number itself is returned.
    
### data_type_lab.py
    Has function called data_type that takes one argument. Compare and return results, based on the argument supplied to the function. Complete the test to produce the perfect function that accounts for all expectations.

    If the argument is a string it returns its length.
    If the argument is None it returns a string 'no value'
    If the argument is a boolean it returns that boolean
    if the argument is an integer it returns a string showing how the integer compares to hundred e.g
        * For 67 as argument it returns 'less than 100' 
        * For 4034 as argument it returns 'more than 100' 
        * If integer is 100 it returns equal to 100
    If the argument is a list it returns the 3rd item of the list or None if 3rd item doesn't exist

