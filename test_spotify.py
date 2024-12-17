
from dotenv import load_dotenv
import os
import requests
import base64

load_dotenv()


# they blocked the API so it longer works to many people where training models from the looks of it. 

def get_spotify_token():
    CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

    if not (CLIENT_ID and CLIENT_SECRET):
        print("Missing Spotify credentials. Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET.")
        return None

    # Spotify Token URL
    token_url = "https://accounts.spotify.com/api/token"

    # Basic Authentication for the Spotify API
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode("utf-8")).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Payload to obtain token
    data = {
        "grant_type": "client_credentials"
    }

    # Make the request to obtain the access token
    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:
        token = response.json()["access_token"]
        print("Successfully obtained token.")
        return token
    else:
        print(f"Error obtaining token: {response.status_code}")
        return None

def main():
    # Get access token
    token = get_spotify_token()
    if not token:
        return

    # Track IDs
    track_ids = [
        '6VwBbL8CzPiC4QV66ay7oR'
    ]
    
    # Fetch Audio Features from Spotify API
    url = f"https://api.spotify.com/v1/audio-analysis/6VwBbL8CzPiC4QV66ay7oR"
    headers = {
        'Authorization': f"Bearer {token}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.json())  # Print out the audio features
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    main()
