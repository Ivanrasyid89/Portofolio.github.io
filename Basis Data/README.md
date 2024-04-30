Tugas Praktikum pada Mata Kuliah Basis Data. Data yang digunakan adalah Data Superstore_orders dengan rincian sebagai berikut.
1. Data Customer : Customer ID, Customer Name, Segment, Country/Region, City, State, Postal Code, Region
2. Data Order : Row ID, Order ID, Customer ID, Product ID
3. Data Product : Product ID, Category, Sub-Category, Product Name
4. Data Ship : Order ID, Order Date, Ship Date, Ship Mode, Customer ID
5. Data Sales : Product ID, Sales, Quantity, Discount, Profit

# Perintah #
## Menampilkan Order ID, Customer ID, Country/Region, City, State, Postal Code, Region yang memiliki Order Date = “09/12/2020” menggunakan INNER JOIN ##
```
SELECT ship.`Order ID`, customer.`Customer ID`, customer.`Country/Region`, customer.`City`, customer.`State`, customer.`Postal Code`, customer.`Region`
FROM ship 
INNER JOIN customer
ON ship.`Customer ID` = customer.`Customer ID`
WHERE ship.`Order Date` = '12/06/2020';
```
<img width="425" alt="image" src="https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/8b5960a4-12dd-4f8e-927c-166e5f5f3806">

Penjelasan:
- Baris pertama menunjukkan kolom-kolom yang akan ditampilkan dalam kueri
- Baris kedua menunjukkan nama tabel utama (Tabel Ship) yang digunakan
- Baris ketiga menunjukkan penggabungan antara kedua tabel (Tabel Customer dan Tabel Ship) yang digunakan
- Baris keempat menunjukkan kondisi antara dua tabel yang memiliki kolom yang sama (Customer ID)
- Baris kelima menunjukkan klausa untuk menyaring baris yang ditampilkan dalam kondisi tertentu ('12/06/2020')

## Menampilkan Product ID, Product Name yang memiliki diskon '0.2' menggunakan INNER JOIN ##
```
SELECT product.`Product ID`, product.`Product Name`
FROM product
INNER JOIN sales
ON product.`Product ID` = sales.`Product ID`
WHERE sales.`Discount` = '0.2';
```
<img width="366" alt="image" src="https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/985de9ef-d360-4905-b1ca-b95278f07c54">

Penjelasan:
- Baris pertama menunjukkan kolom-kolom yang akan ditampilkan dalam kueri
- Baris kedua menunjukkan nama tabel utama (Tabel Product) yang digunakan
- Baris ketiga menunjukkan penggabungan antara kedua tabel (Tabel Product dan Tabel Sales) yang digunakan
- Baris keempat menunjukkan kondisi antara dua tabel yang memiliki kolom yang sama (Product ID)
- Baris kelima menunjukkan klausa untuk menyaring baris yang ditampilkan dalam kondisi tertentu ('02')

## Menampilkan Order ID, Customer ID, Product ID, Ship Mode dengan LEFT JOIN ##
```
SELECT orders.`Order ID`, orders.`Customer ID`, orders.`Product ID`, ship.`Ship Mode`
FROM orders
LEFT JOIN ship
ON orders.`Order ID` = ship.`Order ID`
AND orders.`Customer ID` = ship.`Customer ID`;
```
<img width="364" alt="image" src="https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/b2edf1ad-08c8-4d47-94a4-6093241eb41d">

Penjelasan:
- Baris pertama menunjukkan kolom-kolom yang akan ditampilkan dalam kueri
- Baris kedua menunjukkan nama tabel utama (Tabel Orders) yang digunakan
- Baris ketiga menunjukkan penggabungan antara tabel pertama (Tabel Orders) di sebelah kiri dengan tabel kedua (Tabel Ship) di sebelah kanan
- Baris keempat menunjukkan kondisi pertama antara dua tabel yang memiliki kolom yang sama (Order ID)
- Baris kelima menunjukkan kondisi kedua antara dua tabel yang memiliki kolom yang sama (Customer ID)

## Menampilkan Product ID, Category, Sub-Category, Quantity, Discount dengan RIGHT JOIN ##
```
SELECT product.`Product ID`, product.`Category`, product.`Sub-Category`, sales.`Quantity`, sales.`Discount`
FROM product
RIGHT JOIN sales
ON product.`Product ID` = sales.`Product ID`;
```
<img width="364" alt="image" src="https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/1354d7af-8b4f-4418-96ea-3ee84a3baba5">

Penjelasan:
- Baris pertama menunjukkan kolom-kolom yang akan ditampilkan dalam kueri
- Baris kedua menunjukkan nama tabel utama (Tabel Product) yang digunakan
- Baris ketiga menunjukkan penggabungan antara tabel kedua (Tabel Sales) di sebelah kanan dengan tabel pertama (Tabel Product) di sebelah kiri
- Baris keempat menunjukkan kondisi pertama antara dua tabel yang memiliki kolom yang sama (Product ID)

## Menampilkan Total Penjualan (Sales) berdasarkan Kategori (Category) Produk ##
```
SELECT product.`Product ID`, product.`Category`, 
SUM(sales.`Sales`) AS Total_Sales
FROM product
INNER JOIN sales
ON product.`Product ID` = sales.`Product ID`
GROUP BY product.`Category`;
```
<img width="361" alt="image" src="https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/e7fe719d-8263-47a3-9c7c-1f5fee851921">

Penjelasan:
- Baris pertama menunjukkan kolom-kolom yang akan ditampilkan dalam kueri
- Baris kedua menunjukkan fungsi agregate penjumlahan dari Total Penjualan (Sales) yang ditampilkan dalam kolom Total_Sales
- Baris ketiga menunjukkan nama tabel utama (Tabel Product) yang digunakan
- Baris keempat menunjukkan penggabungan antara kedua tabel (Tabel Product dan Tabel Sales) yang digunakan
- Baris kelima menunjukkan kondisi pertama antara dua tabel yang memiliki kolom yang sama (Product ID)
- Baris keenam menunjukkan klausa untuk mengelompokkan baris berdasarkan nilai tertentu dari suatu kolom (Kolom Category)

## Menampilkan Rata-rata Penjualan (Sales) berdasarkan Kategori Produk di setiap Negara (Country/Region) dan Kota (City) ##
```
SELECT product.`Product ID`, product.`Category`, customer.`Country/Region`, customer.`City`, orders.`Customer ID`,
AVG(sales.`Sales`) AS Rata_Rata_Penjualan
FROM product
JOIN orders ON product.`Product ID` = orders.`Product ID`
JOIN customer ON orders.`Customer ID` = customer.`Customer ID`
INNER JOIN sales
ON product.`Product ID` = sales.`Product ID`
GROUP BY product.`Category`, customer.`Country/Region`, customer.`City`
;
```
<img width="452" alt="image" src="https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/ec86ee6c-8c1c-45b3-bac3-2ffdb77fc291">

Penjelasan:
- Baris pertama menunjukkan kolom-kolom yang akan ditampilkan dalam kueri
- Baris kedua menunjukkan fungsi agregate rata-rata dari Rata-rata Penjualan (Sales) yang ditampilkan dalam kolom Rata-Rata_Penjualan
- Baris ketiga menunjukkan nama tabel utama (Tabel Product) yang digunakan
- Baris keempat menunjukkan penggabungan tabel Product dengan tabel Orders berdasarkan kriteria Product ID
- Baris kelima menunjukkan penggabungan tabel Orders dengan tabel Customer berdasarkan kriteria Customer ID
- Baris keenam menunjukkan penggabungan antara kedua tabel (Tabel Product dan Tabel Sales) yang digunakan
- Baris ketujuh menunjukkan kondisi pertama antara dua tabel yang memiliki kolom yang sama (Product ID)
- Baris kedelapan menunjukkan klausa untuk mengelompokkan baris berdasarkan nilai tertentu dari suatu kolom (Kolom Category, Country/Region, dan City)
- Baris kesembilan menunjukkan akhir dari sebuah pernyataan SQL

