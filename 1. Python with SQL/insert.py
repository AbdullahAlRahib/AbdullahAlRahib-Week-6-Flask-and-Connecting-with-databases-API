import mysql.connector

# import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)

mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_table values(123,'Rahim', 23.5)" )
mycursor.execute("insert into test2.test_table values(123,'Rahim', 23.5)" )
mycursor.execute("insert into test2.test_table values(123,'Rahim', 23.5)" )
mycursor.execute("insert into test2.test_table values(123,'Rahim', 23.5)" )
mycursor.execute("insert into test2.test_table values(123,'Rahim', 23.5)" )
mydb.commit()
mydb.close()



