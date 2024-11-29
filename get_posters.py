import requests
import streamlit as st


def fetch_posters(movie_ids):
    api_key = st.secrets['tmdb']
    posters = []
    for movie_id in movie_ids:
        response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key))

        data = response.json()

        poster_id = data['poster_path']
        
        poster_path = "https://image.tmdb.org/t/p/w500" + poster_id
        
        posters.append(poster_path)
        
    return posters  