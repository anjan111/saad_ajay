# client udp socket
import socket as sk
cli_udp = sk.socket(sk.AF_INET , sk.SOCK_DGRAM)
print "creating client "
ip = sk.gethostname()
port = 5005
print "fixing ip =%s and port :%d"%(ip,port)
cli_udp.bind((ip,port))
data= input("enter sending data : ")
cli_udp.sendto(data,(ip,5000))
print"data sending"
print "closing the cleint "
               
cli_udp.close()

