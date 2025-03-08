#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

#Ask the user for 10 input numbers
odd_numbers = 0
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    if num % 2 != 0:                            #Determine if odd or even
        odd_numbers += 1
print("Odd numbers: ", odd_numbers)             #Print the number of odd numbers
