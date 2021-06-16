#!/usr/bin/env python
# coding: utf-8

# ### 1. Take two integer values from the user and print greatest among them.

# In[4]:


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if(a - b > 0):
    print(a, "is greater")
else: 
    print(b, "is greater")


# ### 2. Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.

# In[2]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# ### 3. Create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a consonant.

# In[1]:


l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)
elif l == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("%s is a consonant." % l)


# In[2]:


l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)
elif l == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("%s is a consonant." % l)


# ### 4. A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All three sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third side that is a different length. If all of the sides have different lengths then the triangle is scalene. Write a program that reads the lengths of the three sides of a triangle from the user. Then display a message that states the triangle’s type.

# In[6]:


print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")


# ### 5. Write a program that determines the name of a shape from its number of sides. Read the number of sides from the user and then report the appropriate name as part of a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside of this range is entered then your program should display an appropriate error message.

# In[5]:


a=int(input())
if (a == 3):
    print("Triangle")
elif (a == 4):
    print("Quadrilateral")
elif (a == 5):
    print("Pentagon")
elif( a == 6):
    print("Hexagon")
elif( a == 7):
    print("Heptagon")
elif( a == 8):
    print("octagon")
elif( a == 9):
    print("nonagon")
elif( a == 10):
    print("Decagon")
else:
          print ("Input should be from 3 to 10")


# ### 6. A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. Ask the user for quantity, suppose, one unit will cost 100. Judge and print total cost for user.

# In[17]:


print("Enter Quantity: ")
qty = float(input())

print("Enter Rate: ")
rate = float(input())

if (qty>1000) :
    dis = 10
expense = (qty*rate) - (qty*rate*dis / 100)
print("\nTotal Expenses = Rs. ", expense)


# ### 7. Take input of age of 3 people by user and determine oldest and youngest among them.

# In[18]:


print("Enter first age")
first = input()
print("Enter second age")
second = input()
print("third age")
third = input()

if first >= second and first >= third:
      print("Oldest is",first)
elif second >= first and second >= third:
      print("Oldest is",second)
elif third >= first and third >= second:
      print("Oldest is",third)
else:
  print("All are equal")


# ### 8. A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

# In[1]:


print ("Enter salary")

salary = int(input())

print ("Enter year of service")

yos = int(input())

if yos>5:

  print ("Bonus is",.05*salary)

else:

  print ("No bonus")


# ### 9. Write a program to check if a year is leap year or not. If a year is divisible by 4 then it is leap year but if the year is a century year like 2000, 1900, 2100 then it must be divisible by 400.

# In[20]:


year = int(input("Enter Year: "))

# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# ###  10. Accept d1 and d2 as input. First, check to see that they are in the proper range for dice. If not, print a message. Otherwise, determine the outcome if this is the come out roll. If the sum is 7 or 11, print the winner. If the sum is 2, 3 or 12, print loser. Otherwise print the point.

# In[21]:


import random
# Returns the value of a simulated roll of two dice
def roll_dice():
    input("Press ENTER to roll the dice...")
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a + b

# Plays one round of craps using the given amount as the bet. Returns the
# amount won as a positive number or the amount lost as a negative number.

def play_one_round(bet):
    roll = roll_dice()

    # First phase: 7 or 11 wins, 2, 3, or 12 loses
    if roll == 7 or roll == 11:
        print ("You win!")
        return bet
    elif roll == 2 or roll == 3 or roll == 12:
        print ("Sorry, you lose.")
        return -bet
    else:
        point = roll
        print()
        print ("The point is now", point, ".")

    # Second phase
    roll = roll_dice()
    print ("You rolled ", roll)
    while roll != 7 and roll != point:
        roll = roll_dice()
        print ("You rolled ", roll)

    # after loop, roll is 7 or is equal to point
    if roll == 7:
        print ("Sorry, you lose.")
        return -bet
    else:
        print ("You win!")
        return bet
play_one_round(1)


# ### 11. Write a python program to display the number of days in a month name from the given list of months or month number entered by user.

# In[24]:


print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
    print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 day")
else:
    print("Wrong month name")


# ### 12. Write a Python program to get next day of a given date.

# In[25]:


year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

