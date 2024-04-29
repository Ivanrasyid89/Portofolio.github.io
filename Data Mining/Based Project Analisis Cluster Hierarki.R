#### INSTALL PACKAGE ####
library(psych)
library(GPArotation)
library(clValid)
library(ggplot2)
library(cluster)
library(factoextra)
library(tidyverse)
library(car)
library(readxl)

#### MEMBACA DATA ####
Data_Cluster <- read_xlsx("D:/MATERI KULIAH/SEMESTER 5/DATA MINING/TUGAS DATA MINING/Data Cluster Sosial Ekonomi.xlsx")
X1 <- Data_Cluster$`Pers.Pend.Miskin (%)`
X2 <- Data_Cluster$`Tingkat.Peng.Terbuka (%)`
X3 <- Data_Cluster$Peng.Perkapita
X4 <- Data_Cluster$IPM
Data <- cbind(X1, X2, X3, X4)

#### STATISTIKA DESKRIPTIF ####
summary(Data)

#### PEMERIKSAAN ASUMSI ####
# Uji Sampel Representatif (KMO)
kmo <- KMO(Data);kmo
# Nonmultikolinearitas
korelasi <- cor(Data, method = 'pearson');korelasi
corrplot(korelasi, method = "number", type = "upper", 
         tl.col = "black", tl.srt = 45)

#### DATA PREPROCESSING ####
# Standarisasi Data
datastand <- scale(Data);datastand
# Analisis PCA
pca <- prcomp(datastand);pca
# Menampilkan Varian Tiap Komponen
summary(pca)
# Plot
plot(summary(pca)$importance[2,], xlab = "Principal Component",
     ylab = "Cumulative Proportion of Variance Explained",
     type = "b", pch = 16, col = "blue", ylim = c(0,1))
PC1 <- pca$x[,1]
PC2 <- pca$x[,2]
data <- cbind(PC1,PC2);data[1:10]

#### ANALISIS KLUSTER HIERARKI ####
# Menghitung Matriks Jarak Euclidien
jarak <- dist(data, method = "euclidean");jarak

## Single Linkage ##
hiers <- hclust(dist(data), method = "single")
# Korelasi Cophenetic
hc1 <- hclust(jarak, "single")
d2 <- cophenetic(hc1)
cors <- cor(jarak,d2);cors

## Average Linkage ##
hierave <- hclust(dist(data), method = "ave")
# Korelasi Cophenetic
hc2 <- hclust(jarak, "ave")
d3 <- cophenetic(hc2)
corave <- cor(jarak,d3);corave

## Complete Linkage ##
hiercomp <- hclust(dist(data), method = "complete")
# Korelasi Cophenetic
hc3 <- hclust(jarak, "complete")
d4 <- cophenetic(hc3)
corcomp <- cor(jarak,d4);corcomp

## Centorid Linkage ##
hiercen <- hclust(dist(data), method = "centroid")
# Korelasi Cophenetic
hc4 <- hclust(jarak, "centroid")
d5 <- cophenetic(hc4)
corcen <- cor(jarak,d5);corcen

## Ward ##
hierward <- hclust(dist(data), method = "ward.D")
# Korelasi Cophenetic
hc5 <- hclust(jarak,"ward.D")
d6 <- cophenetic(hc5)
corward <- cor(jarak,d6);corward

KorCop<-data.frame(cors,corave,corcomp,corcen,corward);KorCop

#### PEMILIHAN JUMLAH CLUSTER ####
## Indeks Validitas ##
inval <- clValid(obj = data.frame(data), nClust = 2:5, clMethods = "hierarchical", validation = "internal", metric = "euclidean", method = "average", maxitems = length(data), verbose = T)
summary(inval)
optimalScores(inval)
plot(inval)

#### ANALISIS KLUSTER METODE TERBAIK ####
matriks_jarak <- dist(data, method = "euclidean", diag = F)
## Metode Average Linkage ##
hirave <- hclust(matriks_jarak, method = "average");hirave
plot(hirave, labels(Data_Cluster$Provinsi), hang = 1, col = "blue", main = "Cluster Dendogram", sub = " ", xlab = "PROVINSI", ylab = "Jarak")
rect.hclust(hirave, k = 3, border = 2:5)
## Anggota Kluster ##
anggotaave <- data.frame(id = Data_Cluster$Provinsi, cutree(hirave, k = 3));anggotaave
clus_hier <- eclust(datastand, "hclust", k = 3, hc_method = "average", graph = TRUE)
fviz_dend(clus_hier, rect = TRUE, cex = 0.5)
## Karakteristik Kluster
idclus = clus_hier$cluster;idclus
aggregate(Data_Cluster[,2:5],list(idclus),mean)

