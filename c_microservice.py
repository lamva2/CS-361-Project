# Microservice C: Implement search for note and delete from text file
# If the user chooses to delete a certain note entry, ask the user
# for the date of the entry and microservice will search for that
# date in the text file and delete it from the text file

import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:
    date_to_delete = socket.recv_string()
    print(f"Received request from the client: {date_to_delete}")
    
    if len(date_to_delete) > 0 and date_to_delete != "exit":
        try:
            file_path = 'notes.json'
            
            # Load the data from the file
            with open(file_path, 'r') as f:
                notes = json.load(f)
            
            # Filter out the note with the given date
            updated_notes = [note for note in notes if note['date'] != date_to_delete]
            
            # Check if any notes were deleted
            if len(updated_notes) == len(notes):
                print(f"No note found for date {date_to_delete}")
                socket.send_string("False")
                break
            
            # Save the updated list back to the file
            with open(file_path, 'w') as f:
                json.dump(updated_notes, f, indent=4)
            
            print(f"Note for {date_to_delete} deleted successfully.")
            socket.send_string("True")
            
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except json.JSONDecodeError:
            print("Error decording JSON in file.")
    else:
        break
    
context.destroy()