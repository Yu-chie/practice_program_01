#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

#Ask the user for 2 input numbers
print("Please Enter a number")
num1 = int(input("Enter base number: "))
num2 = int(input("Enter exponent: "))

result = num1 ** num2                   #Raise the First number with the second
print("The result is: ", result)        #Print the result. Even with out words