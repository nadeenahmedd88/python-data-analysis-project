import pandas as pd

df = pd.read_csv("3) Sentiment dataset.csv")

df.info()

df.drop(columns=["Unnamed: 0"], inplace=True)
df.drop(columns=["Unnamed: 0.1"], inplace=True)

df.isnull().sum()
df = df.drop_duplicates()

df["Sentiment"] = df["Sentiment"].str.lower().str.strip()
df["Platform"] = df["Platform"].str.lower().str.strip()
df["Country"] = df["Country"].str.strip()  


date_cols = ["Year", "Month", "Day", "Hour"]

for col in date_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.dropna(subset=date_cols, inplace=True)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df.to_csv("cleaned_sentiment_dataset.csv", index=False)


df.info()

