# Sentiment Analysis - Netflix Review

## Overview
This project analyzes and cleans over 10.000 Netflix user reviews from the Google Play Store. Data can be accessed on the page address:

https://www.kaggle.com/datasets/ashishkumarak/netflix-reviews-playstore-daily-updated

## Problem Statement
Netflix, as a leading streaming service, receives millions of user reviews from its global customer base. These reviews offer valuable insights into user satisfaction, product performance, and areas for improvement. However, manually processing such a vast amount of textual data is inefficient and can lead to missed opportunities to address recurring issues or to improve customer experience. Therefore, Netflix needs an automated solution to categorize user feedback into actionable sentiments (positive, negative, neutral), providing a scalable way to understand customer needs and prioritize improvements.

## Table of Contents
1. [Overview](#overview)
2. [Data](#data)
3. [Data Processing](#data-processing)
4. [Text Processing](#text-processing)
5. [Exploratory Data Analysis](#exploratory-data-analysis)
6. [Feature Extraction](#feature-extraction)
7. [Modeling](#modeling)
8. [Model Evaluation](#model-evaluation)
9. [Results](#results)

## Data
The dataset contains reviews of the Netflix app from the Google Play Store. It includes the following columns:

- reviewId: Unique identifier for each review
- userName: Name of the user
- content: Review text
- score: Rating given by the user
- thumbsUpCount: Number of likes for the review
- reviewCreatedVersion: App version at the time of review
- at: Timestamp of the review
- appVersion: Current app version

## Data Processing
The data processing stage is categorized in 2 parts as follows:
### Data Cleaning
- Missing Value Checking
- Duplicate Value Checking

## Text Processing
The text processing stage is organized into 6 parts as follows
- Case folding
- Cleansing
- Tokenizing
- Stop words removal
- Lemmatization
- Labeling

## Exploratory Data Analysis
### Distribution of Scores
![image](https://github.com/user-attachments/assets/c957bdce-4753-4d2e-b1c6-3a5dec91fd0c)

The plot above is the rating of each content written by each user. It can be noticed that most of them gave a rating of 1 (very bad). This could be due to various issues that arose at the time the movie was shown.

### Proportion of Sentiment
![image](https://github.com/user-attachments/assets/3b12be98-f973-4242-8037-f8ad7d85f45a)

Based on the pie chart above, shows the proportion of sentiment distribution in the analyzed Netflix user reviews. The majority of positive reviews at 61.3% indicate overall satisfaction with the service, while the majority of negative reviews at 26.6% highlight areas of potential improvement. Neutral reviews at 12.1% provide a balanced perspective on the user experience.
- Positive reviews of 61.3% generally indicate customer satisfaction with the content, user interface, and services provided by Netflix.
- Negative reviews at 26.6% arise from app performance issues like bugs and crashes or user interface changes.
- Neutral reviews at 12.1% are neutral, which may represent users who do not have strong opinions or only report minor issues.

### Word Cloud
![image](https://github.com/user-attachments/assets/c79c39f9-539b-48f1-ad31-a249c381b1d9)
![image](https://github.com/user-attachments/assets/344214fe-1375-4af2-af1c-fe59b72042cf)
![image](https://github.com/user-attachments/assets/7b1e7257-86f8-4ab6-a202-0bf4f3808c6d)


## Feature Extraction
- CountVectorizer
- TF-IDF

## Modeling
- Multinomial Logistic Regression
- Naive Bayes Multinomial

## Model Evaluation
### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score

### Results
| Model                        | Accuracy | Precision | Recall  | F1-Score | ROC AUC Score |
|------------------------------|----------|-----------|---------|----------|---------------|
| Multinomial Logistic Regression | 0.884   | 0.882     | 0.884   | 0.882    | 0.945         |
| Naive Bayes Multinomial      | 0.692    | 0.689     | 0.692   | 0.622    | 0.860         |

- Based on the comparison of the two accuracy models of Logistic Regression and Naive Bayes. The accuracy of Logistic Regression is higher than Naive Bayes. This indicates that this model can overcome data complexity.
- With over 88% of reviews correctly classified (reliable), Netflix can trust the model output to take actions, like Improve app performance address specific issues mentioned in negative reviews, and Improve content delivery or service features based on positive and neutral feedback.
- Operational Efficiency: Netflix can process large numbers of user reviews with great confidence that the classification is correct, allowing the service team to focus on developing actionable insights in real time without having to manually read through all the reviews.

## Business Impact
### Improve Customer Satisfaction
- Quickly identify negative reviews to improve customer satisfaction with app issues, content dissatisfaction, and other technical issues.
- Improve user experience using the best model to automatically categorize reviews that can track issues, so that action can be taken to fix them.

### Enhanced Product and Service Development
- Positive reviews at 61.3% can provide insights into what customers like such as content, user interface, and more. These insights are used to develop content and features that resonate with their users.
- Negative reviews of 26.6% can identify problems to create strategies that can improve customer satisfaction and content recommendations, to provide content that matches user preferences.

## Conclusion
The model's insights provide Netflix with valuable feedback that can drive improvements in customer satisfaction, operational efficiency, content strategy, and overall user experience. By addressing common pain points highlighted in negative reviews and leveraging positive feedback to enhance product features, Netflix can retain users, reduce churn, and maintain its competitive edge in the streaming industry.
