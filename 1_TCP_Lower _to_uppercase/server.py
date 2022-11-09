import socket 

def lower_to_upper(text):
    return text.upper()

#create a socket
#AF_INET -> IPv4,  #SOCK_STREAM -> TCP 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind a socket with port number - Sending data to a particular port
#Remember not to use a port that is already taken
server_socket.bind(('localhost', 9872))
print("TCP socket created successfully")

#Now listen for incoming connections
server_socket.listen(3)
print("waiting for connections...")

#While loop is used for listening to multiple connections
while True:
    #accept the incoming connection
    #accept() returns two values - connection (new client socket object) and address associated with the object
    #the new client socket object is used to send and receive data
    conn, addr = server_socket.accept()
    client_data = conn.recv(1024).decode() # (recv data from the client - arg bufsize:Int) and decode the recieved data
    text_lowercase = lower_to_upper(client_data)
    
    #send the data back to the client
    conn.send(bytes(text_lowercase, 'utf-8')) # sending byte data encoded as UTF-8
    
    #Close the client connection
    conn.close()
    