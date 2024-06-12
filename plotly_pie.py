# Here we are using plotly express to create a pie chart of bird window collision deaths by building number
# it was my first time using plotly express and I found it very easy to use

import plotly.express as px
import pandas as pd


dfb = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/bird-window-collision-death.csv')

fig = px.pie(dfb, values='Deaths', names='Bldg #', color='Side', hole=0.3) # hole is the size of the hole in the middle of the pie chart
fig.update_traces(insidetextfont=dict(color='white'), textinfo='label+percent') # this will make the text white and show the label and percentage
fig.update_layout(title_text='Bird Window Collision Deaths by Building Number', legend={"itemclick":False}) # this will remove the ability to click on the legend
fig.show() # this will show the pie chart