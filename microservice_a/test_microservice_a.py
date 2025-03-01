import zmq

# Set up environment to create sockets
context = zmq.Context()
print("Client attempting to connect to server...")

# Using request socket
socket = context.socket(zmq.REQ)

# Connect to remote socket
socket.connect("tcp://localhost:5555")

print("Sending a request...")

# Send request to server
socket.send_string("Request random playlist name")

# Receive playlist name from server
playlist_name = socket.recv()

# Print playlist name to terminal
print(f"Server sent back playlist name in adjective + verb form: {playlist_name.decode()}")

socket.send_string("Quit")