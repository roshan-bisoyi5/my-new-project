mport mysql.connector  
mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="dbpython")   
mycursor=mysqldb.cursor()
mycursor.execute("create table student(roll INT,name VARCHAR(255), marks INT)") 
try:  
   mycursor.execute("UPDATE student SET name='Ramu', marks=100 WHERE roll=1")#Execute SQL Query to update record
   mysqldb.commit() 
   print('Record updated successfully...')   
except:   
mysqldb.rollback() 
try:   
   mycursor.execute("DELETE FROM student WHERE roll=3")#Execute SQL Query to detete a record   
   mysqldb.commit() # Commit is used for your changes in the database  
   print('Record deteted successfully...')  
except:  
mysqldb.rollback()
mysqldb.close()