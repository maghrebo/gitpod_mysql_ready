import mysql.connector
from flask import Flask, jsonify

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

def addAnimale():
    query = ""