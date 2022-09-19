a = int(input("Put in a number:"))
b = int(input("Put in another number:"))
working = input("How would you like to work the numbers? e.g / to divide and * to multipy")
if working == "+":
    print(a + b)
elif working == "-":
    print(a - b)
elif working == "*":
    print(a * b)
else:
    print(a / b)