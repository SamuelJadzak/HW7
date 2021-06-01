def FizzFunc():
    Fizz = 0
    for x in range(99):
        if (x % 3 == 0):
            Fizz = Fizz+1
    print("Fizz"*Fizz)
    return Fizz

