import cv2
from turtle import *
import math

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

def heart_a(n):

    return 15 * math.sin(n) ** 3


def heart_b(n):

    return 12 * math.cos(n)- 5 * \
        math.cos(2*n)- 2 *\
        math.cos(3*n)- \
        math.cos(4*n)

tracer (5)
bgcolor("black")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı.")
        break

   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=3, minSize=(20, 30))

  
    if len(faces) > 0:
        print("Yüz Tespit Edildi - KALP ÇİZİLİYOR")
        clear() 
        for i in range(300):

            goto (heart_a(i)*15, heart_b(i)*15)

            for j in range(1):

                color('blue') 
                hideturtle()
                goto(0,0)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (150,30, 150), 2)  # Yüz etrafında dikdörtgen çiz

    else:
        print("Yüz Tespit Edilemedi - KALP ÇİZİLMİYOR")
        clear()  

   
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
