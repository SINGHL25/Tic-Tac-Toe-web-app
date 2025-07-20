# utils/celebration.py

import streamlit as st
import time
import random

def show_winner_celebration(player):
    st.balloons()
    st.markdown(f"## 🎉 Congratulations {player['name']}! 🎉")
    
    for _ in range(5):
        st.markdown(
            f"<h3 style='color: {random.choice(['red', 'green', 'blue', 'purple', 'orange'])};'>🏆 {player['name']} wins the Scrum Battle!</h3>",
            unsafe_allow_html=True
        )
        time.sleep(0.3)
