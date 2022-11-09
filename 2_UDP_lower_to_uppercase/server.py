import socket 

#UDP - User Datagram Protocol

#create a socket
#AF_INET -> IPv4,  #SOCK_DGRAM -> UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 9872))

while True:
    data, addr = server_socket.recvfrom((1024)) # arg buffsize
    data = data.decode('utf-8')
    #lowercase to upper case
    data = data.upper().encode('utf-8')
    server_socket.sendto(data, addr)
    
