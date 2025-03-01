import zmq # type: ignore
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

definitions = {
    "Bar Chart": "Graph which compares data using bars to represent values. They are often used for categorical data.",
    "Line Graph": "Graph which uses lines to connect data points. They are often used to show how a variable changes over time.",
    "Scatter Plot": "Graph which uses dots to represent values. They are often used for larger, more spread datasets."
}
    
# Convert the input term to lowercase and check for matching term
while True:
    try:
        term = socket.recv_string()

        if len(term) > 0:
            print("Message Recieved: %s\n" % term)

        term_lower = term.lower()

        if term == "exit":
            break

        found = False

        for key in definitions:
            if key.lower() == term_lower:
                socket.send_string(definitions[key])
                found = True
                break

        if not found:
            socket.send_string("Sorry, that definition could not be found.")
    
    except zmq.ZMQError as e:
        print(f"Error encountered while trying to send/receive: {e}")
        break

print("Goodbye!\n")
context.destroy()