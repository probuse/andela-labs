def fizz_buzz(number):
    if number % 3 == 0:
        response = "Fizz"
        if number % 5 == 0:
            response = "FizzBuzz"
        return response
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    else:
        return number
    
print fizz_buzz(3)
print fizz_buzz(33)
print fizz_buzz(5)
print fizz_buzz(25)
print fizz_buzz(15)
print fizz_buzz(105)
print fizz_buzz(101)
print fizz_buzz(8)

