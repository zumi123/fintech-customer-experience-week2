from google_play_scraper import reviews, Sort
import pandas as pd
import time

def get_reviews(app_id, bank_name, num_reviews=400):
    all_reviews = []
    count = 0

    while len(all_reviews) < num_reviews:
        print(f"Fetching batch {count + 1} for {bank_name}...")
        result, _ = reviews(
            app_id,
            lang='en',
            country='et',
            sort=Sort.NEWEST,
            count=200,
            filter_score_with=None
        )
        all_reviews.extend(result)
        count += 1
        time.sleep(1)

        if count > 10:
            break

    df = pd.DataFrame(all_reviews)
    df['bank'] = bank_name
    df['source'] = 'Google Play'
    return df[['content', 'score', 'at', 'bank', 'source']]

def main():
    apps = {
        'com.combanketh.mobilebanking': 'CBE',
        'com.boa.boaMobileBanking': 'BOA',
        'com.dashen.dashensuperapp': 'Dashen Bank'
    }

    all_dfs = []

    for app_id, bank_name in apps.items():
        df = get_reviews(app_id, bank_name)
        all_dfs.append(df)

    final_df = pd.concat(all_dfs, ignore_index=True)
    final_df.to_csv('data/raw_reviews.csv', index=False)
    print("Reviews saved to data/raw_reviews.csv")

if __name__ == "__main__":
    main()
