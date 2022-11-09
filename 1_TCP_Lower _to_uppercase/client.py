import socket 

#create a client socket
client_socket = socket.socket()

#connect to the the server using connect() - takes a tuple as an argument (ipaddr, port)
client_socket.connect(('localhost', 9872))

#Enter the string that is sent to the server
text = input("Enter the string : ")

#send the text to the server
client_socket.send(bytes(text, 'utf-8'))

#recieve the formatted text from the server
server_data = client_socket.recv(1024).decode()
print(server_data)