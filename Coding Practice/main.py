# ex1:-from:https://adriann.github.io/programming_problems.html from section list,string
'''
problem statement:-Write a function that takes a number and returns 
a list of its digits.So for 2342 it should return [2,3,4,2]
'''
# def ex1():
#     list1=[]
#     a=input('Enter Number:')
#     len_of_users_input=len(a)
#     for x in range(len_of_users_input):
#         list1.append(int(a[x]))
#     print(list1)
# ex1()
# -------------------------------------------------------------------
# ex2:-same website
'''problem statement:-Write a function that combines two lists by alternatingly taking elements, 
e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].'''
# def ex2():
#     list1=['a','b','c']
#     list2=[1,2,3]
#     list3=[]
#     for x in range(len(list1)):
#         if len(list1)==len(list2):
#             list3.append(list1[x])
#             try:
#                 list3.append(list2[x])
#             except:
#                 pass
#     print(list3)
# ex2() 
# -------------------------------------------------------------------
# ex3:-https://codingbat.com/prob/p138533
'''
problem statement:-Given a string, return a version without the first and last char, 
so "Hello" yields "ell". The string length will be at least 2.'''
# def without_end(str):
#     print (str[1:len(str)-1:])
# without_end('Hello')
# ex4:-https://codingbat.com/prob/p194053
'''
problem statement:-
Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).'''
# def combo_string(a, b):
#     len_=len(a),len(b)
#     if len_[0]>len_[1]:
#         print(b+a+b)
#     elif len_[0]<len_[1]:
#         print(a+b+a)
#     else:
#         print('')
# combo_string('hello','Hello')
