# Mobile Price Classification
## Overview
This project focuses on building a machine-learning model to classify mobile phones into different price ranges. The primary goal is to accurately predict the price range of a mobile phone based on its specifications. The project involves various stages including data preprocessing, exploratory data analysis (EDA), feature engineering, model building, and evaluation. Data can be accessed on the page address:

https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification

## Table of Content
1. [Project Overview](#overview)
2. [Data](#data)
3. [Data Processing](#data-processing)
4. [Exploratory Data Analysis](#exploratory-data-analysis)
5. [Feature Engineering](#feature-engineering)
6. [Modeling](#modeling)
7. [Model Evaluation](#model-evaluation)

## Data
The dataset contains the specifications of mobile phones along with their price range category. It includes the following columns:
- battery_power: Battery power in mAh
- blue: Has Bluetooth or not
- clock_speed: Speed at which microprocessor executes instructions
- dual_sim: Supports dual SIM or not
- fc: Front camera megapixels
- four_g: Has 4G or not
- int_memory: Internal memory in GB
- m_dep: Mobile depth in cm
- mobile_wt: Weight of the mobile phone
- n_cores: Number of cores in processor
- pc: Primary camera megapixels
- px_height: Pixel resolution height
- px_width: Pixel resolution width
- ram: Random access memory in MB
- sc_h: Screen height of the mobile in cm
- sc_w: Screen width of the mobile in cm
- talk_time: Longest time that a single battery charge will last when you are
- three_g: Has 3G or not
- touch_screen: Has touch screen or not
- wifi: Has wifi or not
- price_range: This is the target variable with categories from 0 (low cost) to 3 (very high cost)

## Data Processing
### Data Cleaning
- Checked for missing values
- Handled outliers

## Exploratory Data Analysis
- Distribution of Features: Visualized the distribution of key features such as battery power, RAM, and internal memory
- Correlation Matrix: Analyzed the correlation between features to identify multicollinearity
- Price Range Distribution: Visualized the distribution of the target variable (price range)

## Feature Engineering
- Normalization: Scaled numerical features to have zero mean and unit variance
- Categorical Encoding: Encoded categorical features using one-hot encoding where applicable

## Modeling
### Model
- Neural Network
- XGBoost
### Hyperparameter Tuning
- Grid Search CV

## Model Evaluation
### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score

### Results
| Model                        | Accuracy | Precision | Recall  | F1-Score | ROC AUC Score |
|------------------------------|----------|-----------|---------|----------|---------------|
| Neural Network | 0.935   | 0.935     | 0.935   | 0.934    | 0.995         |
| XGBoost      | 0.92    | 0.920     | 0.92   | 0.920    | 0.991         |
