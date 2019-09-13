#Special Operator

'''
====>> Identity Operator
=========================
===>> To check the memory loc / id's are same or not

            1. is
                True ===> both id's are same
                False ==> different
            2. is not

                True ==>>  different
                False ==>>  same

'''
a = input("enter any data : ")
b = input("enter same a data : ")
c = a
print " a ==> ",a," id of a ====>> ",id(a)
print " b ==> ",b," id of b ====>> ",id(b)
print " c ==> ",c," id of c ====>> ",id(c)
print  a,"  is  " , b ," ===>> ", a is b
print  a,"  is  " , c ," ===>> ", a is c
print  a,"  is not  " , b ," ===>> ", a is not b
print  a,"  is not  " , c," ===>> ", a is not c

# wap given single character is vowel or not using in operator







