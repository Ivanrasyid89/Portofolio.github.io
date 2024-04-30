Analisis Cluster Hierarki yang digunakan berdasarkan Tugas Based Project pada Mata Kuliah Data Mining. Pada tugas ini, analisis cluster digunakan untuk mengelompokkan provinsi di Indonesia. Data yang digunakan terdiri dari 4 variabel sebagai berikut.
1. X1 : Persentase Penduduk Miskin (%)
2. X2 : Tingkat Pengangguran Terbuka (%)
3. X3 : Indeks Pembangunan Manusia
4. X4 : Pengeluaran Perkapita

# Langkah-Langkah Analisis #
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
> plot(summary(pca)$importance[2,], xlab = "Principal Component",
+      ylab = "Cumulative Proportion of Variance Explained",
+      type = "b", pch = 16, col = "blue", ylim = c(0,1))
> PC1 <- pca$x[,1]
> PC2 <- pca$x[,2]
> data <- cbind(PC1,PC2);data
             PC1         PC2
 [1,] -0.2948073  0.91194337
 [2,]  0.4169411  0.36038293
 [3,]  0.9007228  0.42517950
 [4,]  0.3939016 -0.64485398
 [5,]  0.1150257 -0.35291168
 [6,] -0.3920098 -0.08630765
 [7,] -0.8339573 -0.69385303
 [8,] -0.6819343 -0.15823340
 [9,]  0.9801343 -0.88719890
[10,]  2.6239516  1.06057957
[11,]  4.4529989 -0.06317367
[12,]  1.2569762  1.77659158
[13,]  0.2839362  0.33026627
[14,]  1.6719233 -1.40591623
[15,]  0.3470350 -0.06639190
[16,]  1.6833887  1.55898807
[17,]  1.8020408 -0.93433425
[18,] -1.1950835 -0.64820965
[19,] -2.9701992  0.14681560
[20,] -0.5859926  0.13458650
[21,]  0.2939878 -0.75636293
[22,]  0.7029766 -0.77246804
[23,]  1.8340768  0.09416696
[24,] -0.2616201 -0.31560000
[25,]  0.9514018  0.66118850
[26,] -1.2079488 -0.68697643
[27,]  0.3783934 -0.10649571
[28,] -0.7468852 -0.67204848
[29,] -1.4300436 -0.87147878
[30,] -1.8749777 -0.88646433
[31,] -0.9002161  1.56801975
[32,] -0.7793887 -0.12565109
[33,] -2.4841826  1.47115836
[34,] -4.4505659  0.63506317
```
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/f217b0d9-04de-4e16-954f-c879a0bc0d94)

Berdasarkan output, PC1 dan PC2 mampu menjelaskan sebesar 86,27% total keragaman dari data, sehingga ke-4 variabel dapat direduksi menjadi 2 variabel dalam bentuk komponen utama, yaitu sebanyak 2 komponen utama.

#### 4. Melakukan Analisis Cluster Hierarki ####
- Menghitung Matriks Jarak Euclidean
```
> jarak <- dist(data, method = "euclidean");jarak
            1          2          3          4          5
2  0.90044695                                            
3  1.29082583 0.48810177                                 
4  1.70233309 1.00550091 1.18399299                      
5  1.32959445 0.77455930 1.10577839 0.40373515           
6  1.00297230 0.92408550 1.39024339 0.96417359 0.57285487
7  1.69389043 1.63589739 2.06430349 1.22883619 1.00836985
8  1.13804464 1.21510903 1.68676437 1.18077195 0.82039309
9  2.20508257 1.36881228 1.31477879 0.63434999 1.01679684
10 2.92254114 2.31542027 1.83664122 2.80742355 2.87969913
11 4.84690799 4.05822163 3.58568742 4.10056374 4.34763839
12 1.77641459 1.64660440 1.39758046 2.57066072 2.41636820
13 0.82054394 0.13637193 0.62404662 0.98130112 0.70374916
14 3.03981952 2.16674716 1.98687239 1.48746611 1.87956084
15 1.17008608 0.43246227 0.74041383 0.58035753 0.36867587
16 2.08132801 1.74371552 1.37771106 2.55336969 2.47287751
17 2.79383488 1.89599419 1.63115048 1.43758654 1.78439692
18 1.80127025 1.90154727 2.35469064 1.58898855 1.34297684
19 2.78265017 3.39386653 3.88091783 3.45599689 3.12543432
20 0.83010395 1.02803695 1.51484881 1.25208627 0.85386246
21 1.76915959 1.12349402 1.32822055 0.14972308 0.44136194
22 1.95775752 1.16840388 1.21386293 0.33438406 0.72229757
23 2.28054947 1.44192393 0.99031259 1.61872069 1.77623649
24 1.22799190 0.95780903 1.37833058 0.73356445 0.37848934
25 1.27118659 0.61329627 0.24138893 1.42005406 1.31450534
26 1.84129624 1.93319132 2.38398544 1.60240408 1.36450015
27 1.22082653 0.46846727 0.74532308 0.53858160 0.36067077
28 1.64724149 1.55576543 1.97952548 1.14111080 0.91909660
29 2.11408511 2.22009808 2.66716974 1.83797025 1.62977016
30 2.39399425 2.60912236 3.07000365 2.28170735 2.06028922
31 0.89272393 1.78697783 2.13294744 2.56350361 2.17271569
            6          7          8          9         10
2                                                        
3                                                        
4                                                        
5                                                        
6                                                        
7  0.75128490                                            
8  0.29871310 0.55677589                                 
9  1.58877511 1.82436597 1.81490022                      
10 3.22666606 3.87752089 3.52340558 2.54872053           
11 4.84506392 5.32444010 5.13581298 3.56928645 2.14668002
12 2.48788034 3.23652589 2.73914618 2.67813764 1.54314451
13 0.79400055 1.51608256 1.08237599 1.40246684 2.45133223
14 2.44973201 2.60508580 2.66408676 0.86466162 2.64385313
15 0.73931308 1.33732954 1.03305982 1.03659970 2.54055393
16 2.64844802 3.37821313 2.92294412 2.54526960 1.06445748
17 2.35223456 2.64694496 2.60239601 0.82325699 2.15759554
18 0.98013321 0.36399915 0.70950601 2.18830716 4.18389647
19 2.58870755 2.29570314 2.30850840 4.08342022 5.66828792
20 0.29397881 0.86475347 0.30813683 1.86997298 3.34083900
21 0.95894048 1.12967595 1.14463221 0.69850918 2.95465928
22 1.29221177 1.53894319 1.51501230 0.29996599 2.65522293
23 2.23339041 2.78197442 2.52863951 1.30088305 1.24814086
24 0.26377351 0.68603593 0.44880763 1.36699645 3.19693515
25 1.53736964 2.24134892 1.82735854 1.54865396 1.71957438
26 1.01319266 0.37405466 0.74582869 2.19722478 4.21158080
27 0.77066771 1.34713881 1.06158921 0.98569244 2.53073042
28 0.68485678 0.08976082 0.51790399 1.74036949 3.79005813
29 1.30154053 0.62198850 1.03362781 2.41022916 4.49084921
30 1.68506507 1.05868900 1.39773844 2.85511207 4.90217755
31 1.73062786 2.26284305 1.73999911 3.09254207 3.56051317
           11         12         13         14         15
2                                                        
3                                                        
4                                                        
5                                                        
6                                                        
7                                                        
8                                                        
9                                                        
10                                                       
11                                                       
12 3.68772245                                            
13 4.18758623 1.74317636                                 
14 3.08825819 3.20944498 2.22279957                      
15 4.10596517 2.05537861 0.40164556 1.88405272           
16 3.20969615 0.47872628 1.86231695 2.96492646 2.10421037
17 2.79042993 2.76517889 1.97581784 0.48920356 1.69421546
18 5.67830089 3.44851530 1.77339062 2.96544216 1.64822362
19 7.42616756 4.53047257 3.25930227 4.89492366 3.32407878
20 5.04287062 2.46834253 0.89166514 2.73337394 0.95442797
21 4.21638285 2.70983492 1.08667569 1.52336004 0.69200724
22 3.81651226 2.60856677 1.17966850 1.15763314 0.79071989
23 2.62364421 1.77865052 1.56801744 1.50882183 1.49568465
24 4.72137172 2.58522734 0.84544361 2.21977018 0.65769722
25 3.57573521 1.15650324 0.74499657 2.18908044 0.94585018
26 5.69521363 3.48497098 1.80568645 2.96825503 1.67424599
27 4.07483575 2.07796187 0.44685925 1.83349758 0.05090843
28 5.23541043 3.16406362 1.43778563 2.52768598 1.25039238
29 5.93831167 3.77257897 2.09330309 3.14766931 1.95094156
30 6.38130820 4.11108282 2.47817321 3.58473667 2.36851406
31 5.59622220 2.16725198 1.71296540 3.93194566 2.05595154
           16         17         18         19         20
2                                                        
3                                                        
4                                                        
5                                                        
6                                                        
7                                                        
8                                                        
9                                                        
10                                                       
11                                                       
12                                                       
13                                                       
14                                                       
15                                                       
16                                                       
17 2.49614393                                            
18 3.62730251 3.01075095                                 
19 4.86313797 4.89317481 1.94501953                      
20 2.67936768 2.61635152 0.99184751 2.38423794           
21 2.70023795 1.51851826 1.49299376 3.38683453 1.25226052
22 2.52920847 1.11091987 1.90212301 3.78646304 1.57613116
23 1.47255145 1.02900002 3.11880343 4.80456444 2.42040691
24 2.70132179 2.15442068 0.99095058 2.74776798 0.55487423
25 1.15838196 1.80811491 2.51434338 3.95519077 1.62508195
26 3.66117315 3.02013633 0.04084581 1.94954753 1.03043444
27 2.11585652 1.64684202 1.66411642 3.35816006 0.99406289
28 3.29905364 2.56238513 0.44883182 2.36931712 0.82252440
29 3.94976321 3.23269554 0.32412245 1.84634849 1.31323622
30 4.31766237 3.67733008 0.72043141 1.50571498 1.64439267
31 2.58362059 3.68292931 2.23575926 2.51090641 1.46746970
           21         22         23         24         25
2                                                        
3                                                        
4                                                        
5                                                        
6                                                        
7                                                        
8                                                        
9                                                        
10                                                       
11                                                       
12                                                       
13                                                       
14                                                       
15                                                       
16                                                       
17                                                       
18                                                       
19                                                       
20                                                       
21                                                       
22 0.40930571                                            
23 1.75933941 1.42493648                                 
24 0.70920526 1.06732145 2.13538154                      
25 1.56257649 1.45502103 1.04910842 1.55741387           
26 1.50353851 1.91283677 3.14071722 1.01659160 2.54565195
27 0.65532566 0.74085988 1.46944874 0.67330668 0.95795496
28 1.04428227 1.45333515 2.69229468 0.60211104 2.15909693
29 1.72787033 2.13531683 3.40396143 1.29391448 2.83202247
30 2.17286391 2.58047342 3.83649875 1.71137628 3.22236720
31 2.61321218 2.83691909 3.10621954 1.98892641 2.06175461
           26         27         28         29         30
2                                                        
3                                                        
4                                                        
5                                                        
6                                                        
7                                                        
8                                                        
9                                                        
10                                                       
11                                                       
12                                                       
13                                                       
14                                                       
15                                                       
16                                                       
17                                                       
18                                                       
19                                                       
20                                                       
21                                                       
22                                                       
23                                                       
24                                                       
25                                                       
26                                                       
27 1.68921268                                            
28 0.46130524 1.25940533                                 
29 0.28873380 1.96357924 0.71167259                      
30 0.69622046 2.38454026 1.14828866 0.44518638           
31 2.27589700 2.10685652 2.24530979 2.49637140 2.64095667
           31         32         33
2                                  
3                                  
4                                  
5                                  
6                                  
7                                  
8                                  
9                                  
10                                 
11                                 
12                                 
13                                 
14                                 
15                                 
16                                 
17                                 
18                                 
19                                 
20                                 
21                                 
22                                 
23                                 
24                                 
25                                 
26                                 
27                                 
28                                 
29                                 
30                                 
31                                 
 [ reached getOption("max.print") -- omitted 3 rows ]
```
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
Nilai korelasi untuk Single Linkage sebesar **79,89%**
- Average Linkage
```
> ## Average Linkage ##
> hierave <- hclust(dist(data), method = "ave")
> # Korelasi Cophenetic
> hc2 <- hclust(jarak, "ave")
> d3 <- cophenetic(hc2)
> corave <- cor(jarak,d3);corave
[1] 0.8188729
```
Nilai korelasi untuk Average Linkage sebesar **81,88%**
- Complete Linkage
```
> ## Complete Linkage ##
> hiercomp <- hclust(dist(data), method = "complete")
> # Korelasi Cophenetic
> hc3 <- hclust(jarak, "complete")
> d4 <- cophenetic(hc3)
> corcomp <- cor(jarak,d4);corcomp
[1] 0.4906064
```
Nilai korelasi untuk Complete Linkage sebesar **49,06%**
- Centroid Linkage
```
> ## Centorid Linkage ##
> hiercen <- hclust(dist(data), method = "centroid")
> # Korelasi Cophenetic
> hc4 <- hclust(jarak, "centroid")
> d5 <- cophenetic(hc4)
> corcen <- cor(jarak,d5);corcen
[1] 0.8039401
```
Nilai korelasi untuk Centroid Linkage sebesar **80,39%**
- Ward Linkage
```
> ## Ward ##
> hierward <- hclust(dist(data), method = "ward.D")
> # Korelasi Cophenetic
> hc5 <- hclust(jarak,"ward.D")
> d6 <- cophenetic(hc5)
> corward <- cor(jarak,d6);corward
[1] 0.5360377
```
- Perbandingkan nilai korelasi
```
> KorCop<-data.frame(cors,corave,corcomp,corcen,corward);KorCop
      cors    corave   corcomp    corcen   corward
1 0.798912 0.8188729 0.4906064 0.8039401 0.5360377
```
Berdasarkan output perbandingan korelasi, dapat diketahui bahwa metode **Average Linkage** adalah metode yang terbaik untuk mengukur kedekatan dua cluster.

#### 5. Pemilihan Jumlah Cluster Optimal ####
## Menggunakan Indeks Validitas ##
```
> inval <- clValid(obj = data.frame(data), nClust = 2:5, clMethods = "hierarchical", validation = "internal", metric = "euclidean", method = "average", maxitems = length(data), verbose = T)
[1] "Finished internal validation, hierarchical 2 clusters"
[1] "Finished internal validation, hierarchical 3 clusters"
[1] "Finished internal validation, hierarchical 4 clusters"
[1] "Finished internal validation, hierarchical 5 clusters"
> summary(inval)

Clustering Methods:
 hierarchical 

Cluster sizes:
 2 3 4 5 

Validation Measures:
                                 2       3       4       5
                                                          
hierarchical Connectivity   3.0956  8.1742 15.6996 19.7103
             Dunn           0.3029  0.3072  0.2519  0.2555
             Silhouette     0.5047  0.4283  0.3774  0.3547

Optimal Scores:

             Score  Method       Clusters
Connectivity 3.0956 hierarchical 2       
Dunn         0.3072 hierarchical 3       
Silhouette   0.5047 hierarchical 2       

> optimalScores(inval)
                 Score       Method Clusters
Connectivity 3.0956349 hierarchical        2
Dunn         0.3071523 hierarchical        3
Silhouette   0.5047025 hierarchical        2
> plot(inval)
Hit <Return> to see next plot: Connectivity
Hit <Return> to see next plot: Dunn
Hit <Return> to see next plot: Silhouette
```
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/1d30c83a-80eb-4fe8-bf41-7121a798d7af)
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/b6afc4c4-85dc-4e0e-977b-95f9f3a04f99)
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/2bc882c2-3558-4cee-b625-0fa0047a39e7)
Berdasarkan ouptut, dapat diketahui bahwa banyaknya cluster yang optimal sebanyak **3 cluster** menggunakan Indeks Connectivity, Dunn, dan Silhouette.

#### 6. Melakukan Analisis Cluster Metode Terbaik ####
```
> hirave <- hclust(jarak, method = "average");hirave

Call:
hclust(d = jarak, method = "average")

Cluster method   : average 
Distance         : euclidean 
Number of objects: 34
> anggotaave <- data.frame(id = Data_Cluster$Provinsi, cutree(hirave, k = 3));anggotaave
                     id cutree.hirave..k...3.
1                  ACEH                     1
2        SUMATERA UTARA                     1
3        SUMATERA BARAT                     1
4                  RIAU                     1
5                 JAMBI                     1
6      SUMATERA SELATAN                     1
7              BENGKULU                     1
8               LAMPUNG                     1
9  KEP, BANGKA BELITUNG                     1
10            KEP, RIAU                     1
11          DKI JAKARTA                     2
12           JAWA BARAT                     1
13          JAWA TENGAH                     1
14        DI YOGYAKARTA                     1
15           JAWA TIMUR                     1
16               BANTEN                     1
17                 BALI                     1
18  NUSA TENGGARA BARAT                     1
19  NUSA TENGGARA TIMUR                     3
20     KALIMANTAN BARAT                     1
21    KALIMANTAN TENGAH                     1
22   KALIMANTAN SELATAN                     1
23     KALIMANTAN TIMUR                     1
24     KALIMANTAN UTARA                     1
25       SULAWESI UTARA                     1
26      SULAWESI TENGAH                     1
27     SULAWESI SELATAN                     1
28    SULAWESI TENGGARA                     1
29            GORONTALO                     1
30       SULAWESI BARAT                     1
31               MALUKU                     1
32         MALUKU UTARA                     1
33          PAPUA BARAT                     3
34                PAPUA                     3
```
![image](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/78907471-39dd-4f46-b783-2c261b6f9ca7)
Berdasarkan output dan plot Dendogram, dapat diketahui masing-masing aggota dari setiap cluster.

#### 7. Karakteristik Tiap Cluster ####
```
> aggregate(Data,list(idclus),mean)
  Group.1       X1       X2       X3       X4
1       1  9.18800 5.057167 11155.13 72.40300
2       2  4.69000 7.590000 18927.00 81.65000
3       3 22.64667 4.070000  7708.00 64.39333
```

