#wap find the salary based on exp

exp = input("enter no of years of exp : ")
if( exp >=0):
    if( exp >=0 and exp <=2):
        print "salary  2.4 lac PA "
    elif( exp > 2 and exp <= 4):
        print "salary  4.8 lac PA "
    elif(exp > 4 and exp <= 6):
        print "salary  8.0 lac PA "
    elif(exp > 6 and exp <= 10):
        print "salary  14.0 lac PA "
    elif(exp > 10 and exp <= 14):
        print "salary  25 lac PA "
    elif(exp > 14 and exp <= 20):
        print "salary  50 lac PA "
    else:
        print "salary 1.0 cr PA"
else:
    print" enter proper exp "



