#AI Smart Safety Assistance System
Real-Time Object Detection + Distance-Based Danger Alert
🏆 Achievement

#🥈 Winner – 2nd Prize at Visionathon
This project was presented at Visionathon and secured Second Place for innovation, technical execution, and real-world impact.

# 📌 Project Overview
The AI Smart Safety Assistance System is a real-time intelligent safety prototype that combines:
🎥 YOLOv8 Object Detection
📏 Ultrasonic Distance Measurement
🧠 Sensor Fusion Logic
🔊 Buzzer Alert System
🔵 LED Status Indicator
The system detects nearby objects using computer vision and measures their real-world distance using an ultrasonic sensor connected to ESP32. When an object comes within a dangerous threshold, the system instantly triggers alerts.
This creates a low-cost intelligent driver-assistance style system.

#🎯 Problem Statement
Accidents often occur due to:
Low visibility (fog, night driving)
Blind spots
Human reaction delay
Lack of real-time distance awareness
Existing advanced safety systems are expensive and not accessible to everyone.
This project provides a cost-effective, AI-powered safety layer.

# DEMO
[fog hud.pptx](https://github.com/user-attachments/files/25743420/fog.hud.pptx)
![pic_1](https://github.com/user-attachments/assets/58273a42-0757-4f21-aa5e-da58fe833cb5)
![pic](https://github.com/user-attachments/assets/345fb389-2867-44cf-b3de-d42d31a96d69)

#🧠 System Working (Sensor Fusion Architecture)
🔹 1. Vision Layer (Laptop Camera + YOLOv8)
Captures real-time video
Detects objects such as:
Person
Car
Animals
Obstacles
Draws bounding boxes with labels

#🔹 2. Distance Layer (ESP32 + Ultrasonic Sensor)
Ultrasonic sensor measures distance in centimeters
ESP32 sends data via Serial communication to Python
Provides real-world physical distance

#🔹 3. Decision Layer (AI Logic)
If:
Object is detected
AND
Distance < Safety Threshold
Then:
🔴 Bounding box turns RED
⚠ Danger message displayed
🔊 Buzzer activates
Otherwise:
🟢 Bounding box stays GREEN
🔵 Blue LED indicates SAFE mode
This is real-time AI-based threat analysis.
🏗 System Architecture

Laptop (Python + YOLO + OpenCV)
│
│ Serial Communication (115200 baud)
│
ESP32
├── Ultrasonic Sensor
├── Buzzer
└── Blue LED

# 🛠 Hardware Components
ESP32
Ultrasonic Sensor (HC-SR04)
Buzzer
Blue LED
Breadboard
Jumper wires
Laptop with camera

#💻 Software Stack
Python 3.8+
OpenCV
Ultralytics YOLOv8
PySerial
Arduino IDE

# 🚀 Setup Instructions
1️⃣ Upload ESP32 Code
Open Arduino IDE
Select ESP32 board
Upload ultrasonic + buzzer code
Note the COM port

2️⃣ Run Python Program
Update COM port in the Python file:
ser = serial.Serial("COM5", 115200, timeout=1)
Then run:
python fog_hud.py
Press ESC to exit.

#⚙️ Key Features
✔ Real-time object detection
✔ Live distance measurement
✔ Intelligent danger detection
✔ Automatic buzzer activation
✔ Visual warning overlay
✔ Low-cost prototype
✔ Scalable architecture

#📊 Technical Specifications
Model Used: YOLOv8n
Detection Speed: ~20–30 FPS (CPU)
Ultrasonic Accuracy: ±1 cm
Communication Speed: 115200 baud
Danger Threshold: 50 cm (configurable)
💰 Prototype Cost
Approximate total cost: ₹1000 (~$15)
Affordable and scalable for smart safety applications.

#🌍 Applications
Driver Assistance Systems
Fog Detection Safety Systems
Smart Helmets
Industrial Safety Monitoring
Autonomous Robotics
Smart City Infrastructure

#🔮 Future Scope
LiDAR integration
Depth camera support
Edge AI deployment (Jetson Nano)
Object tracking (DeepSORT)
Speed estimation
Automatic braking system

#🏁 Conclusion
This project demonstrates how AI + embedded systems + sensor fusion can create practical, affordable safety solutions.
Winning 🥈 2nd Prize at Visionathon validates its innovation and real-world relevance.
