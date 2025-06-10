# sentiment_analysis.py

import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

# Load pre-trained sentiment model (DistilBERT fine-tuned on SST-2)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Load data
reviews_df = pd.read_csv("data/fintech_reviews_clean.csv")

# Sentiment Analysis
def get_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    scores = softmax(outputs.logits.numpy()[0])
    label = ["negative", "positive"][scores.argmax()]
    return label, float(scores.max())

# Apply sentiment analysis
reviews_df['sentiment'], reviews_df['sentiment_score'] = zip(*reviews_df['review'].map(get_sentiment))

# Save results
reviews_df.to_csv("data/with_sentiment.csv", index=False)

print("Sentiment analysis completed. Results saved to 'data/with_sentiment.csv'")
