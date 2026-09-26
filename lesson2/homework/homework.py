# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
number1 = int(input("what is the first number?"))
print("the number is " , number1)
number2 = int(input("what is the second number? "))
print("the number is" , number2)
print("The quotient is ", number1 // number2) 
print( "the remainder is", number1 % number2) 



# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
color = input("what is your favorite color?")
animal = input("what is your favorite animal?")
print("A",  color,  animal, "would be awesome!")

# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for i in range(0,6):
     print(i*2)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
pushups = input("how many push-ups can you do?")
print("i can do" , int(pushups)*7)


# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for i in range(1,7):
    print("square of ", i, "is", i*i) 


