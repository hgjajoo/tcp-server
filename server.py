import socket
# import time       # for line 18

HOST = '127.0.0.1'  
PORT = 8080        

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket object

server_socket.bind((HOST, PORT)) # binding the socket to the IP address and port
print(f"Server listening on {HOST}:{PORT}") # logging the IP address and port

server_socket.listen() # checking for incoming connections

while True:
    client_socket, client_address = server_socket.accept() # accepting the connection
    print(f"Client connected from {client_address[0]}") # logging the IP address of the client

    # time.sleep(5) # can be added to test the timeout

    client_socket.close() # closing the connection
