#reading csv file using pandas
import pandas as pd

scores = pd.read_csv("d/scores.csv")
print(scores["Total"].max())
