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
- Baris kedua menunjukkan nama tabel yang digunakan
- Baris ketiga menunjukkan penggabungan antara kedua tabel yang digunakan
- Baris keempat menunjukkan kondisi antara dua tabel yang memiliki kolom yang sama
- Baris kelima menunjukkan klausa untuk menyaring baris yang ditampilkan dalam kondisi tertentu
