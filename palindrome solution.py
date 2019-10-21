# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:37:24 2019

@author: prabh
"""
'''

Write a function that take the string and number k as an input parameters, where string which we can delete 
at most k characters, return True whether you can make a palindrome.
For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
'''


def isKPal(str1, str2, m, n): 
	if not m: return n 

	if not n: return m 

	if str1[m-1] == str2[n-1]: 
		return isKPal(str1, str2, m-1, n-1) 

	res = 1 + min(isKPal(str1, str2, m-1, n),(isKPal(str1, str2, m, n-1))) 
				
	return res 

def isPal(string, k): 
	revStr = string[::-1] 
	l = len(string) 

	return (isKPal(string, revStr, l, l) <= k * 2) 

string = input()
k = int(input())
print("True" if isPal(string, k) else "False") 