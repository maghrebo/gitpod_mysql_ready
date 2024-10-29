import mysql.connector

#Connesione al database Animali
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

#Creazione del cursore di comando sul database
mycursor = mydb.cursor()

#Esecuzione della query
mycursor.execute("SELECT * FROM mammiferi")

myresult = mycursor.fetchall()

#Print con la funzione di python per CLI
for x in myresult:
  print(x)