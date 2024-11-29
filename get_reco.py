import pandas
import streamlit as st

# Function which recommends 5 similar movies, given a movie name
def recommend_movie(movie_name: str):

    df, similarity = st.session_state["movies_df"], st.session_state["similarity_vectors"]

     # getting index of movie in dataframe  
    movie_index = df[df['title'] == movie_name].index[0]
    
    # Similarity vector for the given movie
    sim = similarity[movie_index]
    
    # Enumerating to add indices to the vector
    sim = list(enumerate(sim))
    
    # Sorting based on similarity and assiging first 5 movies
    similar_movie_indices = sorted(sim, reverse=True, key=lambda x: x[1])[1:6]
    
    # Similar movies
    similar_movies_titles = [df.loc[index[0], 'title'] for index in similar_movie_indices]

    # # Movie Ids
    # movie_ids = [df.loc[index[0], 'movie_id'] for index in similar_movie_indices]
    
    return similar_movies_titles