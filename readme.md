# Spotify Mood Analyzer

## Overview

Spotify Mood Analyzer is a data science project that leverages the Spotify API to analyze the emotional characteristics of music tracks. By extracting audio features and applying machine learning clustering techniques, this tool provides insights into the mood distribution of a playlist.

## Features

- 🎵 Fetch tracks from a Spotify playlist
- 🔍 Extract audio features using Spotify's API
- 📊 Cluster tracks by mood characteristics
- 📈 Generate mood distribution visualization
- 🛡️ Robust error handling with dummy data fallback

## Prerequisites

- Python 3.8+
- Spotify Developer Account
- Spotify API Credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/spotify-mood-analyzer.git
cd spotify-mood-analyzer
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with your Spotify API credentials:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_PLAYLIST_ID=your_playlist_id  # Optional
```

### Obtaining Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create a new application
3. Copy your Client ID and Client Secret

## Usage

Run the main script:
```bash
python mood_analyzer_main.py
```

## Project Structure

```
spotify-mood-analyzer/
│
├── mood_analyzer.py         # Core mood analysis logic
├── mood_analyzer_main.py    # Main execution script
├── requirements.txt          # Project dependencies
└── .env                     # Environment configuration
```

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Spotify Web API
- Matplotlib

## Machine Learning Approach

The project uses unsupervised learning (clustering) to group tracks based on:
- Tempo
- Energy
- Danceability
- Valence (musical positiveness)

## Visualization

The script generates a mood distribution plot, showing how tracks are clustered across different emotional spectrums.

## Error Handling

- Graceful API connection failure
- Automatic fallback to simulated data
- Comprehensive logging

## Future Improvements

- [ ] Add more advanced mood classification
- [ ] Implement playlist recommendation
- [ ] Create interactive visualization
- [ ] Support multiple playlist analysis

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

