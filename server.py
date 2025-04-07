import serial
import json
import time
from flask import Flask, render_template, jsonify
import threading
import os

# Create Flask app
app = Flask(__name__, template_folder='.')

# Global variable to store latest data
latest_data = {
    "weight": 0.0,
    "alert": False
}

# Arduino port - set to COM6 as specified
ARDUINO_PORT = "COM6"
BAUD_RATE = 9600

# Function to read data from Arduino
def read_from_arduino():
    global latest_data
    
    try:
        arduino = serial.Serial(port=ARDUINO_PORT, baudrate=BAUD_RATE, timeout=1)
        time.sleep(2)  # Allow time for connection to establish
        print(f"Connected to Arduino on {ARDUINO_PORT}!")
        
        while True:
            if arduino.in_waiting:
                line = arduino.readline().decode('utf-8').strip()
                
                # Look for JSON data (starts with { and ends with })
                if line.startswith("{") and line.endswith("}"):
                    try:
                        data = json.loads(line)
                        latest_data = data
                        print(f"Weight: {data['weight']}, Alert: {data['alert']}")
                    except json.JSONDecodeError:
                        print(f"Error parsing JSON: {line}")
                # Also print regular output lines for debugging
                elif line:
                    print(f"Arduino says: {line}")
            
            time.sleep(0.1)
    
    except Exception as e:
        print(f"Error connecting to Arduino on {ARDUINO_PORT}: {e}")
        print("Please check if the Arduino is connected and the port is correct.")
        print("You may need to restart this script after connecting the Arduino.")

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint for getting data
@app.route('/data')
def get_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    # Start Arduino reading in a separate thread
    arduino_thread = threading.Thread(target=read_from_arduino)
    arduino_thread.daemon = True
    arduino_thread.start()
    
    # Print instructions
    print("\n=======================================")
    print("SETUP INSTRUCTIONS:")
    print(f"1. Arduino should be connected to {ARDUINO_PORT}")
    print("2. Save the HTML file as 'index.html' in the same folder as this script")
    print("3. Access the website at: http://127.0.0.1:5000")
    print("=======================================\n")
    
    # Start Flask server
    app.run(debug=True, use_reloader=False)