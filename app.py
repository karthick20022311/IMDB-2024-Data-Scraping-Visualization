import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("IMDb 2024 Movie Dashboard")

# Load dataset
df = pd.read_csv("IMDB_2024_movies_cleaned.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Top Rated Movies")

top_rated = df.sort_values(by="Rating", ascending=False).head(10)

fig, ax = plt.subplots()
ax.barh(top_rated["Movie Name"], top_rated["Rating"])
ax.invert_yaxis()

st.pyplot(fig)

st.subheader("Most Voted Movies")

top_votes = df.sort_values(by="Votes", ascending=False).head(10)

fig2, ax2 = plt.subplots()
ax2.barh(top_votes["Movie Name"], top_votes["Votes"])
ax2.invert_yaxis()

st.pyplot(fig2)