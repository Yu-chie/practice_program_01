#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

#Ask the user for 10 input numbers
sum = 0
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    sum += num              #Get the sum
print(sum)                  #Print the sum