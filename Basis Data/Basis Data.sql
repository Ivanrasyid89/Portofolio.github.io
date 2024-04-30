-- Membuat Schema Basis Data 
CREATE DATABASE Basis_Data;
-- Menggunakan Schema Basis Data
USE Basis_Data;
-- Menampilkan Data
SELECT * FROM Basis_data.customer;
SELECT * FROM Basis_data.ship;
-- Mengganti Nama Tabel Order
ALTER TABLE Basis_Data.order RENAME TO orders;
SELECT * FROM Basis_data.orders;
SELECT * FROM Basis_data.sales;
SELECT * FROM Basis_data.product;
SELECT * FROM Basis_data.superstore_orders;

-- Menampilkan Order ID, Customer ID, Country/Region, City, State, Postal Code, Region yang memiliki Order Date = "09/12/2020"
SELECT ship.`Order ID`, customer.`Customer ID`, customer.`Country/Region`, customer.`City`, customer.`State`, customer.`Postal Code`, customer.`Region`
FROM ship 
INNER JOIN customer
ON ship.`Customer ID` = customer.`Customer ID`
WHERE ship.`Order Date` = '12/06/2020';

-- Menampilkan Product ID, Product Name yang memiliki diskon '0.2' menggunakan INNER JOIN
SELECT product.`Product ID`, product.`Product Name`
FROM product
INNER JOIN sales
ON product.`Product ID` = sales.`Product ID`
WHERE sales.`Discount` = '0.2';

-- Menampilkan Order ID, Customer ID, Product ID, Ship Mode dengan Left Join
SELECT orders.`Order ID`, orders.`Customer ID`, orders.`Product ID`, ship.`Ship Mode`
FROM orders
LEFT JOIN ship
ON orders.`Order ID` = ship.`Order ID`
AND orders.`Customer ID` = ship.`Customer ID`;

-- Menampilkan Product ID, Category, Sub-Category, Quantity, Discount dengan Right Join
SELECT product.`Product ID`, product.`Category`, product.`Sub-Category`, sales.`Quantity`, sales.`Discount`
FROM product
RIGHT JOIN sales
ON product.`Product ID` = sales.`Product ID`;

-- Menampilkan Total Penjualan (Sales) berdasarkan Kategori Produk (Category)
SELECT product.`Product ID`, product.`Category`, product.`Sub-Category`, product.`Product Name`, 
SUM(sales.`Sales`) AS Total_Sales
FROM product
INNER JOIN sales
ON product.`Product ID` = sales.`Product ID`
GROUP BY product.`Category`;

-- Menampilkan Rata-rata Penjualan (Sales) berdasarkan Kategori Produk di setiap Negara/Wilayah (State/Region)
SELECT product.`Product ID`, product.`Category`, customer.`Region`, customer.`State`, orders.`Customer ID`,
AVG(sales.`Sales`) AS Rata_Rata_Penjualan
FROM product
JOIN orders ON product.`Product ID` = orders.`Product ID`
JOIN customer ON orders.`Customer ID` = customer.`Customer ID`
INNER JOIN sales
ON product.`Product ID` = sales.`Product ID`
GROUP BY product.`Category`
;

-- Menampilkan Total Penjualan (Sales) tiap Tanggal Pemesanan (Order Date)
SELECT ship.`Order Date`, ship.`Order ID`, ship.`Customer ID`, orders.`Product ID`, sales.`Sales`
FROM ship
JOIN orders ON ship.`Order ID` = orders.`Order ID` AND ship.`Customer ID` = orders.`Customer ID`
JOIN sales ON orders.`Product ID` = sales.`Product ID`
WHERE ship.`Order Date` = '08/11/2020';

-- Menampilkan Total Penjualan (Sales) berdasarkan Kategori Produk (Category) di setiap Negara/Wilayah (State/Region)
SELECT customer.`State`, customer.`Region`, orders.`Customer ID`, product.`Product ID`, product.`Category`, sales.`Sales`
FROM customer
JOIN orders ON customer.`Customer ID` = orders.`Customer ID`
JOIN product ON orders.`Product ID` = product.`Product ID`
JOIN sales ON product.`Product ID` = sales.`Product ID`;

-- Menampilkan Total Penjualan (Sales) berdasarkan Segmentasi Pelanggan (Segment) dan Negara/Wilayah (State/Region) di setiap Kategori Produk (Category)
SELECT product.`Product ID`, product.`Category`, orders.`Customer ID`, customer.`Segment`, customer.`State`, customer.`Region`, sales.`Sales`
FROM product
JOIN orders ON product.`Product ID` = orders.`Product ID`
JOIN customer ON orders.`Customer ID` = customer.`Customer ID`
INNER JOIN sales
ON product.`Product ID` = sales.`Product ID`
;

-- Menampilkan Nama Produk (Product Name) berdasarkan Jumlah Produk (Quantity) tertinggi
SELECT sales.`Quantity`, product.`Product ID`, product.`Product Name`
FROM sales
INNER JOIN product
ON sales.`Product ID` = product.`Product ID`
ORDER BY sales.`Quantity` DESC
;

-- Menampilkan Nama Produk (Product Name) dan Kategori (Category) berdasarkan Jumlah Penjualan (Sales) yang memiliki Diskon (Discount) lebih dari 10%
SELECT sales.`Quantity`, sales.`Discount`, product.`Product Name`, product.`Product ID`, product.`Category`
FROM sales
INNER JOIN product
ON sales.`Product ID` = product.`Product ID`
WHERE sales.`Discount` > 0.1;
