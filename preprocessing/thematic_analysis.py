from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re
import string

# Load the cleaned reviews with sentiment
df = pd.read_csv("data/with_sentiment.csv")

# --- Preprocessing ---
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df["cleaned_review"] = df["review"].apply(clean_text)

# --- TF-IDF for keyword extraction ---
tfidf_vectorizer = TfidfVectorizer(max_df=0.85, min_df=2, ngram_range=(1, 2), max_features=100)
tfidf_matrix = tfidf_vectorizer.fit_transform(df["cleaned_review"])
keywords = tfidf_vectorizer.get_feature_names_out()

# --- Theme keyword definitions ---
theme_keywords = {
    "Account Access Issues": ["login", "password", "access", "locked"],
    "Transaction Performance": ["transfer", "delay", "transaction", "failed", "pending"],
    "User Interface & Experience": ["ui", "design", "navigate", "interface", "layout"],
    "Customer Support": ["support", "help", "response", "contact"],
    "Feature Requests": ["feature", "add", "missing", "update"]
}

# --- Assign themes ---
def identify_themes(text):
    matched_themes = []
    for theme, words in theme_keywords.items():
        if any(word in text for word in words):
            matched_themes.append(theme)
    return "; ".join(matched_themes) if matched_themes else "Other"

df["identified_theme"] = df["cleaned_review"].apply(identify_themes)

# --- Save to CSV ---
df["review_id"] = df.index
final_df = df[["review_id", "review", "sentiment", "sentiment_score", "identified_theme"]]
final_df.to_csv("data/review_themes_rule_based.csv", index=False)
