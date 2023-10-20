import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.9)
mp_drawing = mp.solutions.drawing_utils

model = load_model('gestureRecognizer')

f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

cap = cv2.VideoCapture(0)
previous_name = ""
how_many = 0
while True:
    _, frame = cap.read()

    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(frame_rgb)

    className = ''
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mp_drawing.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            # print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]

            if previous_name == className:
                how_many = how_many + 1
            if previous_name != className:
                how_many = 0
            previous_name = className

            if how_many >= 8:
                # print(className)
                # here is where we will put the code for the rest of the things and remember to set how many back to 0 or lower
                if className == "thumbs down":
                    print("next slide")

                if className == "thumbs up":
                    print("back 1 slide")

    cv2.imshow("Output", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
