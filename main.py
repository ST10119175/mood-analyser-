from mood_analyzer import SpotifyMoodAnalyzer

import os
import requests
import base64

from dotenv import load_dotenv



# Load environment variables
load_dotenv()



def main():

      # Retrieve credentials from environment variables
    CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    PLAYLIST_ID = os.getenv('SPOTIFY_PLAYLIST_ID', '0JrAPPgKGVTuSl3jXVTyAg')  # Default playlist

    # Initialize mood analyzer
    mood_analyzer = None
    features = None

    #The features no longer works. (To many people trying to train AI with it)
    # Attempt to fetch data from Spotify API
    if CLIENT_ID and CLIENT_SECRET:
        try:
            print("Attempting to fetch data from Spotify API...")
            mood_analyzer = SpotifyMoodAnalyzer(CLIENT_ID, CLIENT_SECRET)
            tracks = mood_analyzer.get_playlist_tracks(PLAYLIST_ID)
            if tracks:
                print(f"Retrieved {len(tracks)} tracks. Extracting audio features...")
                features = mood_analyzer.extract_audio_features(tracks)
                if features is not None and not features.empty:
                    print("Successfully retrieved audio features from Spotify API.")
        except Exception as e:
            print(f"Failed to retrieve data from Spotify API: {e}")
    else:
        print("Spotify credentials not found. Skipping API call.")

    # Fallback to dummy data if API fails
    if features is None or features.empty:
        print("Loading dummy data...")
        mood_analyzer = SpotifyMoodAnalyzer("dummy_client_id", "dummy_client_secret")  # Dummy client info
        features = mood_analyzer.generate_dummy_data(num_tracks=100)
        print(f"Generated {len(features)} tracks with simulated audio features.")

    # Proceed with mood analysis
    try:
        print("Clustering tracks by mood...")
        clustered_data = mood_analyzer.cluster_moods(features)
        print("Clustering complete.")

        print("Visualizing mood distribution...")
        mood_analyzer.visualize_mood_distribution(clustered_data)

        print("Generating mood analysis report...")
        report = mood_analyzer.mood_analysis_report(clustered_data)
        print("Mood Analysis Report:")
        for cluster, stats in report.items():
            print(f"{cluster}: {stats}")
    except Exception as e:
        print(f"An error occurred during mood analysis: {e}")

if __name__ == "__main__":
    main()