# VOICE-ASSISTANT-USING-PYTHON-AND-ARDUINO
This project is a simple voice-controlled assistant built using Python for voice recognition and Arduino for executing hardware-level commands. It demonstrates how natural language input can control devices and perform automated tasks in real time.

🔧** Features**
Voice recognition using Python's speech_recognition library

Integration with Arduino via pySerial

Basic command execution (e.g., LED on/off, sensor reading)

Modular and beginner-friendly codebase

🧠 **Technologies Used**
Python 3

Arduino Uno

speech_recognition

pyttsx3 (text-to-speech)

pyserial

Arduino IDE (C++)

🛠️ **Requirements**
Python 3.x installed

Arduino IDE

USB connection between PC and Arduino

Required Python libraries:
pip install speechrecognition pyttsx3 pyserial
⚙️ How It Works
The Python script listens for voice commands using a microphone.

Recognized commands are parsed and matched to predefined actions.

Commands are sent over serial to the Arduino.

The Arduino interprets the command and performs the action (like turning an LED on/off).
📂 **Project Structure**
voice-assistant-arduino/
│
├── voice_assistant.py       # Main Python script
├── arduino_code.ino         # Arduino sketch
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
🎯 **Example Commands**
"Turn on the light"

"Turn off the light"

"Read temperature"

👨‍💻 **Authors**

Manas Bhatt
Hoza Mihu
Avdesh Belwal

📹 **Working Video**
link: http://tiny.cc/h05m001

🎓 **Academic Info**
This project was submitted in partial fulfillment for the degree of Bachelor of Technology in Computer Science & Engineering at Dev Bhoomi Uttarakhand University.

📜 **License**
This project is licensed for academic and learning purposes.

