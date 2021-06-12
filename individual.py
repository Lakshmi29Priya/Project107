import pandas as pd
import plotly.graph_objects as go
import csv
df=pd.read_csv("data.csv")
student_df=df.loc[df['Roll No']=="3"]
print(student_df.groupby("Marks In Percentage")["Days Present"].mean())

fig=go.Figure(go.Bar(
    x=student_df.groupby("Marks In Percentage")["Days Present"].mean(),
    y=['3'],
    orientation='h'
))
fig.show()