import pandas as pd
import csv 
import plotly.figure_factory as ff

df=pd.read_csv("Mobileratings.csv")
graph=ff.create_distplot([df["Avg Rating"].tolist()], ["Ratings"], show_hist=False)
graph.show()