import sqlite3
import pandas as pd

#use SQLite3 to create and connect the process to a new database STAFF
conn = sqlite3.connect('STAFF.db')

#create a table in the database
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']  #columns name


#Read the CSV file
#Since this CSV doesn't contain headers, we can use the keys of the attribute_dict dictionary as a list to assign headers to the data
file_path = r"C:\Users\esraa\Desktop\Python_Projects\IBM\SQLite\INSTRUCTOR.csv"
df = pd.read_csv(file_path, names = attribute_list)


#Loading the data to a table in the database

#if_exists='fail': Default. The command doesn't work if a table with the same name exists in the database.
#if_exists='replace': The command replaces the existing table in the database with the same name.
#if_exists='append': The command appends the new data to the existing table with the same name.

#create a fresh table upon execution ---> if_exists='replace'
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')
# This database can now be used to retrieve the relevant information using SQL queries.


# Running queries on data

#Viewing all the data in the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#Viewing only FNAME column of data
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#Viewing the total number of entries in the table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#appending data to the table
#ID is 100, FNAME, is John, LNAME is Doe, CITY is Paris, CCODE is FR
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)
#append the data to the INSTRUCTOR table
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')


#Viewing the total number of entries in the table after appending data to the table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# close the connection to the database
conn.close()
