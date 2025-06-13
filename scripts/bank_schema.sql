-- Table: banks
CREATE TABLE banks (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(100) NOT NULL UNIQUE
);

-- Table: reviews
CREATE TABLE reviews (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    review CLOB,
    rating NUMBER,
    review_date DATE,
    bank_id NUMBER,
    source VARCHAR2(50),
    sentiment VARCHAR2(50),
    sentiment_score FLOAT,
    FOREIGN KEY (bank_id) REFERENCES banks(id)
);
