# mood_analyzer.py
import os
import requests
import base64
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Dict, Any
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class SpotifyMoodAnalyzer:
    def __init__(self, client_id, client_secret):
        """Initialize Spotify client."""
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        ))

    def generate_dummy_data(self, num_tracks=100):
        """Generate dummy data to simulate audio features."""
     
        dummy_data = {
        'danceability': np.random.rand(num_tracks),
        'energy': np.random.rand(num_tracks),
        'valence': np.random.rand(num_tracks),
        }
        return pd.DataFrame(dummy_data)



    def get_playlist_tracks(self, playlist_id):
        """Fetch tracks from a Spotify playlist."""
        try:
            tracks = []
            results = self.sp.playlist_tracks(playlist_id)
            while results:
                tracks.extend(results['items'])
                results = self.sp.next(results) if results['next'] else None
            print(f"Retrieved {len(tracks)} tracks.")
            return tracks
        except spotipy.exceptions.SpotifyException as e:
            print(f"Spotify API Error: {e}")
            if e.http_status == 403:
                print("403 Forbidden: Check credentials or permissions.")
            raise

    def extract_audio_features(self, tracks):
        """Retrieve audio features for tracks, skipping tracks with no features."""
        track_ids = [track['track']['id'] for track in tracks if track['track']]
        print(f"Track IDs: {track_ids}")  # Debugging output

        try:
            features = self.sp.audio_features(track_ids)
            # Filter out tracks with no audio features
            valid_features = [f for f in features if f is not None]
            print(f"Retrieved audio features for {len(valid_features)} valid tracks.")
            df = pd.DataFrame(valid_features)
            return df
        except spotipy.exceptions.SpotifyException as e:
            print(f"Error while retrieving audio features: {e}")
            raise

    def cluster_moods(self, features):
        """Cluster tracks based on audio features."""
        try:
            clustering_features = features[['danceability', 'energy', 'valence']].dropna()
            kmeans = KMeans(n_clusters=3, random_state=42).fit(clustering_features)
            features['mood_cluster'] = kmeans.labels_
            print("Tracks successfully clustered by mood.")
            return features
        except Exception as e:
            print(f"Error during clustering: {e}")
            raise

    def visualize_mood_distribution(self, features):
        """Visualize the distribution of mood clusters."""
        try:
            mood_counts = features['mood_cluster'].value_counts()
            mood_counts.plot(kind='bar', color=['blue', 'green', 'orange'])
            plt.title("Mood Distribution")
            plt.xlabel("Mood Cluster")
            plt.ylabel("Number of Tracks")
            plt.show()
        except Exception as e:
            print(f"Error during visualization: {e}")
            raise

    def mood_analysis_report(self, features):
        """Generate a detailed mood analysis report."""
        report = {}
        try:
            for cluster in features['mood_cluster'].unique():
                cluster_data = features[features['mood_cluster'] == cluster]
                report[f"Cluster {cluster}"] = {
                    'Average Danceability': cluster_data['danceability'].mean(),
                    'Average Energy': cluster_data['energy'].mean(),
                    'Average Valence': cluster_data['valence'].mean(),
                }
            return report
        except Exception as e:
            print(f"Error generating mood analysis report: {e}")
            raise