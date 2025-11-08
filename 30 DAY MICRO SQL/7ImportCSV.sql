DROP TABLE IF EXISTS Vehicles;
CREATE TABLE Vehicles(
	Year INT,
	Month_Name VARCHAR(50),
	Date DATE,
	State VARCHAR(50),
	Vehicle_Class VARCHAR(40),
	Vehicle_Category VARCHAR(40),
	Vehicle_Type VARCHAR(40),
	EV_Sales_Quantity INT
);

SELECT * FROM Vehicles;

-- Importing a csv file into sql
\Vehicles (Year,Month_Name,Date,State,Vehicle_Class,Vehicle_Category,Vehicle_Type,EV_Sales_Quantity)
FROM 'C:\Users\princ\ALL PROGRAMS\EV Adoption Project\EV_Dataset.csv'
DELIMITER ','
CSV HEADER;