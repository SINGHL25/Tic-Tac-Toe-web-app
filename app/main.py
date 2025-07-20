# app/main.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.tic_tac_toe import TicTacToe
from utils.helper import show_winner_celebration
import time


players = []
game = TicTacToe()


def run_app():
    st.set_page_config(page_title="Tic Tac Toe - Scrum Battle", layout="centered")
    st.title("🔥 Tic Tac Toe Scrum Battle 🔥")

    with st.sidebar:
        st.header("Player Setup")
        for i in range(6):
            name = st.text_input(f"Player {i+1} Name:", key=f"name_{i}")
            img = st.file_uploader(f"Player {i+1} Image (Optional):", type=['jpg', 'png'], key=f"img_{i}")
            players.append({"name": name, "image": img})

        if st.button("Start Game"):
            st.session_state.start = True
            st.session_state.board = ["" for _ in range(9)]
            st.session_state.current = 0
            st.experimental_rerun()

    if not st.session_state.get("start"):
        st.info("Add players and click Start Game")
        return

    st.subheader(f"Current Player: {players[st.session_state.current]['name']}")

    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            idx = i * 3 + j
            if st.session_state.board[idx] == "":
                if cols[j].button(" ", key=f"btn_{idx}"):
                    st.session_state.board[idx] = "X" if st.session_state.current % 2 == 0 else "O"
                    winner = game.check_winner(st.session_state.board)
                    if winner:
                        st.success(f"🏆 Winner is: {players[st.session_state.current]['name']} 🏆")
                        show_winner_celebration(players[st.session_state.current])
                        st.session_state.start = False
                    elif "" not in st.session_state.board:
                        st.warning("It's a draw!")
                        st.session_state.start = False
                    else:
                        st.session_state.current = (st.session_state.current + 1) % len(players)
                    st.experimental_rerun()
            else:
                cols[j].write(f"**{st.session_state.board[idx]}**")


