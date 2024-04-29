Analisis Cluster Hierarki yang digunakan berdasarkan Tugas Based Project pada Mata Kuliah Data Mining. Pada tugas ini, analisis cluster digunakan untuk mengelompokkan provinsi di Indonesia. Data yang digunakan terdiri dari 4 variabel sebagai berikut.
1. X1 : Persentase Penduduk Miskin (%)
2. X2 : Tingkat Pengangguran Terbuka (%)
3. X3 : Indeks Pembangunan Manusia
4. X4 : Pengeluaran Perkapita

### Langkah-Langkah Analisis ###
#### 1. Melakukan Analisis Statistik Deskriptif ####

```> summary(Data)
       X1               X2              X3       
 Min.   : 4.450   Min.   :2.725   Min.   : 7146  
 1st Qu.: 6.258   1st Qu.:3.979   1st Qu.: 9699  
 Median : 8.525   Median :4.665   Median :10990  
 Mean   :10.243   Mean   :5.045   Mean   :11080  
 3rd Qu.:12.223   3rd Qu.:6.006   3rd Qu.:11858  
 Max.   :26.560   Max.   :8.330   Max.   :18927  
       X4       
 Min.   :61.39  
 1st Qu.:70.23  
 Median :72.19  
 Mean   :71.97  
 3rd Qu.:73.22  
 Max.   :81.65
```
#### 2. Melakukan Pemeriksaan Asumsi ####
- Asumsi Kecukupan Sampel (KMO)
```
> kmo <- KMO(Data);kmo
Kaiser-Meyer-Olkin factor adequacy
Call: KMO(r = Data)
Overall MSA =  0.74
MSA for each item = 
  X1   X2   X3   X4 
0.90 0.92 0.69 0.66
```
Berdasarkan output dapat diketahui bahwa semua sampel memiliki nilai MSA yang lebih dari 0,5. Hal ini dapat diartikan bahwa semua yang digunakan telah representatif, sehingga **Asumsi Kecukupan Sampel Terpenuhi**.
- Asumsi Nonmultikolinieritas
```
> korelasi <- cor(Data, method = 'pearson');korelasi
           X1         X2         X3         X4
X1  1.0000000 -0.3883683 -0.6153603 -0.6697805
X2 -0.3883683  1.0000000  0.4337638  0.4882251
X3 -0.6153603  0.4337638  1.0000000  0.8778390
X4 -0.6697805  0.4882251  0.8778390  1.0000000
```
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/f618b70f-39aa-43e3-a9f9-1a75b8607f33)

Berdasarkan output dapat diketahui bahwa terjadi pelanggaran asumsi nonmultikolinieritas. Hal ini disebabkan karena adanya korelasi yang kuat antara "Indeks Pembangunan Manusia" dan "Pengeluaran Perkapita", sehingga **Asumsi Nonmultikolinieritas Tidak Terpenuhi**.

#### 3. Melakukan Data Preprocessing ####
- Standarisasi Data
```
> datastand <- scale(Data);datastand
               X1          X2          X3          X4
 [1,]  0.83776492  0.66732493 -0.49697110  0.21323199
 [2,] -0.34740148  0.50137893 -0.10306492  0.19015950
 [3,] -0.82375453  0.76819406  0.02245095  0.33115803
 [4,] -0.65988908 -0.42922018  0.03491352  0.39781187
 [5,] -0.49983446 -0.26002034 -0.09282781  0.04403376
 [6,]  0.31568197 -0.23398959  0.01310402 -0.27385381
 [7,]  0.83395409 -1.01165808 -0.10662565  0.04916098
 [8,]  0.25280337 -0.40969712 -0.33095189 -0.38921624
 [9,] -1.10385013 -0.37065100  1.01411534  0.06966986
[10,] -0.76278134  2.00465441  1.50861225  1.15151307
[11,] -1.05812024  1.65649321  3.49283121  2.48202639
[12,] -0.41599632  2.13806198  0.08787944  0.29526749
[13,]  0.13085699  0.40050980  0.13238861  0.21066838
[14,]  0.20897889 -0.74809679  1.51439845  2.22310184
[15,]  0.02605931  0.06861781  0.40612003  0.20041394
[16,] -0.77802464  2.12504661  0.50582057  0.34653968
[17,] -1.08098518 -0.14613583  1.27404891  1.14638585
[18,]  0.65484535 -1.06697341 -0.17739524 -0.64301358
[19,]  1.86859293 -1.05721188 -1.42543246 -1.55565856
[20,] -0.66941614 -0.03875901 -0.76758688 -0.85579317
[21,] -0.94570092 -0.53008931  0.16844104 -0.08671032
[22,] -1.09622848 -0.37390485  0.61842878 -0.03287452
[23,] -0.74944346  0.77795559  0.69498456  1.40274680
[24,] -0.66179450 -0.37065100 -0.76981234 -0.03543813
[25,] -0.56461847  0.98620154  0.04426045  0.47215655
[26,]  0.39761470 -1.11252721 -0.61581060 -0.43279760
[27,] -0.30738782  0.05560244  0.15597847  0.21835921
[28,]  0.17658688 -0.93356585 -0.61046950  0.06710625
[29,]  0.98638707 -1.38585003 -0.17472469 -0.55328725
[30,]  0.28710079 -1.50949606 -0.76625160 -1.29417039
[31,]  1.09118474  1.05127840 -0.98078582 -0.44817926
[32,] -0.76468676 -0.36739716 -1.19353967 -0.64044997
[33,]  2.11248569  0.34519447 -1.32573191 -1.55822217
[34,]  3.10901628 -1.19061945 -1.75079452 -2.71184645
attr(,"scaled:center")
          X1           X2           X3           X4 
   10.243235     5.044559 11079.558824    71.968235 
attr(,"scaled:scale")
         X1          X2          X3          X4 
   5.248208    1.536644 2246.727859    3.900750
```
Sebelum melakukan analisis PCA untuk mengatasi masalah multikolinieritas, data perlu dilakukan standarisasi terlebih dahulu agar memiliki skala yang sama.
- Analisis PCA
```
> pca <- prcomp(datastand);pca
Standard deviations (1, .., p=4):
[1] 1.6652977 0.8231298 0.6576018 0.3417612

Rotation (n x k) = (4 x 4):
          PC1        PC2         PC3         PC4
X1 -0.4862432  0.2589753 -0.83016114 -0.08562600
X2  0.3935748  0.9164249  0.04993102  0.05264184
X3  0.5425567 -0.2455728 -0.46216713  0.65705997
X4  0.5606234 -0.1810835 -0.30780011 -0.74710723
```
Output tersebut menampilkan nilai eigen tiap komponen utama dan vektor eigen
```
> summary(pca)
Importance of components:
                          PC1    PC2    PC3    PC4
Standard deviation     1.6653 0.8231 0.6576 0.3418
Proportion of Variance 0.6933 0.1694 0.1081 0.0292
Cumulative Proportion  0.6933 0.8627 0.9708 1.0000
```
Berdasarkan output, PC1 dan PC2 mampu menjelaskan sebesar 86,27% total keragaman dari data, sehingga ke-4 variabel dapat direduksi menjadi 2 variabel dalam bentuk komponen utama, yaitu sebanyak 2 komponen utama.
#### 4. Melakukan Analisis Cluster Hierarki ####
- Menghitung Matriks Jarak Euclidean
- Single Linkage
```
> ## Single Linkage ##
> hiers <- hclust(dist(data), method = "single")
> # Korelasi Cophenetic
> hc1 <- hclust(jarak, "single")
> d2 <- cophenetic(hc1)
> cors <- cor(jarak,d2);cors
[1] 0.798912
```
Nilai korelasi untuk Single Linkage sebesar 79,89%
- Average Linkage
- Complete Linkage
- Centroid Linkage
- Ward Linkage
