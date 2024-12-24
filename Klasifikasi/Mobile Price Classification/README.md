# Mobile Price Classification
## Overview
This project focuses on building a machine-learning model to classify mobile phones into different price ranges. The primary goal is to accurately predict the price range of a mobile phone based on its specifications. The project involves various stages including data preprocessing, exploratory data analysis (EDA), feature engineering, model building, and evaluation. Data can be accessed on the page address:

https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification

## Problem Statement
The smartphone company is highly competitive and pricing strategies play a crucial role in maximizing market share and profitability. Many customers consider price as a significant factor when purchasing a smartphone, and the ability to predict the price range of new models can guide product positioning and marketing strategies. A challenge arises in identifying how a smartphone's technical specifications (e.g., RAM, battery, processor) relate to its price range. By predicting the price range using these specifications, the company can improve targeted strategies for different market segments and offer better-priced products.

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
### Distribution of Features
![image](https://github.com/user-attachments/assets/5641bdd1-2b60-4e70-8a48-eba0e633e383)
![image](https://github.com/user-attachments/assets/86c54759-310e-4c87-b482-15dd96c65f5a)

### Correlation Matrix
![image](https://github.com/user-attachments/assets/154bc907-ec48-4a45-8c13-23dc933b4c4e)

Based on the correlation plot, we know that the correlation of each feature can impact for target (price range).

## Feature Engineering
- Normalization: Scaled numerical features to have zero mean and unit variance
- Categorical Encoding: Encoded categorical features using one-hot encoding where applicable

## Modeling
### Model
- Neural Network
- XGBoost

### Hyperparameter Tuning
- Adam Optimizer
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
| Neural Network | 0.945   | 0.945     | 0.945   | 0.944    | 0.996         |
| XGBoost      | 0.907    | 0.908     | 0.907   | 0.907    | 0.991         |

- Based on the comparison of the two accuracies of the Neural Network and XGBoost models. Neural Network accuracy is higher than XGBoost. This indicates that this model can overcome the complexity of the data.
- Pricing new product: When a company is about to launch a new product, this model can predict the price range based on its features. This will certainly help the company in making the right decision regarding the smartphone product it will launch.
- Market Segmentation:  In the product launch process, companies are required to focus on the most dominant features like “battery_power, px_height, px_width, and ram” in designing their products for different customers. In this case, the company should also consider the target customers such as the lower class, middle class, and upper class.

## Business Impact
### Optimized Pricing Strategy
- Companies can price at the upper end of the price range to maximize profits on high-end smartphones that have advanced features.
- Mid-class and low-class phones can be attractively priced based on corresponding features to target price-sensitive consumers.

### Product Development
- Companies can improve key features like “battery_power, px_height, px_width, and ram” on high-end phones to maximize profits.
- On low-class and mid-class phones, companies can increase “battery_power or ram” to differentiate themselves from high-end phones.
- Understanding the most dominant features will help avoid over-engineering the product to be launched, allowing the company to compete while ensuring production cost efficiency.

## Conclusion
The Neural Network model can be applied to predict the price range of mobile phones with an accuracy of 94.50% because its performance is excellent. The identification of dominant features can be used as a guideline in product development and costing strategies. By understanding the important features, companies can make data-driven decisions for product optimization, customer segmentation, and increasing profits.
