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

#Esecuzione della query per gli animali che pesano più di 2 kg
mycursor.execute("SELECT * FROM mammiferi WHERE peso > 2")

myresult = mycursor.fetchall()

#Print con la funzione di python per CLI
for x in myresult:
  print(x)