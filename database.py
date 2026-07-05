# Database management system 

# Database: a place where data are stored, retrieved and managed
# DBMS -  a digital system that managed databases
# Relational DBMS (SQL)
# 1. it works with a structured data (Tabular form)
# 2. tables are relational via a key 

# user table
# id(pk) --- name ---- email      
# 1         bola        baol@gma   
# 2.        Kola        ka@g       

# profile table
# id      dob       address     user_id(fk)
# 1       20 jun     Lagos          1

# orders table
# id --- item --- qty --- total price --- user_id(fk)
# 1     wig         1       50k             1
# 2     Cloth       2       100k            1

# roles table 
# id      Name 
# 1.        Admin
# 2.        Cashier
# 3.        Inventory manager

# user role table
# id  user_id    role_id
# 1    1            1
# 2    1            2
# 3    1            3
# 4    2            2


# types of relationship:-
# 1. one-to-one
# 2. one-to-many
# 3. many-to-many 

# examples - MySQL, Oracle, PostgreSQL, SQLLITE

# categories query
# 1. DDL - Data Definition Language
# CREATE, ALTAR, DROP, TRUNCATE

# 2. DML - Data manipulation language
# INSERT, UPDATE, DELETE

# 3. DQL - Data Query Language
# SELECT  




# Non-relational DBMS (NoSQL)
# example - firebase realtime db, mongodb
# [
#     {
#         'name'
#     }
# ]


import mysql.connector as sql

conn = sql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="password",
    database="may2026"  # add this after creating your database
)

mycursor = conn.cursor()


# query = "CREATE DATABASE may2026"

# id, fullname, email, password, account_no, balance, address, created_at


# query = """CREATE TABLE users(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     fullname VARCHAR(50),
#     email VARCHAR(50) UNIQUE,
#     password VARCHAR(100),
#     account_no VARCHAR(10) UNIQUE,
#     balance FLOAT(10, 2),
#     address TEXT,
#     created_at DATETIME DEFAULT CURRENT_TIMESTAMP
# )
# """


# query = "ALTER TABLE users DROP COLUMN account_no"
# query = "ALTER TABLE users ADD COLUMN account_no VARCHAR(10) AFTER password"
# query = "ALTER TABLE users CHANGE account_no account_number VARCHAR(10) UNIQUE"


# query = "DROP DATABASE may2026"
# query = "DROP TABLE users"

# mycursor.execute(query)