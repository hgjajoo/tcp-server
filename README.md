# TCP Server

### Files

- `server.py`: The server script that listens for client connections.
- `client.py`: The client script that connects to the server.
---

- **Documentation**: [Python Socket Documentation](https://docs.python.org/3/library/socket.html)

---

## How to Run the Project
### Running the Server
1. Open a terminal or command prompt.
2. Navigate to the directory containing `server.py`.
3. Run the server script:
  ``` python server.py ```
   The server will start and listen for incoming connections on `127.0.0.1:8080`.
### Running the Client

1. Open another terminal or command prompt.
2. Navigate to the same directory containing `client.py`.
3. Run the client script:
   ``` python client.py ```
   The client will connect to the server and print a message indicating a successful connection.
---
## Code Explanation
### Server (server.py)
- The server binds to the specified IP address (`127.0.0.1`) and port (`8080`).
- It listens for incoming client connections.
- Upon accepting a connection, it prints the client's address and then closes the connection.
### Client (client.py)
- The client connects to the server using the same IP address and port.
- It prints a message indicating a successful connection.
---

## Notes
- The server is set to listen indefinitely. You may need to manually stop it (e.g., using `Ctrl+C`).
- Uncomment the `time.sleep(5)` line in `server.py` to simulate a delay before closing the connection (useful for testing timeouts).
- I'll be completely honest I didn't know how to do this but I figured out with the help of docs and the internet, tried in python since it felt the easiest but might update this repo with possibly better languages like `Go` in the future.
