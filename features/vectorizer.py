
import pandas as pd
import joblib

from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("data/processed/cleaned_emails.csv")

df["clean_email"] = df["clean_email"].fillna("")

vectorizer = CountVectorizer(
    max_features=1400,
    ngram_range=(1, 2),
    min_df=1
)

X = vectorizer.fit_transform(df["clean_email"])

joblib.dump(vectorizer, "models/count_vectorizer.pkl")

print("Matrix Shape:", X.shape)
print("Vocabulary Size:", len(vectorizer.vocabulary_))

