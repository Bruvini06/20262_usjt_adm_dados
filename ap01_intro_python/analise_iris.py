import os
import pandas as pd

# Descobre exatamente onde este .py está salvo
pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta_script, "Iris.csv")

df = pd.read_csv(caminho_csv)
# print(df.shape)

# print(df.head())

# print(df["Species"].value_counts())

print(df.groupby("Species")["PetalLengthCm"].mean().round(3))