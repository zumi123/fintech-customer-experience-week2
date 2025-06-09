# Customer Experience Analytics for Fintech Apps (Week 2)

This project involves collecting and analyzing user reviews from Ethiopian fintech mobile banking applications using data from the Google Play Store. It includes web scraping, data preprocessing, and version control using Git.

---

## Objectives

- Scrape customer reviews from Google Play Store for 3 major Ethiopian banks.
- Preprocess the data: clean, normalize, and store it in a structured format.
- Maintain codebase with good Git practices.

---

## Target Banks

1. Commercial Bank of Ethiopia (CBE)
2. Bank of Abyssinia
3. Dashen Bank

---

## Project Structure

```
fintech-customer-experience-week2/
│
├── data/
│   ├── raw_reviews.csv              # Raw scraped data
│   └── fintech_reviews_clean.csv    # Cleaned and processed data
│
├── scraping/
│   └── scraper.py                   # Script to scrape reviews from Google Play
│
├── preprocessing/
│   └── clean_data.py                # Script to preprocess and clean review data
│
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Files/directories to ignore in Git
└── README.md                        # Project documentation
```

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fintech-customer-experience-week2.git
   cd fintech-customer-experience-week2
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Methodology

### Web Scraping

- Used `google-play-scraper` to extract:
  - Review content
  - Rating (score)
  - Date
  - App name (bank)
- 400+ reviews collected per bank (~1200 total).
- Source: Google Play Store (country: Ethiopia, language: English).

### Preprocessing

- Removed duplicate reviews.
- Removed rows with missing values.
- Normalized date to `YYYY-MM-DD`.
- Saved cleaned dataset to `data/fintech_reviews_clean.csv` with the following columns:
  ```
  review, rating, date, bank, source
  ```

---

## How to Run

### 1. Scrape Reviews
```bash
python scraping/scraper.py
```

### 2. Clean and Preprocess Data
```bash
python preprocessing/clean_data.py
```

---

## KPIs

| Metric                         | Target       | Achieved |
|-------------------------------|--------------|----------|
| Reviews per bank              | ≥ 400        | ✅        |
| Total reviews collected       | ≥ 1200       | ✅        |
| Missing data after cleaning   | < 5%         | ✅        |
| Clean CSV available           | Yes          | ✅        |
| Organized Git with commits    | Yes          | ✅        |

---

## Git Workflow

- All development is done in the `task-1` branch.
- Frequent commits with meaningful messages.
- `.gitignore` includes:
  ```
  __pycache__/
  *.pyc
  *.pyo
  *.pyd
  .env
  venv/
  data/
  ```
