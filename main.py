# This is a sample Python script.
import cv2
import mediapipe as mp
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import msvcrt
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
hands = mp_hands.Hands()
CREDS_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/presentations.readonly']

# slides-id = 1Z1Q4jy5pL9NprL2hWkiA3UR173h50yRCAatoyGM8Cfw


def authenticate():
    creds = None

    if os.path.exists(CREDS_FILE):
        creds = Credentials.from_authorized_user_file(CREDS_FILE)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open(CREDS_FILE, 'w') as token:
            token.write(creds.to_json())

    return creds


def get_presentation_slides(presentation_idd):
    creds = authenticate()
    service = build('slides', 'v1', credentials=creds)

    presentation = service.presentations().get(presentationId=presentation_idd).execute()
    slidess = presentation.get('slides', [])

    return slidess


def navigate_through_slides(slidess):
    if not slidess:
        print('No slides found.')
        return

    current_slide_index = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
        print(f'Currently on Slide {current_slide_index + 1}')
        print('Press "n" for next slide, "p" for previous slide, or "q" to quit.')

        # Read keyboard input
        key = msvcrt.getch().decode('utf-8').lower()
        # Currently linked to keyboard REPLACE WITH HAND GESTURES as variables
        if key == 'n':
            current_slide_index = (current_slide_index + 1) % len(slides)
        elif key == 'p':
            current_slide_index = (current_slide_index - 1) % len(slides)
        elif key == 'q':
            break  # Exit loop if 'q' is pressed
        else:
            print('Invalid input. Please try again.')

    print('Exiting.')


if __name__ == '__main__':
    # Replace with your actual presentation ID
    presentation_id = '1Z1Q4jy5pL9NprL2hWkiA3UR173h50yRCAatoyGM8Cfw'
    slides = get_presentation_slides(presentation_id)
    # Change navigate method and put in handtracking loop with gesture recognition
    navigate_through_slides(slides)

    while True:
        data, image = cap.read()
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow('Handtracker', image)
        cv2.waitKey(1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/