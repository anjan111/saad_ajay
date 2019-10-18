# client tcpsocket
import socket as sk
cli_tcp= sk.socket(sk.AF_INET , sk.SOCK_STREAM)
print "creating client tcp "
ip = sk.gethostname()
port = 5005
print "fixing ip =%s and port :%d"%(ip,port)
cli_tcp.bind((ip,port))
print "sending the connection"
cli_tcp.connect((ip,5000))
print"connection was formed"
data= input("enter sending data : ")
cli_tcp.send(data)
print"data sending"
print "closing the cleint "
               
cli_tcp.close()

