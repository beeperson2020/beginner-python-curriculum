import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
list1 = ["Apple" , "Microsoft" , "chrome"]
print(list1[2])


# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
list = ["writing" , "art" , "math" , "science"]
print(list[1])

list.sort()
print(list)


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.

error_code = ["401" , "405" , "410" , "423" , "498"]
print(len(error_code))
for x in error_code:
  print(x)



# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
programming_language = ["java" , "c++"]
print(programming_language[1])
programming_language.append("typescript")
print(programming_language)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["confused bob" , "annoying meadow" , "stinky sock" , "frying pan" , "duty5645plip" , "kcuof123242pipe"]
mid = (len(passwords)//2)
print(passwords[mid])
passwords.pop(0)
print(passwords)