import mysql.connector

mydb = mysql.connector.connect(
        host="mysqldb",
        port="3306",
        user="root",
        passwd="p@ssw0rd1",
        database="inventory"
    )