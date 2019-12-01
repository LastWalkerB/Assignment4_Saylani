#!/usr/bin/env python
# coding: utf-8

# In[1]:


dict = {'first_name': "Jawad", 'last_name': "Mustafa", 'age': 19, 'city': "Karachi"}
print (dict)
dict['qualification'] = "high academic level"
print ("After Addition")
print (dict)
del dict['qualification']
print ("After Deletion")
print (dict)


# In[2]:


cities = {
    'Karachi': {'country': "Pakistan", 'population': "14.91 million", 'fact': "6th largest populated city in the world"},
    'New York': {'country': "USA", 'population': "8.62 million", 'fact': "First American Chess tournament was held here"},
    'Berlin': {'country': "Germany", 'population': "3.78 million", 'fact': "Most of the cold wars happen in Berlin"}
}
print (cities)


# In[3]:


age = int (input("Enter your age: "))
if (age < 3):
    print ("Tickets are free of cost!")
elif (age >= 3 and age <= 12):
    print ("Ticket price is $10!")
elif (age > 12):
    print ("Ticket price is $15!")


# In[10]:


def favourite_book(Cinderella):
    print (Cinderella)
    return
favourite_book ("Cinderella is one of my favourite books!!!")


# In[17]:


import random
num = random.randrange(1, 30)

guess = int (input("Enter your guess: "))
if (guess == num):
    print ("\nYou guessed it right!!! The number was: ")
    print (num)

elif (guess < num):
    print("Oops...you guessed it wrong")
    print("Hint: Number is greater than your guessed number")
    guess2 = int (input("Try again: "))
    if (guess2 == num):
        print ("\nYes!!! you guessed it right...the number was: ")
        print (num)
    
    elif (guess2 < num):
        print("You guessed it wrong again")
        print("Hint: Number is greater than your guessed number")
        guess3 = int (input("Try again: "))
        if (guess3 != num):
            print("\nYou lost...the number was")
            print (num)
        elif (guess3 == num):
            print("\nYou Won! The number was: ")
            print (num)
    
    elif (guess2 > num):
        print("You guessed it wrong again")
        print("Hint: Number is less than your guessed number")
        guess3 = int (input("Try again: "))
        if (guess3 != num):
            print("\nYou lost...the number was: ")
            print (num)
        elif (guess3 == num):
            print("\nYou Won! The number was: ")
            print (num)

elif (guess > num):
    print("Oops...you guessed it wrong" )
    print("Hint: Number is less than your guessed number")
    guess2 = int (input("Try again: "))
    if (guess2 == num):
        print ("\nYes!!! You guessed it right...the number was: ")
        print(num)
    
    elif (guess2 < num):
        print("You guessed it wrong again")
        print("Hint: Number is greater than your guessed number")
        guess3 = int (input("Try again: "))
        if (guess3 != num):
            print("\nYou lost...the number was: ")
            print(num)
        elif (guess3 == num):
            print("\nYou Won! The number was: ")
            print (num)
    
    elif (guess2 > num):
        print("You guessed it wrong again")
        print("Hint: Number is less than your guessed number")
        guess3 = int (input("Try again: "))
        if (guess3 != num):
            print("\nYou lost...the number was: ")
            print (num)
        elif (guess3 == num):
            print("\nYou Won! The number was: ")
            print(num)
            


# In[ ]:




