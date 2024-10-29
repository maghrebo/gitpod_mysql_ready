import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Raouf_Database"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM giocatori")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)