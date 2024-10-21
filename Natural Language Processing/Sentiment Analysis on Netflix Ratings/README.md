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
- Cleaning
- Tokenizing
- Lemmatization
- Stop words removal
- Labeling

## Exploratory Data Analysis
- Distribution of Scores:
- Proportion of Sentiment
- Word Cloud

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
| Multinomial Logistic Regression | 0.885   | 0.884     | 0.885   | 0.884    | 0.946         |
| Naive Bayes Multinomial      | 0.694    | 0.715     | 0.694   | 0.619    | 0.861         |
