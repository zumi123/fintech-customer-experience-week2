import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from pathlib import Path

# Load cleaned review data with sentiment
csv_path = "data/with_sentiment.csv"
df = pd.read_csv(csv_path)

# Ensure correct data types
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.dropna(subset=['review', 'sentiment'], inplace=True)

# Plot 1: Sentiment distribution by bank
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='sentiment', hue='bank')
plt.title('Sentiment Distribution by Bank')
plt.xlabel('Sentiment')
plt.ylabel('Review Count')
plt.tight_layout()
sentiment_plot = "data/sentiment_distribution_by_bank.png"
plt.savefig(sentiment_plot)
plt.close()

# Plot 2: Rating distribution
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='rating', bins=5, hue='bank', multiple='stack')
plt.title('Rating Distribution by Bank')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.tight_layout()
rating_plot = "data/rating_distribution_by_bank.png"
plt.savefig(rating_plot)
plt.close()

# Plot 3: WordCloud per bank
wordcloud_paths = []
for bank in df['bank'].unique():
    bank_reviews = " ".join(df[df['bank'] == bank]['review'].astype(str))
    wc = WordCloud(width=800, height=400, background_color='white').generate(bank_reviews)
    path = f"data/wordcloud_{bank.replace(' ', '_')}.png"
    wc.to_file(path)
    wordcloud_paths.append(path)

(sentiment_plot, rating_plot, wordcloud_paths)
