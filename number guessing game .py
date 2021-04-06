#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random 
import math
ul=int(input("Enter upper limit"))
ll=int(input("Enter lower limit"))
totalchance=round(math.log(ul-ll+1,2))
print("You have only ",totalchance,"chance to play")
x=random.randint(ll,ul)
count=0
while count< totalchance:
    count+=1
    guess=int(input("Guess a number"))
    if guess==x:
        print("Congratulations!,you have guessed the number in ",count,"try")
        break
    elif guess>x:
        print("You guessed too high")
    elif guess<x:
        print("You guessed too small")
if count>=totalchance:
    print("\n The number is ",x)
    print("\t Better Luck Next Time")
        
        


# In[ ]:




