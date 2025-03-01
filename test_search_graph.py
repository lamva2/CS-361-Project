import zmq

context = zmq.Context()

print("Connecting to microservice A...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

term = input("Enter a term to define: ")

print("Sending Message: %s\n" % term)
socket.send_string(term)

definition = socket.recv_string()
print("Message Recieved: %s\n" % definition)
print("The definiton for the term %s is %s\n" % (term, definition))

message = "exit"
socket.send_string(message)
print("Message Sent: %s\n" % message)