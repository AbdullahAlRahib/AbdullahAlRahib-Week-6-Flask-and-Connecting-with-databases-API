import mysql.connector

# import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)

mycursor = mydb.cursor()
mycursor.execute("select c1,c2 from test2.test_table" )
for i in mycursor:
    print(i)
mydb.close()



