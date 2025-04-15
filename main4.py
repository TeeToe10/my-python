# if conditionals 
# If statements are used to check if a condition is true or false
# if condition is true, do something
# if condition is false, do something else

# if conditional statememts always start with if
# and depend on a boolean value {true or false}
# example
classStarted = True #Boolean Variable
if classStarted:
    print("Class has started")
else:
    print("Class has not started")
# logical and comparison operators
#== equal to
# != not equal to
# > greater than 
# < Less than
# >= greater than or equal to
# <= less than or equal to
# and logical operators
# or logical operators
# not logical operators
# example
age = 18
if age >= 18:
    print("you are an adult")
elif age == 17:
    print("you are almost an adult")
else:
    print("you are a minor")

number = int(input("What is your number?"))
if number % 2 ==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")