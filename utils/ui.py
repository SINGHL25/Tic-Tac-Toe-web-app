import streamlit as st

def display_player_grid(players, images):
    cols = st.columns(len(players))
    for idx, player in enumerate(players):
        with cols[idx]:
            st.image(images[idx] if images[idx] else "https://via.placeholder.com/100", width=100)
            st.markdown(f"**{player}**")
