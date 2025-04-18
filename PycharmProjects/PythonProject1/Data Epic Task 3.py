#Task 1

for i in range(1,16):
   print(i)

   if i%2==0:
       print("Even number: ", i)
   else:
       print("Odd number: ", i)


#Task 2

try:
    First_number = int(input("Enter first number:"))
    Second_number = int(input("Enter second number:"))

    Operator = input("Choose an operator (+, -, *, /):")

    if Operator == "+":
        result = First_number + Second_number
        print(result)
    elif Operator == "-":
        result = First_number - Second_number
        print(result)
    elif Operator == "*":
        result = First_number * Second_number
        print(result)
    elif Operator == "/":
        if Second_number == 0:
            print("Error: ZeroDivisionError")
        else:
            result = First_number/Second_number
            print(result)
    else:
        print("Choose a valid Operator")

except ValueError:
    print("Enter a numeric value")