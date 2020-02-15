'''
@author: amayamunoz
'''

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by 
calling the function and printing what is returned
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def sub_2(num1, num2):
    difference = num2 - num1
    return difference
difference = sub_2(3,2)
print(difference)


#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def randNum(num1):
    val1 = num1/2
    val2 = val1*77
    val3 = val2+1000
    return val3
val3 = randNum(1)
print(val3)
    
#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def equality (num1,num2):
    if (num1==num2):
        return "true"
    else:
        return "false"
b = equality(100, 60)
print(b)

#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def bigNumber (num1, num2):
    if num1>=num2:
        return num1
    else:
        return num2
result = bigNumber(5,1)
print (result)
    
#5) Define a function that takes in two words and returns a string that contains both words combined.
def twoWords (word_1, word_2):
    return word_1, word_2
both_words = twoWords("bunny", "carrot")
print(both_words)

#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def checkNum (num1, num2, num3):
    if (num1==num2) or (num1==num3):
        return ("true")
    else:
        return ("false")
k = checkNum (1,2,3)
print (k)

#7) Define a function that prints your name.
def myName (name):
    return name
q = myName("quynhAnh")
print (q)

#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def compare_colors(fav, color):
    if (color==fav) :
        print("That's my favorite color")
    else:
        print("Thats not my favorite color, try again")
w = compare_colors("blue","blue")
print(w)
        
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def compare_two_numbers(num1,num2):
    num1=4
    while num1 > 0:
        print(num1)
        num1 -=1

#10) Create your own function that solves any problem you can think of.
def compare_animals(best, animal):
    if (animal==best) :
        print("That's the best")
    else:
        print("That animal is not the best")
u = compare_colors("lions","seals")
print(u)

