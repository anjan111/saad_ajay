# server tcp socket
import socket as sk
ser_tcp = sk.socket(sk.AF_INET , sk.SOCK_STREAM)
print "creating server TCP"
ip = sk.gethostname()
port = 5000
print "fixing ip =%s and port :%d"%(ip,port)
ser_tcp.bind((ip,port))
print "mention how many clients we connect"
n = input("enter mo cleints : ")
ser_tcp.listen(n)
print "waiting for connection "
conn, cli_addr = ser_tcp.accept()
print "connection established "
print "waiting for data "
data = conn.recv(1024)
print "data : ",data
print "cleint addr : ",cli_addr
print "closing the server"
ser_tcp.close()
