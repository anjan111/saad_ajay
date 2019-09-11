# wap read int by raw_input and print datatype , data , memory

# after convert into int then print datatype, data, memory of variable

a = raw_input("enter a  : ")
print "data in a : ",a
print type(a)
print "memory : ",id(a)

print "*****************"
a = int(a)
print "data in a : ",a
print type(a)
print "memory : ",id(a)



