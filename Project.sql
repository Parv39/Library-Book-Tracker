CREATE DATABASE library;
USE library;

CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(50),
  author VARCHAR(50),
  price FLOAT
);

INSERT INTO books VALUES
(101, 'Python Basics', 'John Smith', 450),
(102, 'Data Structures', 'Alice Brown', 500),
(103, 'DBMS Concepts', 'John Smith', 400),
(104, 'Algorithm Design', 'Mark Lee', 550),
(105, 'AI Essentials', 'Alice Brown', 600);