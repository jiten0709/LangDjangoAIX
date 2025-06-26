from django.conf import settings
import requests

base_url = "https://api.themoviedb.org/3"


def get_headers():
    return {
    "accept": "application/json",
    "Authorization": f"Bearer {settings.TMDB_API_KEY}"
}


def search_movie(query:str, page:int=1, raw=False,):
    url = f"{base_url}/search/movie"
    params = {
        "query": query,
        "page": page,
        "include_adult": True,
        "language": "en-US",
    }
    headers = get_headers()
    response = requests.get(url, headers=headers, params=params)
    if raw:
        return response
    return response.json()


def movie_detail(movie_id:int, raw=False,):
    url = f"{base_url}/movie/{movie_id}"
    params = {
        "include_adult": True,
        "language": "en-US",
    }
    headers = get_headers()
    response = requests.get(url, headers=headers, params=params)
    if raw:
        return response
    return response.json()
