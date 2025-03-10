# Microservice D: Implement write to file
# 1. Main program sends user input and what file to write to
# 2. Appends to corresponding file
# 3. Used for adding notes (notes page) and asking questions (help and resources page)
# Notes: questions.json and notes.json file need to be nonempty (meaning having data or having [])

import zmq
import json
from datetime import datetime

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")

while True:
    message = socket.recv_string()
    print(f"Received message: {message}")
    
    if len(message) > 0 and message != "exit":
        try:
    
            data = json.loads(message)
            
            file_path = data["file"]
            note = data["note"]
            date = datetime.today().strftime('%Y-%m-%d')
            
            new_data = {
                "date": date,
                "note": note 
            }
            
            try:
                with open(file_path, 'r') as json_file:
                    existing_data = json.load(json_file)
            except FileNotFoundError:
                existing_data = []
                
            existing_data.append(new_data)
            
            with open(file_path, 'w') as json_file:
                json.dump(existing_data, json_file, indent=4)
            
            print(f"Write to file {file_path} was successful.")
            socket.send_string("True")
            
        except FileNotFoundError:
            print("File not found.")
            break
        except json.JSONDecodeError:
            print("Error decording JSON in file.")
            break 
    else:
        break
    
context.destroy()