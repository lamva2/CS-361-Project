# Microservice B: Implement visualization generator (creates visualization
# using variables and visualization chosen)
# 1. Main program sends variable and visualization style
# 2. Microservice generates visualization and saves it to file
# 3. Microservice sneds image path which the user can access
# Note: everytime microservice is called, previous visualization will be
# overwritten with new visualization (let user know to save/download image)

import zmq # type: ignore
import matplotlib.pyplot as plt
import pandas as pd

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    try:
        message = socket.recv_string()
        print(f"Received request from the client: {message}")

        if len(message) > 0:
            print("Message Recieved: %s\n" % message)
            
        if message == "exit":
            break
        
        # Data Frame
        data = pd.read_csv("C:\\Users\\vlam3\\OneDrive\\Desktop\\CS 361\\CS-361-Project\\snow_data.csv")
        df = pd.DataFrame(data)
        
        # File name to save to
        custom_visual = "custom_visualization.png"
        
        # Variables
        x = list(df.iloc[:, 0])
        y = list(df.iloc[:, 1])
        title = "Total Snowfall Over Time"
        x_label = "Date"
        y_label = "Total Snowfall (inch)"
        
        print("Generating graph.")
        
        # Bar Chart
        if message == "bar chart":
            plt.figure()
            plt.bar(x,y)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(custom_visual)
        # Line Graph
        elif message == "line graph":
            plt.figure()
            plt.plot(x, y)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(custom_visual)
        # Scatter Plot
        elif message == "scatter plot":
            plt.figure()
            plt.scatter(x, y)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(custom_visual)
        
        print("Path to custom visual sent to client.")
        socket.send_string(custom_visual) 
    
    except zmq.ZMQError as e:
        print(f"Error encountered while trying to send/receive: {e}")
        break

context.destroy()
    