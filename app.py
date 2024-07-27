import pandas as pd
import streamlit as st
import pickle


def recommend(movie, movies, similarity):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            st.write(f"Movie ID: {movie_id} (Type: {type(movie_id)})")  # Debug statement
            recommended_movies.append(movies.iloc[i[0]].title)

        return recommended_movies
    except Exception as e:
        st.error(f"Error in recommendation: {e}")
        return []


# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values)

if st.button("Recommend"):
    names = recommend(selected_movie_name, movies, similarity)

    for name in names:
        st.header(name)

