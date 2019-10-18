# server udp socket
import socket as sk
ser_udp = sk.socket(sk.AF_INET , sk.SOCK_DGRAM)
print "creating server udp"
ip = sk.gethostname()
port = 5000
print "fixing ip =%s and port :%d"%(ip,port)
ser_udp.bind((ip,port))
print "waiting for data "
data,cli_addr = ser_udp.recvfrom(1024)
print "data : ",data
print "cleint addr : ",cli_addr
print "closing the server"
ser_udp.close()
