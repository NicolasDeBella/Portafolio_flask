import mysql.connector

def connectionDB():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456789",
        database = "porfolio"
    )

    if mydb:
        print ("Conexion exitosa")
    else:
        print ("Error  en la conexión")
    return mydb