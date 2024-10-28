import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Raouf_Database"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE giocatori (nome VARCHAR(255), cognome VARCHAR(255))")