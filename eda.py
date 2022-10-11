import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    layout="centered", page_icon="🌐", page_title="Big Data Bowl 2023 EDA"
)

st.header("Games Data")
games = pd.read_csv("data/games.csv")
st.dataframe(games)

st.header("Team Play Frequency")
teamType = st.radio("Select a type", ("homeTeamAbbr", "visitorTeamAbbr"))
fig = px.histogram(games, x=teamType)
st.plotly_chart(fig, use_container_width=True)

st.header("PFF Scouting Data")
pff = pd.read_csv("data/pffScoutingData.csv")
st.dataframe(pff)

st.header("Players")
players = pd.read_csv("data/players.csv")
st.dataframe(players)

players['heightIN'] = players['height'].apply(lambda x: int(x.split('-')[0]) * 12 + int(x.split('-')[1]))
fig = px.scatter(x = players['heightIN'], y = players['weight'], color = players['officialPosition'],
                title = 'Positions by Height and Weight', labels = {'x': 'Height (inches)', 'y': 'Weight (lbs)'})
st.plotly_chart(fig, use_container_width=True)

st.header("Plays")
plays = pd.read_csv("data/plays.csv")
st.dataframe(plays)

st.header("All Games")
allGamesDfs = [pd.read_csv(f"data/week{x}.csv") for x in range(1, 9)]
allGames = pd.concat(allGamesDfs)
st.dataframe(allGames.head(250))

st.header("Game Viewer")
gameId = st.selectbox("Select a game", games.gameId.unique())
game = allGames[allGames.gameId == gameId]
playId = st.selectbox("Select a play", game.playId.unique())
play = game[game.playId == playId]
st.dataframe(play)
fig = px.scatter(play, x='x', y='y', title = f"{plays[playId == plays.playId].playDescription.values[0]}")
st.plotly_chart(fig, use_container_width=True)
