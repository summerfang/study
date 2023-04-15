from flask import Flask

import json
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/widgets")
def widgets():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        passwd="p@ssw0rd1",
        database="inventory"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM widgets")
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    results = cursor.fetchall()
    json_data=[]
    for result in results:
        json_data.append(dict(zip(row_headers,result)))

    cursor.close()
    return json.dumps(json_data)

@app.route("/initdb")
def db_init():
    my_db = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1"
    )
    cursor = my_db.cursor()

    cursor.execute("DROP DATABASE IF EXISTS inventory")
    cursor.execute("CREATE DATABASE inventory")
    cursor.close()


    my_db = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory")
    cursor = my_db.cursor()
    cursor.execute("DROP TABLE IF EXISTS widgets")
    cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
    cursor.close()

    return "Database initialized"

if __name__ == "__main__":
    app.run(host='0.0.0.0')