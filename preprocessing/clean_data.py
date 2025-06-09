# preprocessing/clean_data.py

import pandas as pd
import os

def preprocess_reviews(input_file='data/raw_reviews.csv', output_file='data/fintech_reviews_clean.csv'):
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"❌ Input file '{input_file}' not found.")
        return

    # Read the CSV file
    df = pd.read_csv(input_file)

    if df.empty:
        print("❌ The input CSV is empty.")
        return

    print(f"📦 Loaded {len(df)} rows")

    # Drop duplicate reviews
    df = df.drop_duplicates(subset=['content'])
    print(f"🧹 After dropping duplicates: {len(df)} rows")

    # Drop rows with missing content, rating, or date
    df = df.dropna(subset=['content', 'score', 'at'])

    # Normalize date
    df['date'] = pd.to_datetime(df['at'], errors='coerce').dt.date
    df = df.dropna(subset=['date'])

    # Rename columns
    df = df.rename(columns={
        'content': 'review',
        'score': 'rating'
    })

    # Final column selection
    df_final = df[['review', 'rating', 'date', 'bank', 'source']]

    # Save output
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df_final.to_csv(output_file, index=False)

    print(f"✅ Cleaned data saved to {output_file}")
    print(f"📊 Final shape: {df_final.shape}")

if __name__ == "__main__":
    preprocess_reviews()
