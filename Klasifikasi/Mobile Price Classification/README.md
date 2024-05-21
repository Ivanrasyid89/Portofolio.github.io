Data yang digunakan adalah data Mobile Price Classification yang dapat diakses pada alamat laman:
https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification

Data terdiri dari 20 fitur dan 1 target, dengan rincian sebagai berikut:
1. Fitur 1 : Battery Power (Numerik)
2. Fitur 2 : Bluetooth (Kategorik)
3. Fitur 3 : Clock Speed (Numerik)
4. Fitur 4 : Dual Sim (Kategorik)
5. Fitur 5 : Front Camera MP (Numerik)
6. Fitur 6 : Four_g (Kategorik)
7. Fitur 7 : Internal Memory (Numerik)
8. Fitur 8 : Mobile Depth (Numerik)
9. Fitur 9 : Mobile Weight (Numerik)
10. Fitur 10 : Number Cores (Numerik)
11. Fitur 11 : Primary Camera MP (Numerik)
12. Fitur 12 : Pixel Resolution Height (Numerik)
13. Fitur 13 : Pixel Resolution Weight (Numerik)
14. Fitur 14 : RAM (Numerik)
15. Fitur 15 : Screen Height (Numerik)
16. Fitur 16 : Screen Width (Numerik)
17. Fitur 17 : Talk Time (Numerik)
18. Fitur 18 : Three_g (Kategorik)
19. Fitur 19 : Touch Screen (Kategorik)
20. Fitur 20 : WIFI (Kategorik)
21. Target : Price Range (Kategorik)

Model Machine Learning yang digunakan adalah Neural Network dan Extreme Gradient Boosting 

# Langkah-langkah Analisis #
## Exploratory Data Analysis ##
### Visualisasi Data Numerik ###
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/e9218f10-625c-48e8-b18f-c44a03a1649a)

### Visualisasi Data Kategorik ###
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/5e6eb663-ed3c-4f7e-aeca-b3db596f7496)

### Korelasi ###
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/df30e8d6-d927-4e36-842c-09899cf12d73)

## Data Preprocessing ##
### Standardize ###
#### Standarisasi Data ####
```
## Standarisasi data (mean = 0 dan st.dev = 1) ##
# Mendefinisikan fungsi scale data
def scale_data(data_train):
    # Membuat salinan data
    scaled_data_train = data_train.copy()
    # Fitur numerik yang diskalakan
    fitur_numerik = ['battery_power', 'clock_speed', 'fc', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'talk_time']
    # Melakukan standarisasi
    scaler = StandardScaler()
    # Mengubah skala nilai
    scaled_data_train[fitur_numerik] = scaler.fit_transform(scaled_data_train[fitur_numerik])
    return scaled_data_train
# Menampilkan data hasil standarisasi
scaled_data_train = scale_data(data_train)
print(scaled_data_train)
```
Melakukan standarisasi data agar setiap fitur memiliki satuan yang sama.
### Feature Engineering ###
#### Feature Engineering dan Konversi Data ####
```
# Pembuatan kolom fitur untuk masing masing kolom numerik dan kategorik
kolom_fitur = []

# Fitur Numerik:
fitur_numerik = ['battery_power', 'clock_speed', 'fc', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'talk_time']

for col in fitur_numerik:
  kolom_fitur_numerik = tf.feature_column.numeric_column(col)
  kolom_fitur.append(kolom_fitur_numerik)

# Fitur Kategorik:
fitur_kategorik = ['blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi']

for col in fitur_kategorik:
    kolom_fitur_kategorik = tf.feature_column.categorical_column_with_vocabulary_list(
        key=col,
        vocabulary_list=scaled_data_train[col].unique().tolist()
    )
    kolom_fitur_kategorik_onehot = tf.feature_column.indicator_column(kolom_fitur_kategorik)
    kolom_fitur.append(kolom_fitur_kategorik_onehot)

# Pembuatan lapisan fitur sebagai input untuk model NN
feature_layer = tf.keras.layers.DenseFeatures(kolom_fitur)

# Konversi dataframe ke dataset Tensorflow
def data_to_dataset(dataframe, shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop('price_range')
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe),labels))

  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))

  ds = ds.batch(batch_size=batch_size)

  return ds
```
Sebelum melakukan pemodelan NN, data dikonversi terlebih dahulu ke dataset TensorFlow agar bisa dilakukan pembentukan arsitektur NN.
### Split Data ###
#### Partisi Data model NN ####
```
## Partisi Data untuk model NN ##
train, test = train_test_split(scaled_data_train, test_size=0.2, random_state=42)
```
Partisi data menjadi data training dan data testing untuk pembentukan model NN.
```
# Konversi dataframe train dan test ke dataset tfds
train_ds = data_to_dataset(train, shuffle = True, batch_size=32)
test_ds = data_to_dataset(test, shuffle=False, batch_size=32)
```
Konversi data ke dalam TensorFlow Dataset (TFDS) untuk pembentukan model NN menggunakan TensorFlow.
#### Partisi Data Model XGBOOST ####
```
## Split data ke dalam fitur (X) dan target (Y) ##
# Fitur X
X = scale_data(data_train.drop('price_range', axis=1))
# Target Y
y = scaled_data_train['price_range']
```
Sebelum melakukan analisis, data dipecah terlebih dahulu menjadi dua bagian, yaitu fitur (X) dan target (Y).
```
## Partisi data ##
# Partisi data ke dalam data latih (80%) dan data uji (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
# Menampilkan dimensi data
print(f"X_train : {X_train.shape}")
print(f"X_test : {X_test.shape}")
print(f"y_train : {y_train.shape}")
print(f"y_test : {y_test.shape}")
```
Data dipartisi menjadi data training dan data testing secara random. Data training sebanyak 80% dari data keseluruhan, sedangkan data testing sebanyak 20% dari data keseluruhan.

- X_train menunjukkan fitur-fitur yang digunakan untuk melatih model (1600 baris dan 20 kolom).
- X_test menunjukkan fitur-fitur yang digunakan untuk menguji model (400 baris dan 20 kolom).
- y_train menunjukkan target yang digunakan untuk melatih model (1600 baris).
- y_test menunjukkan target yang digunakan untuk menguji model (20 kolom).

Keempat komponen tersebut harus ada sebelum melakukan pemodelan.

## MODELLING ##
### NEURAL NETWORK ###
```
## Membangun Model NN ##
model = tf.keras.Sequential([
    feature_layer,
    tf.keras.layers.Dense(units=512, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(units=256, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(units=128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    tf.keras.layers.Dense(units=64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    tf.keras.layers.Dense(units=4, activation='softmax')  # 4 kelas untuk 'price_range'
])
```
Membuat model Seq dari framework Keras dan menambahkan lapisan fitur yang berisikan kolom numerik dan kategorik yang telah distandarisasi sebelumnya. Menambahkan lapisan Dense (Fully Connected) yang terdiri dari 512, 256, 128, dan 64 neuron dengan fungsi aktivasinya relu. Menambahkan lapisan dropout dengan peluang dropout sebesar 50%. Dropout digunakan untuk mencegah overfitting dengan secara acak menonaktifkan setengah dari neuron di lapisan selama pelatihan berlangsung. Pada lapisan Dense dengan neuron 128 dan 64, ditambahkan regularisasi L2 dengan faktor regulasi sebesar 0.01 untuk mencegah overfitting dengan menambahkan penalti terhadap bobot besar. Menambahkan lapisan output dense dengan 4 unit neuron (kelas target 'price_range') dan fungsi aktivasi softmax. Fungsi aktivasi softmax digunakan untuk klasifikasi multi-kelas, mengubah output menjadi peluang kelas.
```
# Kompilasi Model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```
Mengompilasi model menggunakan optimizer Adam dengan laju pembelajaran sebesar 0.001. Menggunakan fungsi loss sparse_categorical_crossentropy, yang cocok untuk klasifikasi multi-kelas dengan target diskrit. Menggunakan metrik evaluasi akurasi selama pelatihan dan evaluasi model.
```
# Latih model
history = model.fit(train_ds, validation_data=test_ds, epochs=20)
```
Melakukan training model menggunakan train_ds dan dataset validasi (test_ds) dengan jumlah iterasi sebanyak 20.

### XGBOOST ###
```
model_xgb = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
param_grid = {
    'learning_rate': [0.1, 0.01, 0.001],
    # Kedalaman tiap pohon
    'max_depth': [3, 5, 7],
    # Jumlah pohon keputusan
    'n_estimator': [100, 200, 300],
    # Banyak sampel dalam proses boosting
    'subsample': [0.6, 0.8, 1.0],
    # Jumlah minimum sampel
    'min_child_weight': [1, 3, 5]
}
```
Membangun model model klasifikasi menggunakan algoritma XGBoost dengan metrik evaluasi yang digunakan adalah mlogloss (multiclass log loss), yang digunakan untuk mengevaluasi performa model klasifikasi multi-kelas. Learning rate mengontrol seberapa besar langkah yang diambil model saat mengoptimalkan bobot. Max depth adalah kedalaman maksimum tiap pohon keputusan. Semakin dalam pohon, semakin kompleks model, namun juga lebih rentan terhadap overfitting. n estimator adalah jumlah pohon keputusan yang akan digunakan dalam model. Semakin banyak pohon, semakin baik performa model, hingga titik tertentu. Subsampel adalah proporsi sampel yang digunakan untuk melatih setiap pohon. Menggunakan subset data dapat membantu mengurangi overfitting. Min child weight adalah jumlah minimum sampel yang diperlukan dalam satu leaf node. Nilai yang lebih tinggi dapat membuat model lebih konservatif.
```
# GridSearchCV untuk menemukan parameter optimal
grid_search = GridSearchCV(model_xgb, param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)
```
Mendefinisikan grid parameter yang akan digunakan untuk mencari kombinasi parameter terbaik menggunakan teknik GridSearchCV. Banyaknya lipatan (fold) yang ditetapkan sebanyak 5 untuk mempercepat proses komputasi. Menghitung performa model untuk setiap kombinasi parameter berdasarkan cross-validation. Kombinasi parameter yang optimal akan dipilih untuk pemodelan XGBOOST.
```
# Kombinasi parameter optimal
best_xgb = grid_search.best_estimator_

# Menampilkan parameter optimal
print('Kombinasi parameter optimal:', grid_search.best_params_)
```
Mendapatkan model dengan parameter terbaik dari hasil pencarian grid. Dalam hal ini, kombinasi parameter optimal adalah {'learning_rate': 0.1, 'max_depth': 5, 'min_child_weight': 3, 'n_estimator': 100, 'subsample': 0.6}

## Model Evaluation ##
### NEURAL NETWORK ###
#### Menampilkan akurasi dari proses pelatihan model NN ####
```
# Menghitung metrik evaluasi: akurasi, presisi, recall, dan F1 score
accuracy_nn = accuracy_score(y_test, y_pred_nn)
precision_nn = precision_score(y_test, y_pred_nn, average='weighted')
recall_nn = recall_score(y_test, y_pred_nn, average='weighted')
f1_nn = f1_score(y_test, y_pred_nn, average='weighted')
# Menampilkan metrik evaluasi
print("Accuracy:", accuracy_nn)
print("Precision:", precision_nn)
print("Recall:", recall_nn)
print("F1 Score:", f1_nn)
```
Metrik evaluasi yang digunakan untuk tugas klasifikasi adalah Akurasi, Presisi, Recall, dan F1-Score.

- Akurasi : 93,5%. Model NN mampu membuat prediksi yang benar (kelas positif dan kelas negatif) dari total prediksi yang dilakukan, yaitu sebesar 93,5%. Semakin besar akurasi, maka semakin baik model yang digunakan untuk melakukan tugas klasifikasi.
- Presisi : 93,53%. Model NN mampu membuat prediksi yang benar bagi kelas positif dari total prediksi positif yang dilakukan, yaitu sebesar 93,53%. Semakin besar presisi, maka semakin baik model mengidentifikasi kelas positif tanpa salah mengidentifikasi kelas negatif sebagai kelas positif.
- Recall : 93,5%. Model NN mampu membuat prediksi yang benar bagi kelas positif, yaitu sebesar 93,5%.
- F1-score : 93,47%. Model NN mampu mengklasifikasi kelas positif dan negatif dengan benar (seimbang), yaitu sebesar 93,47%.

#### Menampilkan Confussion Matriks ####
```
# Confusion Matrix
cm_nn = confusion_matrix(y_test, y_pred_nn)
print("Confusion Matrix NN:")
print(cm_nn)
```
Kelas 0 (Low Cost):
- Sebanyak 105 sampel diklasifikasikan dengan benar sebagai kelas 0
- Tidak ada sampel pada kelas 0 yang diklasifikasikan sebagai kelas 1, kelas 2 dan kelas 3

Kelas 1 (Medium Cost):
- Sebanyak 6 sampel kelas 1, diklasifikasikan sebagai kelas 0
- Sebanyak 81 sampel diklasifikasikan dengan benar sebagai kelas 1
- Sebanyak 4 sampel kelas 1, diklasifikasikan sebagai kelas 2
- Tidak ada sampel pada kelas 1 yang diklasifikasikan sebagai kelas 3

Kelas 2 (High Cost):
- Tidak ada sampel pada kelas 2 yang diklasifikasikan sebagai kelas 0
- Sebanyak 5 sampel kelas 2, diklasifikasikan sebagai kelas 1
- Sebanyak 83 sampel diklasifikasikan dengan benar sebagai kelas 2
- Sebanyak 4 sampel kelas 2, diklasifikasikan sebagai kelas 3

Kelas 3 (Very High Cost):
- Tidak ada sampel pada kelas 3 yang diklasifikasikan sebagai kelas 0 dan kelas 1
- Sebanyak 7 sampel kelas 2, diklasifikasikan sebagai kelas 3
- Sebanyak 105 sampel diklasifikasikan dengan benar sebagai kelas 3

#### Kurva ROC ####

![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/01c96e9d-5a80-4ff3-bce5-e6a7cd6c6d6d)

Model Neural Network (NN) menunjukkan kinerja yang sangat baik dengan nilai AUC yang sangat tinggi untuk semua kelas (mendekati atau sama dengan 1.00).

### XGBOOST ###
Menampilkan akurasi dari proses pelatihan model XGBOOST.
```
## Mengevaluasi model XGBOOST ##
# Menguji model menggunakan data uji (X_test)
y_pred_xgb = best_xgb.predict(X_test)
# Menghitung metrik evaluasi: akurasi, presisi, recall, dan F1 score
accuracy = accuracy_score(y_test, y_pred_xgb)
precision = precision_score(y_test, y_pred_xgb, average='weighted')
recall = recall_score(y_test, y_pred_xgb, average='weighted')
f1 = f1_score(y_test, y_pred_xgb, average='weighted')
# Menampilkan metrik evaluasi
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
```
Metrik evaluasi yang digunakan untuk tugas klasifikasi adalah Akurasi, Presisi, Recall, dan F1-Score.

- Akurasi : 92%. Model XGBOOST mampu membuat prediksi yang benar (kelas positif dan kelas negatif) dari total prediksi yang dilakukan, yaitu sebesar 92%. Semakin besar akurasi, maka semakin baik model yang digunakan untuk melakukan tugas klasifikasi.
- Presisi : 92,05%. Model XGBOOST mampu membuat prediksi yang benar bagi kelas positif dari total prediksi positif yang dilakukan, yaitu sebesar 92,05%. Semakin besar presisi, maka semakin baik model mengidentifikasi kelas positif tanpa salah mengidentifikasi kelas negatif sebagai kelas positif.
- Recall : 92%. Model XGBOOST mampu membuat prediksi yang benar bagi kelas positif, yaitu sebesar 92%.
- F1-score : 92%. Model XGBOOST mampu mengklasifikasi kelas positif dan negatif dengan benar (seimbang), yaitu sebesar 92%.

#### Menampilkan Confussion Matriks ####
```
# Confusion Matrix
cm_xgb = confusion_matrix(y_test, y_pred_xgb)
print("Confusion Matrix XGBOOST:")
print(cm_xgb)
```
Kelas 0 (Low Cost):
- Sebanyak 101 sampel diklasifikasikan dengan benar sebagai kelas 0
- Sebanyak 4 sampel kelas 0, diklasifikasikan sebagai kelas 1
- Tidak ada sampel pada kelas 0 yang diklasifikasikan sebagai kelas 2 dan kelas 3

Kelas 1 (Medium Cost):
- Sebanyak 3 sampel kelas 1, diklasifikasikan sebagai kelas 0
- Sebanyak 86 sampel diklasifikasikan dengan benar sebagai kelas 1
- Sebanyak 2 sampel kelas 1, diklasifikasikan sebagai kelas 2
- Tidak ada sampel pada kelas 1 yang diklasifikasikan sebagai kelas 3

Kelas 2 (High Cost):
- Tidak ada sampel pada kelas 2 yang diklasifikasikan sebagai kelas 0
- Sebanyak 5 sampel kelas 2, diklasifikasikan sebagai kelas 1
- Sebanyak 80 sampel diklasifikasikan dengan benar sebagai kelas 2
- Sebanyak 7 sampel kelas 2, diklasifikasikan sebagai kelas 3

Kelas 3 (Very High Cost):
- Tidak ada sampel pada kelas 3 yang diklasifikasikan sebagai kelas 0 dan kelas 1
- Sebanyak 11 sampel kelas 2, diklasifikasikan sebagai kelas 3
- Sebanyak 101 sampel diklasifikasikan dengan benar sebagai kelas 3

#### Kurva ROC ####

![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/3cf3467f-00d9-4a59-8625-c0197ac7ea50)

Model XGBoost juga menunjukkan kinerja yang sangat baik dengan nilai AUC yang tinggi, meskipun sedikit lebih rendah dibandingkan dengan model NN untuk kelas 2.

## PREDICTION ##
### Membaca Data Testing ###
```
data_testing = pd.read_csv("test.csv")
```
### Data Preprocessing ###
#### Standarisasi Data ####
```
## Standarisasi data (mean = 0 dan st.dev = 1) ##
# Mendefinisikan fungsi scale data
def scale_data(data_testing):
    # Membuat salinan data
    scaled_data_testing = data_testing.copy()
    # Fitur numerik yang diskalakan
    fitur_numerik = ['battery_power', 'clock_speed', 'fc', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'talk_time']
    # Melakukan standarisasi
    scaler = StandardScaler()
    # Mengubah skala nilai
    scaled_data_testing[fitur_numerik] = scaler.fit_transform(scaled_data_testing[fitur_numerik])
    return scaled_data_testing
# Menampilkan data hasil standarisasi
scaled_data_testing = scale_data(data_testing)
print(scaled_data_testing)
```
Melakukan standarisasi data numerik pada data testing agar memiliki satuan yang sama 
### NEURAL NETWORK ###
#### Konversi Dataframe ke Dataset TensorFlow ####
```
# Mengonversi dataframe ke dataset TensorFlow
def data_to_dataset(dataframe, batch_size=32):
    dataframe = dataframe.copy()
    ds = tf.data.Dataset.from_tensor_slices(dict(dataframe))
    ds = ds.batch(batch_size)
    return ds

test_ds = data_to_dataset(scaled_data_testing)
```
#### Melakukan Prediksi ####
```
# Prediksi menggunakan model NN
y_pred_probs_nn = model.predict(test_ds)
y_pred_nn = tf.argmax(y_pred_probs_nn, axis=1).numpy()

# Menampilkan prediksi
print("Prediksi NN:")
print(y_pred_nn)
```
### XGBOOST ###
#### Kolom yang digunakan ####
```
data_predict = scaled_data_testing[['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi']]

data_predict.head()
```
Data yang digunakan adalah data yang telah distandarisasi sebelumnya
#### Melakukan Prediksi ####
```
# Prediksi menggunakan model XGBoost
y_pred_xgb = best_xgb.predict(data_predict)

# Menampilkan prediksi
print("Prediksi XGBoost:")
print(y_pred_xgb)
```

## KESIMPULAN ##
Berdasarkan hasil evaluasi model di atas, model Neural Network (NN) menunjukkan kinerja yang sangat baik dengan akurasi keseluruhan 93,5%. Nilai precision, recall, dan f1-score untuk setiap kelas juga tinggi, menunjukkan bahwa model memiliki kinerja yang baik dalam mengklasifikasikan sampel ke dalam kelas yang benar. Oleh sebab itu, model NN lebih cocok digunakan untuk melakukan prediksi pada data baru. 
