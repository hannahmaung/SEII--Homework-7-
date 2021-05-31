
#Fizzbuzz program 

def test(fizzbuzz):

    # if number is a multiple of both 3 and 5, print FizzBuzz
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        return("FizzBuzz")
        
    # if number is a multiple of 3 print Fizz
    elif fizzbuzz % 3 == 0:
        return("Fizz")
        
    # if number is a multiple of 5 print Buzz
    elif fizzbuzz % 5 == 0:
        return("Buzz")

    # else, return fizzbuzz   
    else:
        return(fizzbuzz)
