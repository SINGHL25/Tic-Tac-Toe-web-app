import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.tic_tac_toe import TicTacToe
from utils.celebration import show_winner_celebration

def run_app():
    st.set_page_config(page_title="Tic Tac Toe - Scrum Battle", layout="centered")
    st.title("🔥 Tic Tac Toe Scrum Battle 🔥")

    # Initialize session state variables once
    if "players" not in st.session_state:
        st.session_state.players = [{"name": "", "image": None} for _ in range(6)]
    if "start" not in st.session_state:
        st.session_state.start = False
    if "board" not in st.session_state:
        st.session_state.board = ["" for _ in range(9)]
    if "current" not in st.session_state:
        st.session_state.current = 0

    with st.sidebar:
        st.header("Player Setup")
        for i in range(6):
            name = st.text_input(f"Player {i+1} Name:", value=st.session_state.players[i]["name"], key=f"name_{i}")
            img = st.file_uploader(f"Player {i+1} Image (Optional):", type=['jpg', 'png'], key=f"img_{i}")
            st.session_state.players[i]["name"] = name
            st.session_state.players[i]["image"] = img

        if st.button("Start Game"):
            # Validate at least 2 players with names
            valid_players = [p for p in st.session_state.players if p["name"].strip() != ""]
            if len(valid_players) < 2:
                st.warning("Please enter names for at least 2 players to start.")
            else:
                st.session_state.start = True
                st.session_state.board = ["" for _ in range(9)]
                st.session_state.current = 0
                st.experimental_rerun()

    if not st.session_state.start:
        st.info("Add players and click Start Game")
        return

    game = TicTacToe()
    current_player = st.session_state.players[st.session_state.current]

    st.subheader(f"Current Player: {current_player['name']}")

    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            idx = i * 3 + j
            mark = st.session_state.board[idx]

            if mark == "":
                if cols[j].button(" ", key=f"btn_{idx}"):
                    st.session_state.board[idx] = "X" if st.session_state.current % 2 == 0 else "O"
                    winner = game.check_winner(st.session_state.board)
                    if winner:
                        st.success(f"🏆 Winner is: {current_player['name']} 🏆")
                        show_winner_celebration(current_player)
                        st.session_state.start = False
                    elif "" not in st.session_state.board:
                        st.warning("It's a draw!")
                        st.session_state.start = False
                    else:
                        # Move to next player with a name (skip empty)
                        next_player = (st.session_state.current + 1) % len(st.session_state.players)
                        while st.session_state.players[next_player]["name"].strip() == "":
                            next_player = (next_player + 1) % len(st.session_state.players)
                        st.session_state.current = next_player
                    st.experimental_rerun()
            else:
                cols[j].write(f"**{mark}**")

if __name__ == "__main__":
    run_app()



