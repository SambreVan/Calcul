CREATE DATABASE IF NOT EXISTS calculator_db;
USE calculator_db;

CREATE TABLE IF NOT EXISTS operations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operation_type VARCHAR(255) NOT NULL,
    operand1 FLOAT NOT NULL,
    operand2 FLOAT NOT NULL,
    result FLOAT NOT NULL
);
