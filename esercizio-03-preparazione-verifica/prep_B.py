import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
animali = [
    ('Fido', 'Labrador', 30, 5),
    ('Micio', 'Gatto domestico', 4, 3),
    ('Pippo', 'Beagle', 10, 4),
    ('Leo', 'Siamese', 5, 2),
    ('Coco', 'Golden Retriever', 28, 6)  
    ]

mycursor.executemany(sql, animali)

mydb.commit()

print(mycursor.rowcount, "tutti i dati sono stati inseriti")