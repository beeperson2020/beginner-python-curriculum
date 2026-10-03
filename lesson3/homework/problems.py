# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
s1 = int(input ("what is your first score ?"))
s2 = int(input ("what is your second score ?"))
if s1 >= 50 and s2 >= 50 :
    print("You passed both!")
else :
    print("You failed at least one.") 



# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch = input("have you brought lunch? ")
water = input("have you brought water? ")
if  lunch == "yes" and water == "yes":
    print ("you are fully ready!")
elif   lunch == "yes" or water =="yes":
    print("your somewhat ready")
else:
    print("Your not ready, so start packing")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
n = int(input("what is the first number?" ))
if n >= 1 and n <= 10:
    print("in range")
else :
    print ("out of range")


# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
test = int(input("what is your score?"))
if test >= 90 and test <= 100:
    print("you got an A!")
elif test >= 80 and test <= 89:
    print ("you got an B!")
elif test >= 60 and test <= 69:
    print ("you got an D!")
else:
    print("you got an F-!") 


# Problem 9999999999999999999
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is  indivisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair.
n1 = int(input("what is the first number?"))
n2 = int(input("what is the second number?"))
if n1 % 5 == 0 and n2 % 2 != 0:
    print ("intresting pair!")
else:
    print("plain pair!")



























