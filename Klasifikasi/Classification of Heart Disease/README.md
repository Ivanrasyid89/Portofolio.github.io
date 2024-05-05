Data yang digunakan adalah data Classification of Heart Disease yang dapat diakses pada alamat laman: https://www.kaggle.com/datasets/mexwell/heart-disease-dataset/data?select=documentation.pdf

Data terdiri dari 11 fitur dan 1 target, dengan rincian sebagai berikut:
- Fitur 1 : Age 
- Fitur 2 : Sex
- Fitur 3 : Chest Pain Type
- Fitur 4 : Resting Blood Pressure
- Fitur 5 : Serum Cholestrol
- Fitur 6 : Fasting Blood Sugar
- Fitur 7 : Maximum Heart Rate Achieved
- Fitur 8 : Resting Electrocardiogram Results
- Fitur 9 : Exercise Induced Angina
- Fitur 10 : Oldpeak 
- Fitur 11 : ST Slope
- Target : Class

Model Machine Learning yang digunakan adalah K-Nearest Neighbors dan Support Vector Machine

# Langkah-langkah Analisis #
## Exploratory Data Analysis ##
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1190 entries, 0 to 1189
Data columns (total 12 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   age                  1190 non-null   int64  
 1   sex                  1190 non-null   int64  
 2   chest pain type      1190 non-null   int64  
 3   resting bp s         1190 non-null   int64  
 4   cholesterol          1190 non-null   int64  
 5   fasting blood sugar  1190 non-null   int64  
 6   resting ecg          1190 non-null   int64  
 7   max heart rate       1190 non-null   int64  
 8   exercise angina      1190 non-null   int64  
 9   oldpeak              1190 non-null   float64
 10  ST slope             1190 non-null   int64  
 11  target               1190 non-null   int64  
dtypes: float64(1), int64(11)
memory usage: 111.7 KB
```
