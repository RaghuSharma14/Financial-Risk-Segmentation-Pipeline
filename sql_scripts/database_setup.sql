-- Create the Database
CREATE DATABASE IF NOT EXISTS portfolio_risk_db;
USE portfolio_risk_db;

-- Create the Table Structure
CREATE TABLE IF NOT EXISTS Customer_Profiles (
    cust_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    credit_score INT,
    annual_income_usd INT,
    monthly_spend_avg INT,
    is_delinquent TINYINT(1), 
    existing_loan_balance INT,
    region VARCHAR(50)
);

-- Insert Sample Data for the Portfolio
INSERT INTO Customer_Profiles VALUES 
(1, 'John Doe', 780, 110000, 4500, 0, 0, 'North'),
(2, 'Jane Smith', 640, 55000, 1200, 1, 15000, 'West'),
(3, 'Michael Ross', 710, 85000, 3000, 0, 5000, 'East'),
(4, 'Harvey Specter', 820, 250000, 15000, 0, 0, 'North'),
(5, 'Louis Litt', 690, 95000, 2500, 0, 45000, 'South'),
(6, 'Rachel Zane', 740, 75000, 2200, 0, 2000, 'West');