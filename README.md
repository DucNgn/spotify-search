# Spotify Search API

Simple Spotify API for searching tracks

## Installation:
First, create a new file `.secrets.toml` with the content:
  ```
    SPOTIFY_TOKEN="{YOUR_TOKEN_HERE}"
  ```
  Token can be retrieved from https://developer.spotify.com

Then there're 2 ways to run the server:

### With Docker-compose:
+ `docker-compose up --build -d` to build the container and run it.
+ Go to `localhost:8000` for the API home endpoint.
+ Go to endpoint `/docs` for the swagger UI of the API service.

### Without Docker:
+ `poetry install` to install dependencies
+ `poetry shell` to go into the virtual environment
+ `poetry run python src/main.py` to start the local server
