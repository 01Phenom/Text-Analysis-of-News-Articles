Approach to Solution:

1. Data Loading:
   - Loaded input data from an Excel file (`input.xlsx`) containing URLs to web pages.

2. Text Extraction:
   - Utilized `requests` and `BeautifulSoup` libraries to fetch and extract article text from each URL.
   - Extracted article title and main text content, ignoring headers, footers, and non-article content.

3. Text Processing:
   - Cleaned extracted text by removing punctuation and stopwords using NLTK.
   - Prepared dictionaries of positive and negative words from files (`positive-words.txt` and `negative-words.txt`).
   - Calculated sentiment scores based on occurrences of words from these dictionaries.

4. Text Analysis:
   - Computed readability metrics such as average sentence length, percentage of complex words, and Fog Index.
   - Derived additional statistics including word count, syllable count per word, personal pronouns, and average word length.

5. Output Generation:
   - Saved cleaned article text for each URL in separate text files within a `data` directory.
   - Generated a CSV file (`text_analysis_results.csv`) containing detailed analysis results for each article.

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
