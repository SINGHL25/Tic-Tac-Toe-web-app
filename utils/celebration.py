# utils/celebration.py

import streamlit as st
import time

def show_winner_celebration(winner):
    st.balloons()
    st.success(f"🎉 Player {winner} wins the game!")
    time.sleep(1)
