def FizzFunc():
    Fizz = 0
    for x in range(99):
        if (x % 3 == 0):
            Fizz = Fizz+1
    print("Fizz"*Fizz)
    return Fizz

def BuzzFunc():
    Buzz = 0
    for x in range(100):
        if(x % 5 == 0):
            Buzz = Buzz + 1
    print("Buzz"*Buzz)
    return Buzz

def FizzBuzzFunc():
    FizzBuzz = 0
    for x in range(90):
        if (x % 15 == 0):
            FizzBuzz = FizzBuzz + 1
    print("FizzBuzz"*FizzBuzz)
    return FizzBuzz