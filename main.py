# This is a sample Python script.
import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import msvcrt

CREDS_FILE = 'C:/Users/NWAL0169/PycharmProjects/SlideFlick/credentials.json'
CLIENT_ID = 'C:/Users/NWAL0169/PycharmProjects/SlideFlick/credentials.json'
CLIENT_SECRET = 'C:/Users/NWAL0169/PycharmProjects/SlideFlick/client_secrets.json'
SCOPES = ['https://www.googleapis.com/auth/presentations.readonly', 'https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/gmail.readonly']

# slides-id = ‘1Z1Q4jy5pL9NprL2hWkiA3UR173h50yRCAatoyGM8Cfw’


REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'


def get_refresh_token():
    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            'C:/Users/NWAL0169/PycharmProjects/SlideFlick/client_secrets.json',
            SCOPES,
            redirect_uri=REDIRECT_URI
        )

        # Redirect user to OAuth 2.0 consent page
        authorization_url, _ = flow.authorization_url()
        print(_)
        print('Please go to this URL to authorize access:', authorization_url)

        # Obtain authorization code from user
        authorization_response = input('Paste the full redirect URL here: ')
        flow.fetch_token(authorization_response=authorization_response)

        # Access and store the refresh token
        refresh_token = flow.credentials.refresh_token()
        print('Refresh Token:', refresh_token)

    except Exception as e:
        print('An error occurred during token retrieval:', str(e))


def authenticate():
    creds = None

    if os.path.exists(CREDS_FILE):
        creds = Credentials.from_authorized_user_file(CREDS_FILE)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
        creds = flow.run_local_server(port=0)
        print(flow.credentials.refresh_token())
        with open(CREDS_FILE, 'w') as token:
            token.write(creds.to_json())

        return creds


def get_presentation_slides(presentation_id):
    creds = authenticate()
    service = build('slides', 'v1', credentials=creds)

    presentation = service.presentations().get(presentationId=presentation_id).execute()
    slides = presentation.get('slides', [])

    return slides


def navigate_through_slides(slides):
    if not slides:
        print('No slides found.')
        return

    current_slide_index = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
        print(f'Currently on Slide {current_slide_index + 1}')
        print('Press "n" for next slide, "p" for previous slide, or "q" to quit.')
        # Read keyboard input
        key = msvcrt.getch().decode('utf-8').lower()
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
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    presentation_id = '1Z1Q4jy5pL9NprL2hWkiA3UR173h50yRCAatoyGM8Cfw'
    get_refresh_token()
    slides = get_presentation_slides(presentation_id)
    navigate_through_slides(slides)
