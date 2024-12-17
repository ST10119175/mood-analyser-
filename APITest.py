import os
import requests
import base64

from dotenv import load_dotenv

# 1. My mistakes: the playlist must be public 
# 2. Possible issue : the playlist must not be a generated playlist

load_dotenv()

# Spotify Credentials

# Playlist Information
#PLAYLIST_ID = '0JrAPPgKGVTuSl3jXVTyAg'
PLAYLIST_ID = '1JckPj8pGefaXlRjTENPxr'

# Retrieve credentials from environment variables
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
#PLAYLIST_ID = os.getenv('SPOTIFY_PLAYLIST_ID')


def get_access_token(client_id, client_secret):
    """Get Spotify access token using client credentials."""
    # Encode client credentials
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    
    # Token request headers
    headers = {
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    # Token request data
    data = {'grant_type': 'client_credentials'}
    
    # Make token request
    token = response = requests.post('https://accounts.spotify.com/api/token', 
                             headers=headers, 
                             data=data)
    
    
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Error retrieving access token: {response.status_code}")
        print(response.text)
        return None


def get_playlist_tracks(access_token, playlist_id):
   
   




   
    """Retrieve tracks from a Spotify playlist."""
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Parameters to fetch tracks
    params = {
        'limit': 100,  # Adjust as needed
        'fields': 'items(track(name,artists(name)))'  # Specify the fields you want
    }
    
    try:
        response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', 
                                headers=headers, 
                                params=params)
        
        # Check for different possible error codes
        if response.status_code == 200:
            tracks = response.json()
            return tracks['items']
        elif response.status_code == 401:
            print("Error: Unauthorized. The access token may have expired.")
        elif response.status_code == 403:
            print("Error: Forbidden. Check playlist permissions.")
        elif response.status_code == 404:
            print("Error: Playlist not found.")
        else:
            print(f"Unexpected error: {response.status_code}")
            print(response.text)
        
        return None
    
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None




def main():
    # Get access token
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    
    if not access_token:
        print("Failed to obtain access token.")
        return
    
    # Get playlist tracks
    tracks = get_playlist_tracks(access_token, PLAYLIST_ID)
    
    if tracks:
        print("Playlist Tracks:")
        for item in tracks:
            track = item['track']
            print(f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")

if __name__ == '__main__':
    main()


    