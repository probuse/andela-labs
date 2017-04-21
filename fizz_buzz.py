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
