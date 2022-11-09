import socket 

#UDP - User Datagram Protocol
#sendto() and recvfrom() are used to send and receive data respectively

#create a socket
#AF_INET -> IPv4,  #SOCK_DGRAM -> UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

text = input("Enter the text: ").encode('utf-8')
client_socket.sendto(text, ('localhost', 9872))

data, addr = client_socket.recvfrom(1024)
data = data.decode('utf-8')
print(data)
