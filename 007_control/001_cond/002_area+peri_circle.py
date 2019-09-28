# area and perimeter based on radius datatype
rad = input("enter radius in meters : ")
pi = 22.0 /7
if (isinstance(rad,float)):
    area = pi*(rad ** 2)
    print "area of circle : ",area," sq.m"
else:
    peri = 2*pi*rad
    print "perimeter of circle : ",peri," meters"
print"task over"
    
