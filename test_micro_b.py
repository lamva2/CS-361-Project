import zmq
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

context = zmq.Context()

print("Connecting to microservice B...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

term = input("Enter visualization: ")

print("Sending Message: %s\n" % term)
socket.send_string(term)

graph_path = socket.recv_string()
print("Message Recieved: %s\n" % graph_path)

# Load the graph
graph = mpimg.imread(graph_path)
plt.imshow(graph)
plt.show()

term = "exit"
print("Sending Message: %s\n" % term)
socket.send_string(term)
context.destroy()