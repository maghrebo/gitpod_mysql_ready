import mysql.connector

#Connessione al database locale proprio su quello in cui stiamo lavorando "Animali"
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

#Impostazione della query
sql = "INSERT INTO mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
#Impostazione dei valori
animali = [
    ('Fido', 'Labrador', 30, 5),
    ('Micio', 'Gatto domestico', 4, 3),
    ('Pippo', 'Beagle', 10, 4),
    ('Leo', 'Siamese', 5, 2),
    ('Coco', 'Golden Retriever', 28, 6)  
    ]

#Esecuzione della query insieme ai valori
mycursor.executemany(sql, animali)

mydb.commit()
#Output della buon riuscita dell'inserimento dei dati
print(mycursor.rowcount, "tutti i dati sono stati inseriti")