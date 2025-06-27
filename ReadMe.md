# Text Analysis of News Articles

This project automates the process of extracting text from a list of URLs and analyzing it using sentiment and readability metrics. It scrapes article content, processes and cleans the text, performs sentiment scoring and readability calculations, and outputs the results in a structured CSV file.

---

## 📌 Approach to Solution

### 1. Data Loading
- Loaded input data from an Excel file (`input.xlsx`) containing a list of URLs.

### 2. Text Extraction
- Utilized `requests` and `BeautifulSoup` to fetch HTML content.
- Extracted article title and main body text, filtering out non-article content like headers and footers.

### 3. Text Processing
- Cleaned and tokenized text using `nltk`, removing punctuation and stopwords.
- Loaded positive and negative word lists from `positive-words.txt` and `negative-words.txt`.
- Calculated sentiment scores based on the occurrence of these words in the article.

### 4. Text Analysis
- Calculated:
  - **Positive Score**
  - **Negative Score**
  - **Polarity Score**
  - **Subjectivity Score**
  - **Average Sentence Length**
  - **Percentage of Complex Words**
  - **Fog Index**
  - **Word Count**
  - **Syllable Count Per Word**
  - **Personal Pronouns**
  - **Average Word Length**

### 5. Output Generation
- Saved each article’s cleaned content into the `data/` directory as individual text files (`<URL_ID>.txt`).
- Created a CSV file (`text_analysis_results.csv`) containing the analysis results for each article.

How to Run the .py File:

1. Dependencies:
   - Ensure Python 3.x is installed on your system.
   - Install required libraries:
     ```
     pip install pandas nltk requests
     ```

2. Setup:
   - Place the `input.xlsx` file in the same directory as the Python script.
   - Create directories `StopWords` and `MasterDictionary` containing necessary files (`positive-words.txt` and `negative-words.txt`).

3. Running the Script:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the Python script.
   - Execute the script:
     ```
     python main.py
     ```

   - The script will process each URL, extract article text, perform text analysis, and save results accordingly.

Dependencies:
- `pandas`: For data handling and CSV file operations.
- `nltk`: For natural language processing tasks such as tokenization and stopwords.
- `requests`: For making HTTP requests to fetch web pages.
- `BeautifulSoup`: For parsing HTML content and extracting relevant text.
