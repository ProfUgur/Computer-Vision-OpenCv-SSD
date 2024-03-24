import cv2

# Load pre-trained SSD model
model_file = "ssd_mobilenet_v3_large_coco/frozen_inference_graph.pb"
config_file = "ssd_mobilenet_v3_large_coco.pbtxt"
net = cv2.dnn_DetectionModel(model_file, config_file)

# Set input size and scale
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Open video capture (0 for webcam, or file path)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read frame from camera
    
    # Detect objects in the frame
    classes, confidences, boxes = net.detect(frame, confThreshold=0.5)
    
    # Draw bounding boxes around detected objects
    if len(classes) > 0:
        for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
            cv2.rectangle(frame, box, color=(0, 255, 0), thickness=2)
            cv2.putText(frame, f"{classId}", (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display frame
    cv2.imshow("Object Detection", frame)
    
    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()