import cv2

#use pretrained model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

    for (x, y, w, h) in faces:
        # Calculate center and radius for the circle
        center = (x + w // 2, y + h // 2)
        radius = max(w, h) // 2
        cv2.circle(frame, center, radius, (0, 0, 255), 3)  # Green circle

        
        cv2.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (0, 0,255), 3)  

    
    cv2.imshow('Face Detection and make cicle around Face', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
