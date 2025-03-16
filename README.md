# 📚 Book Shop Management System

## 📌 Overview
The **Book Shop Management System** is a simple Python-based project that allows users to manage books and customers in a bookshop using a MySQL database.

## 🚀 Features
- 📖 **Add Books & Customers**
- 🔍 **Display Book & Customer Records**
- ❌ **Delete Books & Customers**
- ✏️ **Update Book Availability & Customer Details**
- 🛡 **Secure Queries (Prevent SQL Injection)**
- 🔄 **Error Handling for Better Stability**

## 🛠 Technologies Used
- **Python** (for the main program logic)
- **MySQL** (for database management)
- **MySQL Connector for Python**

## 📂 Database Setup
1. **Create Database**
```sql
CREATE DATABASE book_shop;
USE book_shop;
```
2. **Create Books Table**
```sql
CREATE TABLE Books (
    s_no VARCHAR(10) PRIMARY KEY,
    book_name VARCHAR(255),
    availability_of_book INT,
    price INT
);
```
3. **Create Customers Table**
```sql
CREATE TABLE customer (
    customer_name VARCHAR(255),
    age INT,
    place VARCHAR(255),
    book_bought VARCHAR(255)
);
```

## 📥 Installation
### 1️⃣ Install MySQL Connector
```sh
pip install mysql-connector-python
```
### 2️⃣ Run the Python Script
```sh
python bookshop.py
```

## 📖 How to Use
1. Run the script and choose an option from the menu.
2. Enter details as prompted.
3. View, add, update, or delete records as needed.
4. Exit when done.

## 🛡 Security & Improvements
- ✅ **Uses parameterized queries** to prevent SQL injection.
- ✅ **Includes error handling** to prevent crashes.
- ✅ **Improved code structure** for readability and maintainability.
