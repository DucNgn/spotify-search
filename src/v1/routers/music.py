"""
Search a track on Spotify
"""
from fastapi import APIRouter
from pydantic import BaseModel
import requests

from config import SPOTIFY_TOKEN
from .handle_exceptions import invalid_arguments, error

search_router = APIRouter(
    prefix="/track", responses={"404": {"description": "Not found"}}
)


class TrackResults(BaseModel):
    name: str
    artist: str
    duration: str
    url: str


def process_tracks_response(response):
    items = response["tracks"]["items"]

    def process_item(item):
        name = item["name"]
        artist_name = item["album"]["artists"][0]["name"]
        url = item["external_urls"]["spotify"]
        duration = item["duration_ms"]
        return TrackResults(name=name, artist=artist_name, duration=duration, url=url)

    res = [process_item(item) for item in items]
    return res


@search_router.get("/track")
async def search_track(name: str = None, limit: int = None):
    """
    Search info by track name
    """
    if not name:
        return invalid_arguments(msg="Please provide a track name")

    SPOTIFY_URL = "https://api.spotify.com/v1/search"
    PARAMS = {"q": name, "type": "track", "limit": limit or 5}

    try:
        res = requests.get(
            url=SPOTIFY_URL,
            params=PARAMS,
            headers={"Authorization": f"Bearer {SPOTIFY_TOKEN}"},
        )
        res.raise_for_status()
        res_data = res.json()
    except requests.exceptions.HTTPError as e:
        return error(code=e.response.status_code, msg=e.response.reason)
    except Exception as e:
        return error()
    else:
        return {"res": process_tracks_response(res_data)}
