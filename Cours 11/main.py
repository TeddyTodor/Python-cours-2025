import pandas as pd
import numpy as np 
import myplotlib.pyplot as plt

data_path = "Data\oscar_age_female.csv"
df = pd.read_csv(data_path)


aimed_columns = ("Year", "Movie")
df = df[aimed_columns]
df = df[df["Name"] == "Luise Rainer"]
print(df.head(10))