# what are variables?
# There are different type of variables
# strings are texts
name = "John" #quotation marks
name2 = "Lucy"
# Integers are whole numbers
num1= "10" # no quotation marks
num2 = 20 
print(int(num1) + num2) # When you have a plus sign 
# Between two variables its called concatenation
# type casting when you convert a variable from one type to another
# print(name +"and"+ name2 + "have" + num1 + str(num2) + "apples")
#  f strings allow us to insert variables into strings
# using f before the string
print(f"{name}  and  {name2}  have  {num1 + str(num2)} apples")

# floats are decimal numbers
dollars = 10.99
# It can be positive or negative
print(f"{name} has {dollars} dollars")
# Booleans are true or false
is_student = True
#  it can be true or false
print(f"{name} is a student: {is_student}")
# lists are collections of values
# dictionaries are collections of key-values pairs
# problem set #1
# create 5 different variables
# print them out
# use f strings to format the strings
name3 = "Emiliano"
name4 = "Benji"
num3 = 500
dollars2 = 49.99
name5 = "Frank"
love_english = False
print(f"{name3} has {num3} mansions")
print(f"{name4} has {dollars2} dollars")
print(f"{name5} loves english: {love_english}")
