import pandas as pd
import matplotlib.pyplot as plt

data_path = "Data/temp.csv"
df = pd.read_csv(data_path,skipinitialspace=True)

def display_columns(df : pd.DataFrame) :
    print("Columns")
    for col in df.columns :
        print(f"-c{col}")

def filter_data (df : pd.DataFrame) :
    
    #Columns filtering
    options = ["name", "z"]
    df_filtered = df[options]

    #Rows filtering
    aimed_characteristic = "name"
    aimed_value = "A"
    condition = df_filtered[aimed_characteristic] == aimed_value
    df_filtered = df_filtered[condition]
    print(df_filtered.head(5))
    return df_filtered


plt.scatter(df["x"], df["y"], c= df["z"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()