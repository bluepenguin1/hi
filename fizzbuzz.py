for x in range(101):
    if x % 3 == 0 and x % 5 != 0:
        print('fizz')
    if x % 5 == 0 and x % 3 != 0:
        print('buzz')
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    else:
        print(x)
    