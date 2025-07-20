import streamlit as st

def show_winner_celebration(winner_name):
    st.balloons()
    st.success(f"🎉 Congratulations {winner_name}! You will host the next Scrum! 🎉")
