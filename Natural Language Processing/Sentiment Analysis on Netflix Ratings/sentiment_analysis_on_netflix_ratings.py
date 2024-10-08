# -*- coding: utf-8 -*-
"""Sentiment Analysis on Netflix Ratings.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gfnRCOlw_aSLbHRwyXwda1vLwnWFu84t

# **IMPORT LIBRARY**
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import string
import re

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize as word_tokenize_wrapper
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud,STOPWORDS
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('wordnet')

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc, roc_auc_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

"""# **IMPORT DATA**

## **Read Data**
"""

data = pd.read_csv("netflix_reviews.csv")
data.head()

"""## **Data Information**"""

data.info()

"""# **DATA PROCESSING**

The first step after importing data is to process the data. Data processing involves two things, i.e:
- Checking for missing values
- Checking for duplication in the data.

## **Data Cleaning**

### **Missing Value Check**

- Model Performance: Missing values can significantly affect the performance of machine learning models. In NLP, if parts of the text are missing, it could lead to **incomplete information** for **model training** and **predictions**.
- Bias: Missing data can introduce **bias**, leading to **incorrect conclusions** or **predictions**.
"""

data.isnull().sum()

data = data.dropna()
data.isnull().sum()

"""### **Duplicate Value Check**

- Redundancy: Duplicate entries can lead to redundancy, causing the model to give more importance to repeated information.
- Bias: Duplication can skew the model’s understanding of the text, leading to overfitting or biased results.
"""

data_duplicated = data.duplicated().sum()
data_duplicated

data = data.drop_duplicates()
data_duplicated = data.duplicated().sum()
data_duplicated

data.head()

data['content'].head(10)

"""# **TEXT PROCESSING**

In text processing, it is split into 6 steps sequentially, i.e:
- **Case Folding**
- **Cleaning**
- **Tokenizing**
- **Lemmatization**
- **Stop Removal**
- **Labeling**

## **Case Folding**

The first thing to do is case folding. Case folding is changing sentences that have **capital letters** into **lowercase letters**. This will have an impact on the results of the analysis.
"""

def case_folding(text):
    # Convert to lowercase
    text = text.lower()
    return text

data['content'] = data['content'].apply(case_folding)
data['content'].head(10)

"""## **Cleaning**

Then perform data cleansing by removing extra punctuation, numbers, and spaces.
"""

def cleaning(text):
    # Remove punctuation
    text = re.sub(r'[^\w\s]|[\d]|_', '', text)
    # Remove number
    text = re.sub(r'\d+', '', text)
    # Remove spacing
    text = text.strip()
    return text

data['content'] = data['content'].apply(cleaning)
data['content'].head(10)

"""## **Tokenizing**

After the data have been cleaned, each sentence's words are transformed into **tokens** according to **spaces** or **punctuation signs**.
"""

def tokenizing(text):
    # Tokenize
    tokens = word_tokenize(text)
    return tokens

data['content'] = data['content'].apply(tokenizing)
data['content'].head(10)

"""## **Lemmatization**

This process involved reducing words to their **original words** or dictionary forms (lemma).
"""

def lemmatization(text):
    # Initialize Lemmatizer
    lemmatizer = WordNetLemmatizer()
    # Lemmatize
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    return lemmatized_words

data['content'] = data['content'].apply(lemmatization)
data['content'].head(10)

"""## **Stop Words Removal**

The process of removing meaningless words, like **articles**, **prepositions**, **conjunctions**, and **other words** that often appear but are not meaningful. This is to reduce the dimensionality of the data and focus only on meaningful words.
"""

def stopword(text):
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in text if word not in stop_words]
    return filtered_words

data['content'] = data['content'].apply(stopword)
data['content'].head(10)

"""## **Labeling**

Automatic labeling of each word using the VADER Lexicon. Each word will be given a different sentiment score. In this case, each word will be categorized into 3 categories, i.e.:
- Positive, if the **compound value >= 0.05**
- Negative, if the **value -0.05 < compound < 0.05**
- Neutral, if the **compound value <= -0.05**
"""

# Initialize Vader Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment
def vader_sentiment(text):
    # Convert text to string if it's not already
    if isinstance(text, list):
        text = ' '.join(text)
    score = analyzer.polarity_scores(text)
    return score['compound']

# Function to label sentiment based on compound score
def vader_sentiment_label(compound):
    # Label sentiment
    if compound >= 0.05:
        return 'Positive'
    elif compound > -0.05 and compound < 0.05:
        return 'Neutral'
    else:
        return 'Negative'

data['vader_sentiment'] = data['content'].apply(vader_sentiment)
data['vader_sentiment_label'] = data['vader_sentiment'].apply(vader_sentiment_label)
data[['content', 'vader_sentiment', 'vader_sentiment_label']].head(10)

"""Label encoding is a process used to **convert categorical labels** into **numeric** form so that they can be fed into machine learning models. In the context of NLP and sentiment analysis, label encoding is often used to convert text labels (like "Positive," "Negative," and "Neutral") into numerical values."""

# Label Encoding
label_encoder = LabelEncoder()
data['vader_sentiment_label_encoded'] = label_encoder.fit_transform(data['vader_sentiment_label'])
data.head()

"""# **EXPLORATORY DATA ANALYSIS**

### **Distribution of Score**
"""

plt.figure(figsize=(5, 5))
sns.countplot(x="score", data=data, palette='Set3')
plt.title('Distribution of Score', fontsize=12)
plt.xlabel('Score')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

"""## **Proportion of Sentiment**

Exploring labels to find out the sentiment proportion of each category
"""

# Pie Chart
plt.figure(figsize=(8, 4))
data['vader_sentiment_label'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'salmon', 'orange'])
plt.title('Proportion of Sentiment', fontsize=12)
plt.ylabel('')
plt.tight_layout()
plt.show()

"""## **Word Cloud**

A word cloud helps in visualizing the most frequent words in the dataset. This can give an immediate sense of what the text data is about.
"""

def create_wordcloud(text, title=None):
    # Join all text elements into a single string, handling potential lists within the Series
    all_text = " ".join( " ".join(text_item) if isinstance(text_item, list) else text_item for text_item in text)
    stop_words = set(STOPWORDS.union(set(stopwords.words('english'))))
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stop_words).generate(all_text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    if title:
        plt.title(title, fontsize=20)
    plt.show()

# Create Word Clouds for each sentiment
positive_reviews = data[data['vader_sentiment_label'] == 'Positive']['content']
negative_reviews = data[data['vader_sentiment_label'] == 'Negative']['content']
neutral_reviews = data[data['vader_sentiment_label'] == 'Neutral']['content']

create_wordcloud(positive_reviews, "Positive Reviews")
create_wordcloud(negative_reviews, "Negative Reviews")
create_wordcloud(neutral_reviews, "Neutral Reviews")

"""# **FEATURE EXTRACTION**

## **CountVectorizer**

Extraction of features that **transform text** into a **matrix of token counts.** It counts the number of occurrences of each word in the document. In other words, it **converts text data** into a **numerical representation** for modeling.
"""

# Function Vectorizer
def vectorizer(text):
    # Convert text to string if it's not already
    if isinstance(text[0], list):
        text = [' '.join(doc) for doc in text]

    # Initialize CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(text)
    return X, vectorizer

X_counts, count_vectorizer = vectorizer(data['content'])

"""## **Change to TF-IDF**

It converts the **token count matrix** from CountVectorizer into **TF-IDF representation**. It not only considers the word frequency, but also how **unique** or **important** a word is in all documents.
"""

# Function to change representation to TF-IDF
def tfidf_transformer(X_counts):
    # Initialize TF-IDF Transformer
    transformer = TfidfTransformer()
    X_tfidf = transformer.fit_transform(X_counts)
    return X_tfidf

# Inisialize TF-IDF
X_tfidf = tfidf_transformer(X_counts)
print("TF-IDF Shape:", X_tfidf.shape)

"""# **SPLIT DATA**

Partitioned data into training data and testing data randomly. The training data is 80% of the total data, while the testing data is 20% of the overall data.
"""

y = data['vader_sentiment_label_encoded']
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

print(X_train.toarray()[:5])

print(X_test.toarray()[:5])

print(y_train.head())

print(y_test.head())

"""# **MODELLING**

Machine learning modeling using **Multinomial Logistic Regression** and **Multinomial Naïve Bayes** algorithms

## **Multinomial Logistic Regression**

### **Build Model**

The **Stochastic Average Gradient Descent** (sag) optimization technique is used to minimize the cost function. This technique is suitable for **large data**.

The Basic Idea:
- Calculates the probability of each class (positive, negative, and neutral) using a softmax activation function. This activation function ensures that the total probability is 1
- Model coefficients are optimized using a 'sag' optimization technique that iteratively updates by considering the average gradient of the training data
"""

# Build Model
model_mlg = LogisticRegression(multi_class='multinomial',
                               solver='sag')

"""### **Train Model**"""

# Train Model
model_mlg.fit(X_train, y_train)

# Weight (paramter model)
W = model_mlg.coef_
W

# Biases
b = model_mlg.intercept_
b

"""## **Naive Bayes Multinomial**

### **Build Model**

Multinomial Naïve Bayes algorithm is a commonly used algorithm for solving text processing cases.

Basic idea:
- The prediction of naive bayes requires that each conditional probability cannot be zero. To avoid this problem, an alpha parameter called Laplacian Smoothing/Correction can be set.
- The model learns the prior probability distribution which provides information about the parameter distribution. By setting fit_prior to True, the model will estimate the class odds from the training data.
- Similarly to alpha, force_alpha when set to True, alpha will be added when a feature does not appear in a particular class during training.
"""

# Build Model
model_nbm = MultinomialNB(alpha = 1,
                          fit_prior = True,
                          force_alpha = True)

"""### **Train Model**"""

# Train Model
model_nbm.fit(X_train, y_train)

"""# **MODEL EVALUATION**

The model was evaluated with several considerations, i.e:
- **Classification evaluation metrics**
- **AUC score**
- **Classification Report**

## **Multinomial Logistic Regression**

### **Predict**

The steps in making predictions are as follows:
- Calculate the linear combination between features and weights (parameters) added with bias.
- Using softmax activation function to get the probability of each class (positive, negative, and neutral).
- Calculating the loss function using "sag" to get the chance of class prediction.
- Update using gradient descent by iteration until converged.
"""

# Predict
y_pred_mlg = model_mlg.predict(X_test)
y_pred_mlg

"""### **Probability**"""

# Probability
y_prob_mlg = model_mlg.predict_proba(X_test)
print(y_prob_mlg)

"""### **Evaluation Metric**"""

# Evaluation Metric
print(f'Accuracy: {accuracy_score(y_test, y_pred_mlg)}')
print(f'Precision: {precision_score(y_test, y_pred_mlg, average="weighted")}')
print(f'Recall: {recall_score(y_test, y_pred_mlg, average="weighted")}')
print(f'F1-Score: {f1_score(y_test, y_pred_mlg, average="weighted")}')

"""### **Confusion Matrix**"""

# Confusion Matrix
conf_mat = confusion_matrix(y_test, y_pred_mlg)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', xticklabels=model_mlg.classes_, yticklabels=model_mlg.classes_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

"""### **ROC Score**"""

# ROC Score
mlg_roc_auc = roc_auc_score(y_test, y_prob_mlg, multi_class='ovr')
print(f'ROC AUC Score: {mlg_roc_auc}')

"""### **ROC Curve**"""

# ROC Curve
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(len(model_mlg.classes_)):
    fpr[i], tpr[i], _ = roc_curve(y_test == i, model_mlg.predict_proba(X_test)[:, i])  # Use predict_proba for multi-class
    roc_auc[i] = auc(fpr[i], tpr[i])

# Plot ROC curve
plt.figure(figsize=(8, 6))
for i in range(len(model_mlg.classes_)):
    plt.plot(fpr[i], tpr[i], label=f'Class {i} (AUC = {roc_auc[i]:.2f})')

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Multinomial Logistic Regression')
plt.legend(loc="lower right")
plt.show()

"""### **Classification Report**"""

# Classification Report
print(classification_report(y_test, y_pred_mlg))

"""## **Naive Bayes Multinomial**

### **Predict**

The steps in making predictions are as follows:
- Calculate the prior probability of each class, which is the proportion of documents in that class to the total number of documents.
- Calculate the likelihood of each features (words) based on the frequency of the word in the documents of that class.
- Calculating predictions with the class that has the highest likelihood that will be selected as the prediction class.
"""

# Predict
y_pred_nbm = model_nbm.predict(X_test)
y_pred_nbm

"""### **Probability**"""

# Probability
y_prob_nbm = model_nbm.predict_proba(X_test)
print(y_prob_nbm)

"""### **Evaluation Metric**"""

# Evaluation Metric
print(f'Accuracy: {accuracy_score(y_test, y_pred_nbm)}')
print(f'Precision: {precision_score(y_test, y_pred_nbm, average="weighted")}')
print(f'Recall: {recall_score(y_test, y_pred_nbm, average="weighted")}')
print(f'F1-Score: {f1_score(y_test, y_pred_nbm, average="weighted")}')

"""### **Confusion Matrix**"""

# Confusion Matrix
con_mat = confusion_matrix(y_test, y_pred_nbm)
plt.figure(figsize=(8, 6))
sns.heatmap(con_mat, annot=True, fmt='d', cmap='Blues', xticklabels=model_nbm.classes_, yticklabels=model_nbm.classes_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

"""### **ROC Score**"""

# ROC Score
nbm_roc_auc = roc_auc_score(y_test, y_prob_nbm, multi_class='ovr')
print(f'ROC AUC Score: {nbm_roc_auc}')

"""### **ROC Curve**"""

# ROC Curve
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(len(model_nbm.classes_)):
    fpr[i], tpr[i], _ = roc_curve(y_test == i, model_nbm.predict_proba(X_test)[:, i])  # Use predict_proba for multi-class
    roc_auc[i] = auc(fpr[i], tpr[i])

# Plot ROC Curve
plt.figure(figsize=(8, 6))
for i in range(len(model_nbm.classes_)):
    plt.plot(fpr[i], tpr[i], label=f'Class {i} (AUC = {roc_auc[i]:.2f})')

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Naive Bayes Multinomial')
plt.legend(loc="lower right")
plt.show()

"""### **Classification Report**"""

# Classification Report
print(classification_report(y_test, y_pred_nbm))

"""## **Score Comparison**"""

score_comparison = pd.DataFrame({'Model': ['Multinomial Logistic Regression', 'Naive Bayes Multinomial'],
                                'Accuracy': [accuracy_score(y_test, y_pred_mlg), accuracy_score(y_test, y_pred_nbm)],
                                'Precision': [precision_score(y_test, y_pred_mlg, average="weighted"), precision_score(y_test, y_pred_nbm, average="weighted"),],
                                'Recall': [recall_score(y_test, y_pred_mlg, average="weighted"), recall_score(y_test, y_pred_nbm, average="weighted")],
                                'F1-Score': [f1_score(y_test, y_pred_mlg, average="weighted"), f1_score(y_test, y_pred_nbm, average="weighted")],
                                'ROC AUC Score': [mlg_roc_auc, nbm_roc_auc]})
score_comparison