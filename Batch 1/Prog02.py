#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

#Ask the user for 2 input numbers
print("Please Enter a number")
num1 = int(input("Enter first number: "))           #Even with out the int
num2 = int(input("Enter second number: "))          #Even with out the int

if num1 == num2:                #Determine if the numbers are equal
    print("Equal")                  #Print "Equal" when the numbers are the same.
else:                               #Even with out this
    print("Not Equal")