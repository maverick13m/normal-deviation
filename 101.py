import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
df2 = pd.read_csv("2.csv")
#height
fig1 = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)
fig1.show()

#Weight
fig2 = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)
fig2.show()

#Homework

fig3 = ff.create_distplot([df2["Avg Rating"].tolist()],["Avg Rating"],show_hist=True)
fig3.show()




