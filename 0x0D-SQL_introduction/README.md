# 0x0D. SQL - Introduction
---
## Description

This project in the High Level Programming series is about:
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

## Files
---
File|Task
---|---
0-list_databases.sql | script that lists all databases of my MySQL server.
1-create_database_if_missing.sql | script that creates the database hbtn_0c_0
2-remove_database.sql | script that deletes the database hbtn_0c_0
3-list_tables.sql | script that lists all the tables of a database
4-first_table.sql | script that creates a table called first_table in the current database
5-full_table.sql | script that prints the full description of the table first_table from the database hbtn_0c_0
6-list_values.sql | script that lists all rows of the table first_table from the database hbtn_0c_0
7-insert_value.sql | script that inserts a new row in the table first_table (database hbtn_0c_0) 
8-count_89.sql | script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0
9-full_creation.sql | script that creates a table second_table in the database hbtn_0c_0 my MySQL server and add multiples rows
10-top_score.sql | script that lists all records of the table second_table of the database hbtn_0c_0
11-best_score.sql | script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0
12-no_cheating.sql | script that updates the score of Bob to 10 in the table second_table
13-change_class.sql | script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0
14-average.sql | script that computes the score average of all records in the table second_table of the database hbtn_0c_0
15-groups.sql | script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
16-no_link.sql | script that lists all records of the table second_table of the database hbtn_0c_0
100-move_to_utf8.sql | script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
101-avg_temperatures.sql | script that displays the average temperature (Fahrenheit) by city ordered by temperature 
102-top_city.sql | script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
103-max_state.sql | script that displays the max temperature of each state (ordered by State name)

## Directories
---
Directory Name | Description
---|---
0x0D-SQL_introduction | Main directory with all the main SQL files

## Note
All files is executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)

## Author
Heindrick Cheung