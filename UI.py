
import streamlit as st
import pandas as pd

# Load game metadata
df = pd.read_csv("game_metadata.csv")

st.title("Game Metadata Explorer")

# Filters
genre_filter = st.multiselect("Filter by Genre", options=df['Genres'].dropna().unique())
platform_filter = st.multiselect("Filter by Platform", options=df['Platforms'].dropna().unique())
min_rating = st.slider("Minimum Rating", min_value=0.0, max_value=5.0, value=0.0)

# Apply filters
filtered_df = df.copy()

if genre_filter:
    filtered_df = filtered_df[filtered_df['Genres'].str.contains('|'.join(genre_filter), na=False)]

if platform_filter:
    filtered_df = filtered_df[filtered_df['Platforms'].str.contains('|'.join(platform_filter), na=False)]

filtered_df = filtered_df[filtered_df['Rating'] >= min_rating]

st.write(f"Found {len(filtered_df)} games matching your criteria:")
st.dataframe(filtered_df)

# Download option
st.download_button("Download Filtered CSV", filtered_df.to_csv(index=False), file_name="filtered_games.csv")

