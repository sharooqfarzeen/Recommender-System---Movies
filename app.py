import streamlit as st
import os
from dotenv import load_dotenv

from get_resources import get_movies_similarity
from get_reco import recommend_movie
from get_posters import fetch_posters

# Page title and layout settings
st.set_page_config(page_title="Movie Recommender System")

# Fetching movies dataframe and similarity vectors
if 'movies_list' not in st.session_state or 'similarity_vectors' not in st.session_state or 'movies_df' not in st.session_state:
    st.session_state["movies_df"], st.session_state["similarity_vectors"], st.session_state["movies_list"] = get_movies_similarity()


st.title("Movie Recommender System")

# Getting movie name from user
# with st.form(key='movie'):
movie_name = st.selectbox("Movies Similar to:", options=st.session_state["movies_list"], placeholder="Choose a movie", index=None)
# submit = st.form_submit_button(label='Show Similar Movies')

if movie_name:
    similar_movies = recommend_movie(movie_name)
    st.header(f"{movie_name}")
    for i in range(len(similar_movies)):
        st.write(f"{i+1}. {similar_movies[i]}")