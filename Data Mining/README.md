Analisis Cluster Hierarki yang digunakan berdasarkan Tugas Based Project pada Mata Kuliah Data Mining. Pada tugas ini, analisis cluster digunakan untuk mengelompokkan provinsi di Indonesia. Data yang digunakan terdiri dari 4 variabel sebagai berikut.
1. X1 : Persentase Penduduk Miskin (%)
2. X2 : Tingkat Pengangguran Terbuka (%)
3. X3 : Indeks Pembangunan Manusia
4. X4 : Pengeluaran Perkapita

### Langkah-Langkah Analisis ###
#### 1. Melakukan Analisis Statistik Deskriptif ####
> summary(Data)
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

#### 2. Melakukan Pemeriksaan Asumsi ####
- Asumsi Kecukupan Sampel (KMO)
kmo <- KMO(Data);kmo
Kaiser-Meyer-Olkin factor adequacy
Call: KMO(r = Data)
Overall MSA =  0.74
MSA for each item = 
  X1   X2   X3   X4 
0.90 0.92 0.69 0.66

Berdasarkan output dapat diketahui bahwa semua sampel memiliki nilai MSA yang lebih dari 0,5. Hal ini dapat diartikan bahwa semua yang digunakan telah representatif, sehingga **Asumsi Kecukupan Sampel Terpenuhi**.
- Asumsi Nonmultikolinieritas
> korelasi <- cor(Data, method = 'pearson');korelasi
           X1         X2         X3         X4
X1  1.0000000 -0.3883683 -0.6153603 -0.6697805
X2 -0.3883683  1.0000000  0.4337638  0.4882251
X3 -0.6153603  0.4337638  1.0000000  0.8778390
X4 -0.6697805  0.4882251  0.8778390  1.0000000

![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/f618b70f-39aa-43e3-a9f9-1a75b8607f33)

Berdasarkan output dapat diketahui bahwa terjadi pelanggaran asumsi nonmultikolinieritas. Hal ini disebabkan karena adanya korelasi yang kuat antara "Indeks Pembangunan Manusia" dan "Pengeluaran Perkapita", sehingga **Asumsi Nonmultikolinieritas Tidak Terpenuhi**.


