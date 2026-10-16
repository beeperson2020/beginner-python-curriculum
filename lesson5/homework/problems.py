# Problem 1
# Search the list and print whether "tiger" is found.
animals = ["cat", "dog", "tiger", "lion"]
for x in animals:
  if x == "tiger":
    print("found tiger")


# Problem 2
# Count how many words have length greater than 5.
words = ["python", "cat", "elephant", "dog", "computer"]
count = 0
for x in words:
  if len(x) > 5:
    print(x)
    count = count  + 1

print (count , "words length > 5.")


# Problem 3
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
s = 0
for x in numbers:
  if x > 25:
    print(x, "bigger than 25")
    s = s + x
print("the sum is" , s)

# Problem 4
# Find and print the biggest number in the list.
Numbers = [12, 7, 33, 5]
h = Numbers[0]
for x in Numbers:
  if x > h:
    h = x 
print( h , "is the biggest number")
  
  


# Problem 5
# Find and print the biggest number less than 100 in the list 
numbers = [104, 99, 86, 120, 101]
h = numbers[1]
for x in numbers:
  if x > h:
    print( h ,"is the biggest number that you asked for")