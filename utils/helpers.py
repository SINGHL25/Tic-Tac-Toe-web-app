# utils/helper.py
import streamlit as st
import time
import random


def show_winner_celebration(player):
    st.balloons()
    st.markdown("## 🎉 Congratulations!")
    st.image(player["image"], width=200) if player["image"] else None
    for _ in range(10):
        st.markdown(f"### 🎆 {random.choice(['🔥', '✨', '💥', '🎇', '🎆'])} Winner Party 🎆")
        time.sleep(0.2)

