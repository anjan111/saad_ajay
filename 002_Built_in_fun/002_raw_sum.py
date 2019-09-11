# wap sum of 2 numbers using raw_input functions
'''
Datatype conversion function

str int ---> int( raw_input())----> int
str float ---> float() ----------> float
str complex ---> complex() -------> complex
str bool    ---> bool() ----------> bool
str str    ---> str()   ---------> str
str list    --> list()  ----------? list
str tuple   ---> tuple() ---------> tuple
str set    ----> set()   ---------> set
str dict  -----> dict()  --------> dict

'''

a = raw_input("enter int : ") # str
b = raw_input("enter int : ") # str
c = a+b # 
print c

print "****************************"
a = int(raw_input("enter int : "))# int
b = int(raw_input("enter int : "))# int
c = a+b # 
print c

