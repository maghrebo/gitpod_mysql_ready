import mysql.connector

# Connessione al database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)

#Creazione del cursore
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


def visualizzare_animali():
    print("\nAnimali inseriti:")
    mycursor.execute("SELECT * FROM mammiferi")
    for (id, nome_proprio, razza, peso, eta) in mycursor.fetchall():
        print(f"ID: {id}, Nome: {nome_proprio}, Razza: {razza}, Peso: {peso}, Età: {eta}")


#def eliminare_animale():
    
    
    


scelta = int(input("Ecco il menu utente, scegli un numero \n  1 Inserimento di un nuovo animale \n  2 Visualizzare tutti gli animali \n  3 Elimanzione di un animale \n  4 Modificare un animale \n  Inserisci qui la tua scelta: "))

if scelta == 1:
    inserisci_animale()
elif scelta == 2:
    visualizzare_animali()
elif scelta == 3:
    elimare_animale()
elif scelta == 4:
    modificare_animale()
else :
    print("Hai inserito un numero non valido! ")