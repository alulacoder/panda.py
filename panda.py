import pandas as pd

df = pd.DataFrame({
    "Name": ["Pulkit Chawla", "Tom Brouwers", "Jlula", "Danstan", "Ian", "james"],
    "Age": [23, 14, 10, 20, 30, 40],
    "City": ["Berlin", "Amsterdam", "New York", "LA", "London", "Paris"]
})

print(df.head())
print(df.info())
print(df.describe())
print(df.shape)

print(df["Name"])
print(df["Age"].max)
print(type(df["Age"]))
