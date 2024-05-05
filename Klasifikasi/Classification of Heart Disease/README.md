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
### Visualisasi data numerik ###
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/3eecf908-6a1b-47a3-a319-502ef5f293de)

### Visualisasi data kategorik ###
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/5d782ab8-1bcd-4f50-90d0-35afa9c97239)

### Visualisasi target ###
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/f930b24b-c5f3-4fb2-a3b1-22c9ef441843)
   
Secara ilustratif, proporsi orang yang terkena penyakit jantung sebesar 52,9%, sedangkan proporsi orang yang tidak terkena penyakit jantung (normal) sebesar 47,1%. 

### Korelasi ###
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/a0503697-1d04-44a1-b44f-3a4e94edf236)

## Data Preprocessing ##
### Data Cleaning ###
```
# Mengganti nilai yang negatif dengan rata-rata
data.loc[data['oldpeak'] < 0, 'oldpeak'] = data['oldpeak'].mean()
# Mengganti nilai 'ST slope' yang sama dengan 0 dengan modus
modus_st_slope = data['ST slope'].mode()[0]
data.loc[data['ST slope'] == 0, 'ST slope'] = modus_st_slope
data.describe()
```
Data yang cleaning adalah tahapan yang penting sebelum melakukan analisis lebih lanjut. Pada tahap ini, fitur oldpeak yang memiliki nilai negatif diganti dengan rata-ratanya, sedangkan fitur ST slope yang memiliki nilai nol diganti dengan modus.

### Missing Value ###
```
# Memeriksa jumlah missing value di setiap kolom
missing_values = data.isnull().sum()
print(missing_values)
```
Pemeriksaan missing value penting dilakukan karena dapat mempengaruhi kinerja algoritma. Dari ke 11 fitur dan 1 target, tidak terdapat nilai yang hilang, sehingga dapat dilanjutkan ke tahap berikutnya.
