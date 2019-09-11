# string dicing   ----> str_var[start_index : stop_index : step_index]
'''
---> To access the step wise character as a sub string from main string 
---> we can access in between start to stop index with step values
start ----> 0
stop  ----> len
step  ----> 1
'''
var = "python program"
print "data with in var : ",var
print "var[3:8:2]  === >> ", var[3:8:2]  # 'hnp'
print "var[:8:2]  ====>>> ",var[:8:2]    #'pto '
print "var[3::2]  ====>>> ",var[3::2]    #'hnporm'
print "var[::]   ===>>>  ",var[::]     #"python program"
 
