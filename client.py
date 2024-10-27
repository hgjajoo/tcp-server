import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket: # creating a socket object
    client_socket.connect((HOST, PORT)) # connecting to the server
    print(f"Connected to server at {HOST}:{PORT}") # logging the IP address and port
