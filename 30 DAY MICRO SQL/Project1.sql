DROP TABLE IF EXISTS Books;
CREATE TABLE Books(
	Book_ID SERIAL PRIMARY KEY,
	Title VARCHAR(100),
	Author VARCHAR(100),
	Genre VARCHAR(50),
	Published_Year INT,
	Price NUMERIC(10,2),
	Stock INT
);

DROP TABLE IF EXISTS Customers; -- now you can't delete this because other tables depend on it
CREATE TABLE Customers(
	Customer_ID SERIAL PRIMARY KEY,
	Name VARCHAR(100),
	Email VARCHAR(100),
	Phone VARCHAR(15),
	City VARCHAR(50),
	Country VARCHAR(150)
);

DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders(
	Order_ID SERIAL PRIMARY KEY,
	Customer_ID INT REFERENCES Customers(Customer_ID),
	Book_ID INT REFERENCES Books(Book_ID),
	Order_Date DATE,
	Quantity INT,
	Total_Amount NUMERIC(10,2)
);

SELECT * FROM Books;
SELECT * FROM Customers;
SELECT * FROM Orders;

-- Import Data into books table
COPY Books(Book_ID,Title,Author,Genre,Published_Year,Price,Stock)
FROM 'C:\Program Files\PostgreSQL\Books.csv'
CSV HEADER;

-- Import Data into Customers table
COPY Customers(Customer_ID,Name,Email,Phone,City,Country)
FROM 'C:\Program Files\PostgreSQL\Customers.csv'
CSV HEADER;

-- Import Data into Orders table
COPY Orders(Order_ID,Customer_ID,Book_ID,Order_Date,Quantity,Total_Amount)
FROM 'C:\Program Files\PostgreSQL\Orders.csv'
CSV HEADER;

-- 1 : Retrieve all the books in the fiction genre
SELECT Book_ID,Title,Genre FROM Books WHERE Genre = 'Fiction';

-- 2 : Find Books published after the year 1950
SELECT Book_ID,Title,Published_Year FROM Books WHERE Published_Year > 1950;

-- 3 : List all the customers from canada
SELECT Customer_ID,Name,Country FROM Customers WHERE Country = 'Canada';

-- 4 : Show Orders placed in November 2023
SELECT Order_ID,Customer_ID,Book_ID,Order_Date FROM Orders WHERE Order_Date BETWEEN '2023-11-01' AND '2023-11-30';

-- 5 : Retrieve the total stock of books available
SELECT DISTINCT SUM(Stock) AS Total_stock FROM Books;

-- 6 : Find the details of the most expensive book
SELECT * FROM Books ORDER BY Price DESC LIMIT 1;

-- 7 : Show all customers who ordered more than one quantity of a book
SELECT c.Customer_ID,c.Name,
	   o.Customer_ID,o.Order_ID,o.Quantity
FROM Customers c
INNER JOIN Orders o
ON c.Customer_ID = o.Customer_ID
WHERE o.Quantity > 1;

-- 8 : Retrieve all the orders where the total_amount exceeds $20
SELECT * FROM Orders WHERE Total_Amount > 20;

-- 9 : List all the Genre's Available in Books
SELECT DISTINCT Genre FROM Books;

-- 10 : Find the book with the lowest stock
SELECT Book_ID,Title,Stock FROM Books ORDER BY Stock LIMIT 1;

-- 11 : Calculate the total revenue generated from all orders
SELECT DISTINCT SUM(Total_Amount) AS Revenue_Generated FROM Orders;

-- 12 : Retrieve the total number of books sold for each genre
SELECT DISTINCT b.Genre, SUM(o.Quantity) AS Total_Sold
FROM Books b
INNER JOIN Orders o
ON b.Book_ID = o.Book_ID;
GROUP BY b.Genre;

-- 13 : Find the average price of the books in 'Fantasy' Genre
SELECT Genre, AVG(Price) AS Average_Price FROM Books WHERE Genre = 'Fantasy' GROUP BY Genre;

-- 14 : List customers who have placed at least 2 orders
SELECT o.Customer_ID,c.Name, COUNT(o.Order_ID) AS ORDER_COUNT
FROM Orders o
JOIN Customers c ON c.Customer_ID = o.Customer_ID
GROUP BY o.Customer_ID,c.Name
HAVING COUNT (Order_ID) >= 2;

-- 15 : Find the most frequently ordered books
SELECT o.Book_ID,b.Title,COUNT(o.Order_ID) AS ORDER_COUNT
FROM Books b
JOIN Orders o ON b.Book_ID = o.Book_ID
GROUP BY o.Book_ID,b.Title
ORDER BY ORDER_COUNT DESC LIMIT 1;

-- 16 : Show the top 3 most expensive books of 'Fantasy' Genre
SELECT Title,Price,Genre FROM Books WHERE Genre = 'Fantasy' ORDER BY Price DESC LIMIT 3;


-- 17 : Retrieve the total quantity of books sold by each author
SELECT b.Author,SUM(o.Quantity) AS Total_Books_Sold
FROM Orders o
JOIN books b ON o.Book_ID = b.Book_ID
GROUP BY b.Author;

-- 18 : List the cities where customers who spent over $30 are located
SELECT DISTINCT c.City,o.Total_Amount
FROM Customers c
JOIN Orders o ON c.Customer_ID = o.Customer_ID
WHERE o.Total_Amount > 30;

-- 19 : Find the customer who spent the most on orders
SELECT c.Name,SUM(o.Total_Amount) AS Total_Spent
FROM Customers c
JOIN Orders o ON c.Customer_ID = o.Customer_ID
GROUP BY c.Name
ORDER BY Total_Spent DESC LIMIT 1;

-- 20 : Calculate the stock remaining after fulfilling all orders
SELECT b.Title,b.Stock,b.Stock - COALESCE(SUM(o.Quantity),0) AS Avalable_In_Stock
FROM Books b
LEFT JOIN Orders o ON b.Book_ID = o.Book_ID
GROUP BY b.Title,b.Stock;
