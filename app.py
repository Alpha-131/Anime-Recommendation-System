import streamlit as st
import pickle 
import pandas as pd


def recommend(anime_name):
    anime_index = anime[anime['Title'] == anime_name].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)),reverse = True, key=lambda x:x[1])[1:6]
    
    rec_anime = []
    for i in anime_list:
        if i == "Unknown":
            rec_anime.append(anime.iloc[i[0]].JN)
        else:
            rec_anime.append(anime.iloc[i[0]].Title)
    return rec_anime

jikan_url = "https://api.jikan.moe/v3/search/anime"

similarity = pickle.load(open('similarity.pkl','rb'))

anime_dict = pickle.load(open('anime.pkl','rb'))
anime = pd.DataFrame(anime_dict)

st.title("Anime Recommender System")

selected_anime = st.selectbox('Enter an anime to get suggestions',anime['Title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_anime)
    for i in recommendations:
        st.write(i)

