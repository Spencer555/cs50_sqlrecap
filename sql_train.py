# with sql 
# main key words 
# CREATE, INSERT 
# SELECT
# DELETE ,DROP


# CREATE TABLE 
# CREATE TABLE table (column type, ...); 


# in terminal create dbase called favorites
# sqlite3 favorites.db; 


# .mode csv
# put in csv mode
# import from csv to table 
# .import favorites.csv favorites

# .schema - shows the schema of the dbase table


# SELECT columns FROM table;
# select from a table

# select everything from a table 
# SELECT * From favorites;

# select only a row from table 
# SELECT language From favorites;


# select only a certain number e.g 10 

# SELECT * From favorites LIMIT 10;


# get count of all items
# SELECT COUNT(*)  FROM favorite;


# get count of row items
# if u re going to count rows it s conventional to count everything(*) than individual since its the same 
# SELECT COUNT(languages)  FROM favorite;


#  get count of all distinct items of a row
# SELECT COUNT(DISTINCT(languages))  FROM favorite;


# new keywords
# LIKE
# ORDER BY
# LIMIT
# GROUP BY

# using where language is c
# SELECT COUNT(*) FROM favorite WHERE language = 'C';

# using where language is c and problem is hello world
# SELECT COUNT(*) FROM favorite WHERE language = 'C' AND problem = 'Hello, World';



# group by something and get count of the duplicate
# SELECT language, COUNT(*) FROM favorite GROUP BY language;



# order by count default is ascending u can set to descending DESC;
# SELECT language, COUNT(*) AS n FROM favorite ORDER BY n DESC;


# insert into table
# INSERT INTO table (column, ...) VALUES();
# INSERT INTO table (language, problem) VALUES(sql, hello);


# delete data from table where there is no timestamp
# dont do delete from favorites it would clear the entire dbase
# DELETE FROM favorite WHERE Timestamp IS NULL


# update 
# UPDATE favorites SET language = 'SQL', problem = 'Fiftyville

