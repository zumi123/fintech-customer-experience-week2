# Customer Experience Analytics for Fintech Apps 

This repository contains a four-part project aimed at analyzing user reviews from Ethiopian fintech apps to uncover satisfaction drivers and improvement opportunities. The project progresses from data collection to insight generation, simulating real-world data science and engineering pipelines in the banking sector.

---

## Project Structure

```
├── data/                       # Raw and processed review datasets
├── plots/                      # Generated plots for insights
├── preprocessing/              # Scripts for cleaning, sentiment, thematic analysis
├── scraping/                   # Script to scrape reviews from Google Play
├── scripts/                    # Oracle DB insert scripts
├── requirements.txt            # Python dependencies
├── .gitignore                  # Files/directories to ignore in Git
├── README.md                   # Project overview (you are here)
├── task4_report.pdf            # report for task-4
```

---

## Tasks Overview

### Task 1: Data Collection and Preprocessing
- Scraped reviews (400+ each) from the Google Play Store for 3 banks using `google-play-scraper`
- Cleaned and saved 1,200+ reviews in a structured CSV file
- Managed code using Git (branch: `task-1`)

### Task 2: Sentiment and Thematic Analysis
- Applied sentiment analysis using DistilBERT and basic rules
- Extracted top keywords with TF-IDF and grouped them into 3–5 themes per bank
- Output included labeled CSV and plotted sentiment trends
- (branch: `task-2`)

### Task 3: Store Cleaned Data in Oracle
- Set up Oracle 23ai in Docker
- Created relational schema (`banks`, `reviews`)
- Inserted 500+ reviews via Python script
- Validated with SQL (branch: `task-3`)

### Task 4: Insights and Recommendations
- Visualized sentiment and ratings using Matplotlib/Seaborn
- Generated word clouds and identified drivers/pain points
- Made UX recommendations for app improvement
- (branch: `task-4`)

---

## How to Run

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Run preprocessing:
   ```bash
   python preprocessing/clean_data.py
   python preprocessing/sentiment_analysis.py
   python preprocessing/thematic_analysis.py
   ```

3. Insert to Oracle:
   ```bash
   python scripts/insert_to_oracle.py
   ```

4. View insights notebook or plots in `plots/`

---

## Outputs

- Cleaned review dataset with sentiments and themes
- Oracle DB populated with 500+ labeled reviews
- Insightful visualizations: rating trends, sentiment bar charts, word clouds
- Final report with actionable recommendations

---

This project demonstrates an end-to-end NLP workflow applied to real user data from mobile banking apps. It emphasizes explainability, ethical considerations, and actionable findings.
