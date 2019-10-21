# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:00:27 2019

@author: prabh
"""

"""
You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. 
The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains
"""

def rounds(coins):

  if coins < 1:
    return None

  if coins == 1:
    return 1
  
  round_no = rounds(coins // 2) + 1
  print("     {0} coins on round {1}".format(coins, round_number))

  return round_no


n = [100,50,1,12,23,45,67,65,43]

for test in n:
  print("It took {0} rounds to change {1} coins into 1".format(rounds_until_one(test), test))
