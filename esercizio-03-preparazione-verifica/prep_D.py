import mysql.connector

# Connessione al database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)

mycursor = mydb.cursor()

# Funzione per inserire un animale
def inserisci_animale():
    Nome_Proprio = input("Inserisci il nome dell'animale: ")
    razza = input("Inserisci la razza dell'animale: ")

    # Verifica del peso
    while True:
        peso_input = input("Inserisci il peso dell'animale (in kg): ")
        try:
            peso = int(peso_input)
            break
        except ValueError:
            print("Errore: il peso deve essere un numero intero.")

    # Verifica dell'età
    while True:
        eta_input = input("Inserisci l'età dell'animale (in anni): ")
        try:
            eta = int(eta_input)
            break
        except ValueError:
            print("Errore: l'età deve essere un numero intero.")

    sql = "INSERT INTO mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, (Nome_Proprio, razza, peso, eta))
    mydb.commit()
    print("Animale inserito correttamente!")

#Input della scelta della voglia di stampare alti 5
scelta = input("Vuoi inserire altri 5 animali? (si o no)  ")


# Ciclo per inserire 5 animali in caso la risposta fosse si
if scelta.lower() == "si" :

    for i in range(5):
        inserisci_animale()

        # Chiedi all'utente se vuole inserire un altro animale
        if i < 4:  # Solo se non è la quinta volta
            continua = input("Vuoi inserire un altro animale? (s/n): ").strip().lower()
            if continua != 's':
                print("Interruzione dell'inserimento.")
                break

else:
    print("Hai inserito una parola diversa da si, grazie e arrivederci")

# Verifica degli animali inseriti
print("\nAnimali inseriti:")
mycursor.execute("SELECT * FROM mammiferi")
for (id, nome_proprio, razza, peso, eta) in mycursor.fetchall():
    print(f"ID: {id}, Nome: {nome_proprio}, Razza: {razza}, Peso: {peso}, Età: {eta}")

# Chiusura del cursore e della connessione
mycursor.close()
mydb.close()
