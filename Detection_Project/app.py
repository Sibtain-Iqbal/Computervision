from flask import Flask, render_template
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-detection')
def start_detection():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

        for (x, y, w, h) in faces:
            center = (x + w // 2, y + h // 2)
            radius = max(w, h) // 2
            cv2.circle(frame, center, radius, (0, 255, 0), 3)  # Green circle
            cv2.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 0), 3)  # Blue ellipse

        cv2.imshow('Face Detection with Circle and Ellipse', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return "Face detection started!"

if __name__ == '__main__':
    app.run(debug=True)
