#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

#Ask the user for 2 input numbers
print("Please Enter a number")
num1 = int(input("Enter first number: "))           #Even with out the int
num2 = int(input("Enter second number: "))          #Even with out the int

if num1 > num2:                                 #Determine the bigger number
    print("The bigger number is: ", num1)           #Print the bigger number. Even with out words
else:                                               
    print("The bigger number is: ", num2 )          #Print the bigger number. Even with out words