number = int(input("Enter a number: "))
def factorial():
    returned = 1
    for i in range(number,1,-1):
        returned *= i
    return returned

print(factorial())