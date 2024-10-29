import mysql.connector

#Connessione al database locale
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

#Qua creiamo il database Animali nella macchina locale
mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")

#Ricconessione al database proprio Animali
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

#Qua facciamo la creazione della tabella sottostante nel database animali
mycursor.execute("CREATE TABLE IF NOT EXISTS mammiferi (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, Nome_Proprio VARCHAR(255), Razza VARCHAR(255), Peso INT, Eta INT)")