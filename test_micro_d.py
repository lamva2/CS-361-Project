import zmq
import json

context = zmq.Context()

print("Connecting to microservice D...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

file = input("Enter file: ")
note = input("Enter note: ")

data = {
    "file": file,
    "note": note
}

print("Sending Message")
message = json.dumps(data)
socket.send_string(message)
is_added = socket.recv_string()

print("Sending exit.")
socket.send_string("exit")

context.destroy()