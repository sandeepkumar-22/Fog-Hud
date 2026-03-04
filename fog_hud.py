import cv2
import serial
import time
from ultralytics import YOLO

# CONFIGURATION
SERIAL_PORT = "COM5" 
BAUD_RATE = 115200

DANGER_CLASSES = ["person", "car", "dog", "cat"]
DIST_DANGER = 20
DIST_WARNING = 50

# INITIALIZE
ser = serial.Serial("COM5", 115200, timeout=1)
time.sleep(2)

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

print("System Started...")

# MAIN LOOP
while True:

    #Read Distance From ESP32
    distance = 999
    try:
        line = ser.readline().decode().strip()
        if "Distance" in line:
            distance = float(line.split(":")[1].replace("cm", "").strip())
    except:
        pass

    #Capture Camera Frame
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    vision_danger = False

    #YOLO Detection
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls]

            if label in DANGER_CLASSES and conf > 0.5:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                vision_danger = True

                cv2.rectangle(frame, (x1, y1), (x2, y2),
                              (0, 0, 255), 2)

                cv2.putText(frame, f"{label} {conf:.2f}",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 2)

    # SENSOR FUSION LOGIC
    if distance < DIST_DANGER and vision_danger:
        status = "DANGER"
        color = (0, 0, 255)
        ser.write(b'1')  #buzzer
    elif distance < DIST_WARNING:
        status = "WARNING"
        color = (0, 255, 255)
        ser.write(b'0')
    else:
        status = "SAFE"
        color = (0, 255, 0)
        ser.write(b'0')

    #Display
    cv2.putText(frame, f"Distance: {distance:.1f} cm",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, color, 2)

    cv2.putText(frame, status,
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, color, 3)

    cv2.imshow("AI Smart Safety System", frame)

    if cv2.waitKey(1) == 27:
        break

# CLEANUP
cap.release()
cv2.destroyAllWindows()
ser.close()