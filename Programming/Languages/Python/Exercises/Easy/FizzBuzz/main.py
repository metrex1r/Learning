#write a program that write fizz for every number that is a multiplication
#of three and write buzz for every multiplication of five
#write fizzbuzz if it's a multiplication of both

number = range(1, 51)
for i in number:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
