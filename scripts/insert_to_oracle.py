import pandas as pd
import oracledb

# Load cleaned CSV
df = pd.read_csv("data/with_sentiment.csv")

# Connect to Oracle 23ai
conn = oracledb.connect(
    user="system",
    password="YourStrongPassword",  
    dsn="localhost/FREE"
)
cursor = conn.cursor()

# Insert unique banks and store their IDs
bank_id_map = {}
for bank in df["bank"].unique():
    # Insert if not already exists
    cursor.execute("MERGE INTO banks b USING (SELECT :name AS name FROM dual) d ON (b.name = d.name) " 
               "WHEN NOT MATCHED THEN INSERT (name) VALUES (d.name)", [bank])

    # Get the bank_id
    cursor.execute("SELECT id FROM banks WHERE name = :name", [bank])
    bank_id = cursor.fetchone()[0]

    bank_id_map[bank] = bank_id

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (review, rating, review_date, bank_id, source, sentiment, sentiment_score)
        VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7)
    """, [
        row['review'], row['rating'], row['date'],
        bank_id_map[row['bank']], row['source'],
        row['sentiment'], row['sentiment_score']
    ])

conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully!")
