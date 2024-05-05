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

### Standarisasi ###
```
## Standarisasi data (mean = 0 dan st.dev = 1) ##
# Mendefinisikan fungsi scale data
def scale_data(data):
    # Membuat salinan data
    scaled_data = data.copy()
    # Fitur numerik yang akan diskalakan
    fitur_numerik = ['age', 'resting bp s', 'cholesterol', 'max heart rate', 'oldpeak']
    # Looping for untuk iterasi setiap fitur numerik
    for feature in fitur_numerik:
        # Menghitung rata-rata dari fitur
        mean = np.mean(data[feature])
        # Menghitung standar deviasi dari fitur
        std_dev = np.std(data[feature])
        # Standarisasi nilai pada fitur
        scaled_data[feature] = (data[feature] - mean) / std_dev
    # Mengembalikan nilai ke scaled data
    return scaled_data
# Menampilkan data hasil standarisasi
scaled_data = scale_data(data)
print(scaled_data)
```
Melakukan transformasi pada setiap data numerik sehingga hasil transformasi memiliki nilai tengah 0 dan simpangan baku 1. Hal ini bertujuan untuk menyeragamkan skala data yang digunakan.

### Split Data ###
```
## Split data ke dalam fitur (X) dan target (Y) ##
# Fitur X
X = scale_data(data.drop('target', axis=1))
# Target Y
y = scaled_data['target']
```
Sebelum melakukan analisis, data dipecah terlebih dahulu menjadi dua bagian, yaitu fitur (X) dan target (Y).

### Partisi Data ###
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
- X_train menunjukkan fitur-fitur yang digunakan untuk melatih model (952 baris dan 11 kolom)
- X_test menunjukkan fitur-fitur yang digunakan untuk menguji model (238 baris dan 11 kolom)
- y_train menunjukkan target yang digunakan untuk melatih model (952 baris)
- y_test menunjukkan target yang digunakan untuk menguji model (238 kolom)

Keempat komponen tersebut harus ada sebelum melakukan pemodelan.

## Modelling ##
### Algoritma K-NN ###
#### Menentukan banyaknya k (tetangga) ####
```
## Menentukan nilai k menggunakan akar dari banyaknya observasi ##
# Fungsi untuk menghitung nilai k
def hitung_k(data):
    # Menghitung jumlah observasi dalam data training
    n = len(X_train)
    # Menentukan nilai k dengan mengambil akar dari jumlah observasi
    k = int(np.sqrt(n))
    return k
# Mendefinisikan data
data = [X_train]
# Menghitung k
k = hitung_k(data)
# Menampilkan k
print("Nilai k yang ditentukan:", k)
```
Salah satu cara untuk menentukan banyaknya tetangga adalah akar dari banyaknya observasi data training. Dalam hal ini, banyaknya k yang digunakan adalah sebanyak 30.

#### Melatih model K-NN ####
```
## Membangun model KNN ##
# Membuat model KNN menggunakan k optimal dan jarak euclidean
model_knn = KNeighborsClassifier(n_neighbors = k, weights='uniform', algorithm='auto', metric='euclidean')
# Melatih model KNN menggunakan data latih
model_knn.fit(X_train, y_train)
```
Dalam membangun model K-NN, jarak yang digunakan untuk mengukur kedekatan titik data baru dengan tetangga adalah jarak Euclidean.

### Algoritma SVM ###
#### Melatih Model SVM ####
```
## Membangun model SVM ##
# Membuat model SVM
modelsvm = SVC()
# Melakukan tuning parameter
param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto'],
    'degree': [2, 3, 4]
}
grid_search = GridSearchCV(modelsvm, param_grid, cv=5)
# Menemukan kombinasi parameter optimal
grid_search.fit(X_train, y_train)
# Kombinasi parameter optimal
best_svm = grid_search.best_estimator_
# Menampilkan parameter optimal
print('Kombinasi parameter optimal:',  grid_search.best_params_)
```
Sebelum melatih model SVM, perlu ditetapkan terlebih dahulu ruang pencarian parameter internal dan fungsi kernel.

#### Tuning parameter ####
```
## Tuning parameter ##
# Inisialisasi daftar parameter yang akan diuji
nilai_C = [0.1, 1, 10, 100]
fungsi_kernel = ['linear', 'rbf', 'poly']
nilai_gamma = ['scale', 'auto']
derajat_poly = [2, 3, 4]

# Inisialisasi variabel untuk menyimpan parameter terbaik dan akurasi terbaik
best_params = {}
best_accuracy = 0.0

# Inisialisasi objek KFold untuk validasi silang
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Inisialisasi variabel untuk menyimpan akurasi dari setiap iterasi
all_accuracies = []

# Melakukan iterasi untuk setiap kombinasi parameter
for C in nilai_C:
    for kernel in fungsi_kernel:
        for gamma in nilai_gamma:
            for degree in derajat_poly:
                # Inisialisasi model SVM dengan parameter tertentu
                modelsvm = SVC(C=C, kernel=kernel, gamma=gamma, degree=degree)
                # Menyimpan akurasi
                accuracies = []
                # Melakukan validasi silang
                for train_index, val_index in kf.split(X_train):
                    X_train_fold, X_val_fold = X_train.iloc[train_index], X_train.iloc[val_index]
                    y_train_fold, y_val_fold = y_train.iloc[train_index], y_train.iloc[val_index]
                    # Melatih model pada setiap lipatan
                    modelsvm.fit(X_train_fold, y_train_fold)
                    # Mengukur akurasi pada setiap lipatan
                    y_pred_fold = modelsvm.predict(X_val_fold)
                    accuracy_fold = accuracy_score(y_val_fold, y_pred_fold)
                    accuracies.append(accuracy_fold)
                # Menghitung rata-rata akurasi dari semua lipatan
                mean_accuracy = np.mean(accuracies)
                # Memeriksa apakah akurasi yang dihasilkan lebih baik dari yang sebelumnya
                if mean_accuracy > best_accuracy:
                    best_accuracy = mean_accuracy
                    best_params = {'C': C, 'kernel': kernel, 'gamma': gamma, 'degree': degree}
                # Menyimpan akurasi dari setiap iterasi
                all_accuracies.append({'C': C, 'kernel': kernel, 'gamma': gamma, 'degree': degree, 'accuracy': mean_accuracy})

# Menampilkan parameter terbaik
print('Kombinasi parameter optimal:', best_params)

# Menampilkan akurasi dari setiap iterasi
print("Akurasi dari setiap iterasi:")
for i, acc in enumerate(all_accuracies, 1):
    print(f"Iterasi {i}: C={acc['C']}, kernel={acc['kernel']}, gamma={acc['gamma']}, degree={acc['degree']}, Accuracy={acc['accuracy']}")
```
Salah satu teknik yang digunakan untuk menemukan kombinasi parameter optimal adalah Grid Search dengan pendekatan Cross Validation. Dalam hal ini, cross validation menggunakan lipatan (fold) sebanyak 5 untuk mempercepat proses komputasi. Cara kerja Grid Search CV ini adalah membagi data training ke dalam lipatan-lipatan dengan ukuran yang sama besar, setiap lipatan terdiri atas data training dan data testing, kemudian Grid Search berusaha mencoba keseluruhan kombinasi parameter dalam rentang yang telah ditentukan, kombinasi parameter tersebut dievaluasi menggunakan CV, kemudian dihitung akurasinya. Hal ini dilakukan dengan cara yang sama, di mana setiap kombinasi parameter yang telah dicoba, dihitung rata-rata akurasinya dari setiap lipatan. Kemudian melakukan iterasi kombinasi parameter lainnya, hingga diperoleh rata-rata akurasi yang paling besar. Adapun kombinasi parameter optimal terletak pada iterasi ke-46 dengan nilai akurasi sebesar 87,07%.

## Model Evaluation ##
### Algoritma K-NN ###
#### Menghitung metriks evaluasi ####
```
## Menghitung metrik evaluasi ##
# Menghitung jumlah prediksi yang benar
prediksi_benar = np.sum(y_pred_knn == y_test)
# Menghitung total jumlah prediksi
total_prediksi = len(y_test)
# Menghitung akurasi
accuracy = prediksi_benar / total_prediksi

# Menghitung TP, FN, TN, dan FN
# Menghitung jumlah positif benar
TP = np.sum((y_pred_knn == 1) & (y_test == 1))
# Menghitung jumlah positif salah
FP = np.sum((y_pred_knn == 1) & (y_test == 0))
# Menghitung jumlah negatif benar
TN = np.sum((y_pred_knn == 0) & (y_test == 0))
# Menghitung jumlah negatif salah
FN = np.sum((y_pred_knn == 0) & (y_test == 1))

# Menghitung presisi, recall, dan F1 score
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * (precision * recall) / (precision + recall)

# Menampilkan metrik evaluasi
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
```
Metrik evaluasi yang digunakan untuk tugas klasifikasi adalah Akurasi, Presisi, Recall, dan F1-Score.
- Akurasi : 84,03%. Model K-NN mampu membuat prediksi yang benar (kelas positif dan kelas negatif) dari total prediksi yang dilakukan, yaitu sebesar 84,03%. Semakin besar akurasi, maka semakin baik model yang digunakan untuk melakukan tugas klasifikasi.
- Presisi : 86,04%. Model K-NN mampu membuat prediksi yang benar bagi kelas positif dari total prediksi positif yang dilakukan, yaitu sebesar 86,04%. Semakin besar presisi, maka semakin baik model mengidentifikasi kelas positif tanpa salah mengidentifikasi kelas negatif sebagai kelas positif.
- Recall : 84,73%. Model K-NN mampu membuat prediksi yang benar bagi kelas positif, yaitu sebesar 84,73%.
- F1-score : 85,38%. Model K-NN mampu mengklasifikasi kelas positif dan negatif dengan benar (seimbang), yaitu sebesar 85,38%. 

#### Kurva ROC ####
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/c61baf0b-9c8b-434e-b2ea-5df7cbd182f3)

Kurva ROC menunjukkan kinerja algoritma dalam mengklasifikasikan dengan ambang batas keputusan yang berbeda. Plot antara True Positif dan False Positif, sedangkan skor ROC merangkum kinerja algortima di setiap ambang batas keputusan. Dalam hal ini, skor ROC model K-NN sebesar 83,96%, semakin tinggi skor ROC maka semakin baik algoritma mampu membedakan kelas positif dan negatif.

### Algoritma SVM ###
#### Menghitung metrik evaluasi ####
```
## Mengevaluasi model SVM ##
# Menguji model menggunakan data uji (X_test)
y_pred_svm = best_svm.predict(X_test)
# Menghitung metrik evaluasi: akurasi, presisi, recall, dan F1 score
accuracy = accuracy_score(y_test, y_pred_svm)
precision = precision_score(y_test, y_pred_svm)
recall = recall_score(y_test, y_pred_svm)
f1 = f1_score(y_test, y_pred_svm)
# Menampilkan metrik evaluasi
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
```
- Akurasi : 89,07%. Model SVM mampu membuat prediksi yang benar (kelas positif dan kelas negatif) dari total prediksi yang dilakukan, yaitu sebesar 89,07%. Semakin besar akurasi, maka semakin baik model yang digunakan untuk melakukan tugas klasifikasi.
- Presisi : 87,23%. Model SVM mampu membuat prediksi yang benar bagi kelas positif dari total prediksi positif yang dilakukan, yaitu sebesar 87,23%. Semakin besar presisi, maka semakin baik model mengidentifikasi kelas positif tanpa salah mengidentifikasi kelas negatif sebagai kelas positif.
- Recall : 93,89%. Model SVM mampu membuat prediksi yang benar bagi kelas positif, yaitu sebesar 93,89%.
- F1-score : 90,44%. Model SVM mampu mengklasifikasi kelas positif dan negatif dengan benar (seimbang), yaitu sebesar 90,44%. 

#### Kurva ROC ####
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/77c81e46-1788-4a4d-8427-2553510230d5)

Kurva ROC menunjukkan kinerja algoritma dalam mengklasifikasikan dengan ambang batas keputusan yang berbeda. Plot antara True Positif dan False Positif, sedangkan skor ROC merangkum kinerja algortima di setiap ambang batas keputusan. Dalam hal ini, skor ROC model SVM sebesar 88,54%, semakin tinggi skor ROC maka semakin baik algoritma mampu membedakan kelas positif dan negatif.

## Prediction ##
### Algoritma K-NN ###
```
# Membuat data baru dalam bentuk array
data_baru = np.array([[40, 1, 1, 140, 237, 1, 0, 150, 1, 1.0, 2]])
# 1. Memilih banyaknya tetangga (k = 30)
k = k
# 2. Menghitung jarak titik data baru dengan data lama (X_train) menggunakan jarak Euclidean
jarak_euclidean = np.sqrt(np.sum((X_train - data_baru) ** 2, axis=1))
# 3. Mengambil k terdekat
indeks_terdekat = np.argsort(jarak_euclidean)[:k]
# 4. Menghtung jumlah titik data dalam setiap kategori di antara 30 tetangga terdekat
jumlah_kelas_0 = np.sum(y_train.iloc[indeks_terdekat] == 0)
jumlah_kelas_1 = np.sum(y_train.iloc[indeks_terdekat] == 1)
# 5. Menetapkan data baru ke dalam kategori yang memiliki jumlah tetangga terbanyak
hasil_prediksi = 1 if jumlah_kelas_1 > jumlah_kelas_0 else 0
# Cetak hasil prediksi
if hasil_prediksi == 0:
    print("Hasil Prediksi : Normal")
else:
    print("Hasil Prediksi : Penyakit Jantung")
```
Dengan menggunakan k = 30 dan jarak euclidean, algoritma K-NN mengklasifikasikan data baru ke dalam kelas "Penyakit Jantung".

### Algoritma SVM ###
```
# Mendefinisikan fungsi untuk menghitung nilai kernel antara fitur dan terget
def fungsi_kernel(X, Y):
    if kernel == 'rbf':
        # Rumus fungsi kernel RBF
        return np.exp(-gamma * np.linalg.norm(X - Y) ** 2)
    elif kernel == 'linear':
        # Rumus fungsi kernel linear
        return np.dot(X, Y.T)
    elif kernel == 'poly':
        # Rumus fungsi kernel polynomial
        return (gamma * np.dot(X, Y.T) + 1) ** best_svm.degree
# Menghitung nilai prediksi
# Mendefinisikan fungsi prediksi
def prediksi(data_baru):
    # Melakukan inisialisasi
    hasil_prediksi = bias
    # Looping for untuk melakukan prediksi
    for i in range(len(alpha[0])):
        # Menghitung prediksi
        hasil_prediksi += alpha[0][i] * best_svm.dual_coef_[0][i] * fungsi_kernel(support_vectors[i], data_baru)
    return np.sign(hasil_prediksi).astype(int)
# Melakukan prediksi
Y_pred_svm = prediksi(data_baru)
if Y_pred_svm == 0:
    print("Hasil Prediksi : Normal")
else:
    print("Hasil Prediksi : Penyakit Jantung")
```
Dengan menggunakan fungsi kernel RBF, kombinasi parameter yang optimal adalah Cost = 10, gamma = 0,090. Data baru diklasifikasikan ke dalam kelas "Penyakit Jantung".

## Kesimpulan ##
Berdasarkan metrik evaluasi dan skor ROC, algoritma yang terbaik untuk klasifikasi penyakit jantung adalah algoritma SVM, karena memiliki kinerja yang lebih baik dibandingkan algoritma K-NN. 

