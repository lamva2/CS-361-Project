import time
import zmq
import random

# Set up environment to create sockets
context = zmq.Context()
# Using a reply socket
socket = context.socket(zmq.REP)
# Network port socket listens to
socket.bind("tcp://*:5555")

# Loop to listen until message received from client
while True:
    # Receive message from client (blank until message arrives)
    message = socket.recv()
    print(f"Received request from the client: {message.decode()}")
    
    if len(message) > 0:
        if message.decode() == "Request random playlist name":
            # Generate random index number for adjectives
            rand_num_1 = random.randint(0, 99)
            # Generate random index number for verbs
            rand_num_2 = random.randint(0, 99)
            
            # Read into adjectives file and create list of adjectives 
            with open('adjectives.txt', 'r') as adjective_file:
                adjectives = adjective_file.read().strip().split(', ')
            
            # Read into verbs file and create list of verbs
            with open('verbs.txt', 'r') as verb_file:
                verbs = verb_file.read().strip().split(', ')
            
            time.sleep(3)
            
            # Concatenate randomly selected adjective and verb to make playlist name
            playlist_name = adjectives[rand_num_1] + " " + verbs[rand_num_2]
            
            # Send playlist name to client
            socket.send_string(playlist_name)
        else:
            break
            
context.destroy()