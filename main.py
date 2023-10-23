# This is a sample Python script.
import os
import json
import secrets
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
<<<<<<< HEAD

CREDS_FILE = 'C:/Users/noahc/PycharmProjects/SlideFlickReal/credentials.json'
CLIENT_ID = 'C:/Users/noahc/PycharmProjects/SlideFlickReal/credentials.json'
CLIENT_SECRET = 'C:/Users/noahc/PycharmProjects/SlideFlickReal/client_secrets.json'
=======
import msvcrt

CREDS_FILE = 'C:/Users/NWAL0169/PycharmProjects/SlideFlick/credentials.json'
CLIENT_ID = 'C:/Users/NWAL0169/PycharmProjects/SlideFlick/credentials.json'
CLIENT_SECRET = 'C:/Users/NWAL0169/PycharmProjects/SlideFlick/client_secrets.json'
>>>>>>> 45b0957975b5e2cbf3f38f3e1b80ed04103970bb
SCOPES = ['https://www.googleapis.com/auth/presentations.readonly', 'https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/gmail.readonly']

# slides-id = ‘1Z1Q4jy5pL9NprL2hWkiA3UR173h50yRCAatoyGM8Cfw’

state = secrets.token_urlsafe(16)
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'


def get_refresh_token():
    try:
        flow = InstalledAppFlow.from_client_secrets_file(
<<<<<<< HEAD
            'C:/Users/noahc/PycharmProjects/SlideFlickReal/client_secrets.json',
=======
            'C:/Users/NWAL0169/PycharmProjects/SlideFlick/client_secrets.json',
>>>>>>> 45b0957975b5e2cbf3f38f3e1b80ed04103970bb
            SCOPES,
            redirect_uri=REDIRECT_URI
        )

        # Redirect user to OAuth 2.0 consent page
        authorization_url, _ = flow.authorization_url(state=state)
<<<<<<< HEAD
        print('Please go to this URL to authorize access:', authorization_url)

        # Load JSON data from a file
        credentials_file_path = 'C:/Users/noahc/PycharmProjects/SlideFlickReal/credentials.json'

        with open(credentials_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Obtain authorization code from user
        code = input('Paste the full redirect URL here: ')
        flow.fetch_token(code=code)

        # Update the refresh token in the JSON data
        print('Main Check 1')
        data["installed"]["refresh_token"] = flow.credentials.refresh_token
        print('Main Check 2')
        # Write the updated data back to the file
        with open(credentials_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
            print('Main Check 3')
        # print(updated_json)
        # print('Check 3')
        # Add or modify data
        # json_data['refresh_token'] = refresh_token

        # Access and store the refresh token
        # refresh_token = flow.credentials.refresh_token()
        # json_data["installed"]['refresh_token'] = refresh_token
        # print('Refresh Token:', refresh_token)

        # Save the updated JSON data back to the file
        # with open('C:/Users/noahc/PycharmProjects/SlideFlickReal/credentials.json', 'w') as json_file:
        #    json.dump(json_data, json_file, indent=4)
=======
        print(_)
        print('Please go to this URL to authorize access:', authorization_url)

        # Load JSON data from a file
        with open('credentials.json', 'r') as json_file:
            json_data = json.load(json_file)

        # Obtain authorization code from user
        authorization_response = input('Paste the full redirect URL here: ')
        json_data["installed"]['refresh_token'] = flow.fetch_token(authorization_response=authorization_response)
        # Add or modify data
        # json_data['refresh_token'] = refresh_token

        # Save the updated JSON data back to the file
        with open('credentials.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        # Access and store the refresh token
        refresh_token = flow.credentials.refresh_token()
        print('Refresh Token:', refresh_token)
>>>>>>> 45b0957975b5e2cbf3f38f3e1b80ed04103970bb

    except Exception as e:
        print('An error occurred during token retrieval:', str(e))


def authenticate():
    creds = None

    if os.path.exists(CREDS_FILE):
        creds = Credentials.from_authorized_user_file(CREDS_FILE)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
        creds = flow.run_local_server(port=0)
<<<<<<< HEAD
        print(flow.credentials.refresh_token)
=======
        print(flow.credentials.refresh_token())
>>>>>>> 45b0957975b5e2cbf3f38f3e1b80ed04103970bb
        with open(CREDS_FILE, 'w') as token:
            token.write(creds.to_json())

        return creds


def get_presentation_slides(presentation_id):
    creds = authenticate()
    service = build('slides', 'v1', credentials=creds)

    presentation = service.presentations().get(presentationId=presentation_id).execute()
    slides = presentation.get('slides', [])

<<<<<<< HEAD
    return slides, service


def navigate_through_slides(slides,service):
=======
    return slides


def navigate_through_slides(slides):
>>>>>>> 45b0957975b5e2cbf3f38f3e1b80ed04103970bb
    if not slides:
        print('No slides found.')
        return

    current_slide_index = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
        print(f'Currently on Slide {current_slide_index + 1}')
        print('Press "n" for next slide, "p" for previous slide, or "q" to quit.')
        # Read keyboard input
<<<<<<< HEAD
        key = input('N = next P = back Q = bye')
=======
        key = msvcrt.getch().decode('utf-8').lower()
>>>>>>> 45b0957975b5e2cbf3f38f3e1b80ed04103970bb
        if key == 'n':
            current_slide_index = (current_slide_index + 1) % len(slides)
            requests = [
                {
                    'updatePageProperties': {
                        'objectId': presentation_id,
                        'pageProperties': {
                            'pageObjectIds': presentation_id,
                            'pageNumber': current_slide_index,
                        },
                        'fields': 'pageNumber',
                    }
                }
            ]

            # Send the request to move to the next slide
            body = {
                'requests': requests,
            }
            response = service.presentations().batchUpdate(presentationId=presentation_id, body=body).execute()
            # Print the response (usually contains information about the changes made)
            print(response)
        elif key == 'p':
            current_slide_index = (current_slide_index - 1) % len(slides)
        elif key == 'q':
            break  # Exit loop if 'q' is pressed
        else:
            print('Invalid input. Please try again.')

    print('Exiting.')


if __name__ == '__main__':
    # Replace with your actual presentation ID
<<<<<<< HEAD
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    presentation_id = '1Z1Q4jy5pL9NprL2hWkiA3UR173h50yRCAatoyGM8Cfw'
    get_refresh_token()
    slides,service = get_presentation_slides(presentation_id)
    navigate_through_slides(slides,service)
=======
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    presentation_id = '1Z1Q4jy5pL9NprL2hWkiA3UR173h50yRCAatoyGM8Cfw'
    get_refresh_token()
    slides = get_presentation_slides(presentation_id)
    navigate_through_slides(slides)
>>>>>>> 45b0957975b5e2cbf3f38f3e1b80ed04103970bb
