import streamlit as st
from utils.data_fetcher import (
    get_player_id,
    get_last_5_games,
    get_last_5_home_or_away_games,
    get_last_5_games_against_opponent
)

# Streamlit UI
st.title("PropNerd: NBA Player Stats")

# Input: NBA player name
player_name = st.text_input("Enter NBA player name:")

# Input: Opponent team abbreviation (for demonstration purposes)
opponent_abbreviation = st.text_input("Enter opponent team abbreviation (e.g., 'HOU' for Rockets):")

# Input: Is the current game home or away
location = st.selectbox("Is the current game at home or away?", ['home', 'away'])

# Analyze button
if st.button("Analyze"):
    if player_name:
        # Step 1: Get player ID
        player_id = get_player_id(player_name)
        if isinstance(player_id, str):
            st.write(player_id)  # Player not found
        else:
            # Step 2: Fetch last 5 games (regardless of location)
            last_5_games = get_last_5_games(player_id)
            st.write("Last 5 Games (All):", last_5_games[['GAME_DATE', 'MATCHUP', 'PTS', 'AST', 'REB']])

            # Step 3: Fetch last 5 home or away games (based on location input)
            last_5_home_or_away = get_last_5_home_or_away_games(player_id, location)
            st.write(f"Last 5 Games ({location.title()}):", last_5_home_or_away[['GAME_DATE', 'MATCHUP', 'PTS', 'AST', 'REB']])

            # Step 4: Fetch last 5 games against the opponent
            if opponent_abbreviation:
                last_5_vs_opponent = get_last_5_games_against_opponent(player_id, opponent_abbreviation)
                st.write(f"Last 5 Games vs {opponent_abbreviation.upper()}:", last_5_vs_opponent[['GAME_DATE', 'MATCHUP', 'PTS', 'AST', 'REB']])
    else:
        st.write("Please enter a valid player name.")
