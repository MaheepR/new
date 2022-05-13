import pandas as pd

df = pd.read_csv('dwarf_stars.csv')

df.head()
df.shape

df = df.dropna()
df.info()

df.shape

df.Mass = df.Mass.str.replace('[^a-zA-Z0-9]','').astype('float')

df["Radius"] = df["Radius"] * (0.102763)

df["Mass"] = float(df["Mass"]*(0.000954588))