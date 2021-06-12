import pandas as pd
import plotly.graph_objects as go
import csv

df=pd.read_csv("data.csv")
print(df.groupby("Marks In Percentage")["Days Present"].mean())

fig=go.Figure(go.Bar(
    x=df.groupby("Marks In Percentage")["Days Present"].mean(),
    y=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"],
    orientation='h'
))
fig.show()