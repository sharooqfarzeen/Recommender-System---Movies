import pickle

def get_movies_similarity():
    movies_df = pickle.load(open('movies_dataframe.pkl', 'rb'))
    similarity_vectors = pickle.load(open('similarity_vectors.pkl', 'rb'))
    movies_list = movies_df['title'].values

    return movies_df, similarity_vectors, movies_list