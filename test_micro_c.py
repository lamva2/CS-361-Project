import zmq
import json

context = zmq.Context()

print("Connecting to microservice C...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

date = input("Enter date: ")

print("Sending Message: %s\n" % date)
socket.send_string(date)
is_deleted = socket.recv_string()

print("Sending exit.")
socket.send_string("exit")

context.destroy()