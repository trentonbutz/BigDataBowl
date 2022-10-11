# https://www.kaggle.com/code/datarohitingole/nfl-data-analysis-and-plotly-animation/notebook
import urllib.request
from PIL import Image
import plotly.graph_objects as go

def plotPlay(playDF, title):
    teams = playDF['team'].unique()
    colors = ["#396EB0", "#116530", "red"]
    plotly_logo = Image.open('field.png')

    fig = go.Figure()

    for team, color in zip(teams, colors):
        fig.add_trace(go.Scatter(
            x = playDF.query(f"team == '{team}'").x,
            y = playDF.query(f"team == '{team}'").y,
            mode = "markers",
            name=team,
            marker=dict(color=color)
        ))
    fig.update_layout(
        template="plotly_white",
        autosize=False,
        width=1000,
        height=550,
        images= [dict(source=plotly_logo,
                      xref="paper", yref="paper",x=0, y=1, sizex=1, sizey=1,
                      layer="below", opacity=0.5)],
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        title=title,
        xaxis_title="x",
        yaxis_title="y",
    )
    plotly_logo.close()
    return(fig)