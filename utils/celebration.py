# utils/celebration.py

import streamlit as st
import time
import random

def show_winner_celebration(player):
    st.balloons()
    st.success(f"🎉 Congratulations {player['name']}! You won the game! 🎉")

    # Optional: Fancy ASCII or emoji fireworks
    fireworks = ["✨", "🎆", "🎇", "🌟"]
    for _ in range(5):
        st.markdown(
            f"<h3 style='text-align: center; color: gold;'>{random.choice(fireworks)} {player['name']} {random.choice(fireworks)}</h3>",
            unsafe_allow_html=True
        )
        time.sleep(0.5)
