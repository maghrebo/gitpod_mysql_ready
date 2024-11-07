import mysql.connector
from flask import Flask, jsonify, request

#Connessione al database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

app = Flask(__name__)

#Definizione delle diverse funzioni per il metodo GET

def getAllData():
    mycursor.execute("SELECT * FROM mammiferi")
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

def getRazza(razza):
    query = "SELECT * FROM mammiferi WHERE razza = %s"
    mycursor.execute(query, (razza,))
    rows = mycursor.fetchall()
    return rows


#Indirizzamento delle diverse route che poi richiamano le funzioni

@app.route("/")
def stampaDati():
    data = getAllData()
    return jsonify({"Mammiferi": data})

@app.route("/<razza>")
def stampaRazza(razza):
    data = getRazza(razza)
    return jsonify({"La razza scelta e: ": data})


#-----------------------------------------------------------------
#Prova dell'azione POST

def addAnimale(data):
    query = "INSERT INTO mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    values = (data['nome'], data['razza'], data['peso'], data['eta'])
    mycursor.execute(query, values)
    mydb.commit()
    return mycursor.rowcount

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    if not data:
        return jsonify({'message': 'Nessun dato fornito'}), 400

    required_fields = ['razza', 'nome', 'peso', 'eta']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Dati mancanti o errati'}), 400

    rows_inserted = addAnimale(data)
    if rows_inserted == 1:
        return jsonify({'message': 'Mammifero inserito con successo'}), 201
    else:
        return jsonify({'message': 'Errore durante l inserimento'}), 500

#-----------------------------------------------------------------
#Prova dell'azione DELETE

def deleteMammifero(id):
    query = "DELETE FROM mammiferi WHERE id = %s"
    mycursor.execute(query, (id,))
    mydb.commit()
    return mycursor.rowcount

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    rows_deleted = deleteMammifero(id)
    if rows_deleted == 1:
        return jsonify({'message': 'Mammifero eliminato con successo'}), 200
    else:
        return jsonify({'message': 'Errore durante l\'eliminazione o ID non trovato'}), 404


#-----------------------------------------------------------------
#Prova dell'azione UPDATE

def updateMammifero(id, data):
    query = "UPDATE mammiferi SET Nome_Proprio = %s, Razza = %s, Peso = %s, Eta = %s WHERE id = %s"
    values = (data['nome'], data['razza'], data['peso'], data['eta'], id)
    mycursor.execute(query, values)
    mydb.commit()
    return mycursor.rowcount

@app.route("/update/<id>", methods=["PUT"])
def update(id):
    print(request.json)
    print("ciao")
    data = request.json
    
    required_fields = ['nome', 'razza', 'peso', 'eta']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Dati mancanti'}), 400

    rows_updated = updateMammifero(id, data)
    if rows_updated == 1:
        return jsonify({'message': 'Mammifero aggiornato con successo'}), 200
    else:
        return jsonify({'message': 'Errore durante l aggiornamento o ID non trovato'}), 404
#occhio al json da inserire!!!! se da errore guarda il file json