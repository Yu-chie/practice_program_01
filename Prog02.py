#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

#Ask the user for 2 input numbers
print("Please Enter a number")
num1 = int(input("Enter first number: "))           #Even with out the int
num2 = int(input("Enter second number: "))          #Even with out the int

#Determine if the numbers are equal
if num1 == num2:
    print("Equal")                  #Print "Equal" when the numbers are the same.
else:
    print("Not Equal")              #Even with out this