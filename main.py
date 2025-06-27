import os
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re
import requests
from bs4 import BeautifulSoup

# Ensure you have the NLTK stopwords data
nltk.download('punkt')

# Paths to directories
stop_words_dir = 'StopWords'
master_dict_dir = 'MasterDictionary'
input_file = 'Input.xlsx'

# Load the Excel file
df = pd.read_excel(input_file)

# Load stop words
stop_words = set()
for filename in os.listdir(stop_words_dir):
    with open(os.path.join(stop_words_dir, filename), 'r', encoding='ISO-8859-1') as file:
        stop_words.update(file.read().split())

# Load positive and negative words
positive_words = set()
negative_words = set()
with open(os.path.join(master_dict_dir, 'positive-words.txt'), 'r', encoding='ISO-8859-1') as file:
    positive_words.update(file.read().split())
with open(os.path.join(master_dict_dir, 'negative-words.txt'), 'r', encoding='ISO-8859-1') as file:
    negative_words.update(file.read().split())

# Remove stop words from positive and negative words
positive_words = positive_words - stop_words
negative_words = negative_words - stop_words

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

def analyze_text(text):
    tokens = clean_text(text)
    sentences = sent_tokenize(text)

    # Sentiment Analysis
    positive_score = sum(1 for word in tokens if word in positive_words)
    negative_score = sum(1 for word in tokens if word in negative_words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(tokens) + 0.000001)

    # Readability Analysis
    avg_sentence_length = len(tokens) / len(sentences)
    complex_words = [word for word in tokens if count_syllables(word) > 2]
    percentage_complex_words = len(complex_words) / len(tokens)
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

    # Text Statistics
    word_count = len(tokens)
    syllable_count_per_word = sum(count_syllables(word) for word in tokens) / len(tokens)
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.IGNORECASE))
    avg_word_length = sum(len(word) for word in tokens) / len(tokens)

    return {
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score,
        'Average Sentence Length': avg_sentence_length,
        'Percentage of Complex Words': percentage_complex_words,
        'Fog Index': fog_index,
        'Word Count': word_count,
        'Syllable Count Per Word': syllable_count_per_word,
        'Personal Pronouns': personal_pronouns,
        'Average Word Length': avg_word_length
    }

def count_syllables(word):
    word = word.lower()
    syllable_count = len(re.findall(r'[aeiouy]', word))
    if word.endswith('es') or word.endswith('ed'):
        syllable_count = max(1, syllable_count - 1)
    return syllable_count

# Create a directory to save the extracted articles
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)

# Function to extract article text and title
def extract_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Assuming the title is within <title> tags or similar
        title = soup.find('title').get_text(strip=True)

        # Extracting article text, assuming it is within <article> tags or similar
        article_body = soup.find('article')
        if article_body:
            paragraphs = article_body.find_all('p')
            article_text = "\n".join([p.get_text(strip=True) for p in paragraphs])
        else:
            article_text = ""

        return title, article_text

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None, None

# Extract articles
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    title, article_text = extract_article(url)
    if title and article_text:
        file_path = os.path.join(output_dir, f'{url_id}.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"{title}\n\n{article_text}")
        print(f"Saved article {url_id}")

# Analyze each file in the data directory
results = []
for filename in os.listdir(output_dir):
    with open(os.path.join(output_dir, filename), 'r', encoding='utf-8') as file:
        text = file.read()
        analysis = analyze_text(text)
        analysis['URL_ID'] = filename.split('.')[0]
        results.append(analysis)

# Save results to a CSV file
df_results = pd.DataFrame(results)
df_results.to_csv('text_analysis_results.csv', index=False)

print("Analysis completed and results saved to text_analysis_results.csv")
