import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Raouf_Database"
)

mycursor = mydb.cursor()

sql = "INSERT INTO giocatori (nome, cognome) VALUES (%s, %s)"
val = ("ciro", "sgabbio")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "dati inseriti")