import mysql.connector
from flask import Flask, jsonify

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

app = Flask(__name__)

def getAllData():
    mycursor.execute("SELECT * FROM mammiferi")
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

def getRazza():
    query = "SELECT * FROM mammiferi WHERE razza = %s"
    mycursor.execute(query, (razza,))
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

@app.route("/")
def stampaDati():
    data = getAllData()
    return jsonify({"Mammiferi": data})

@app.route("/<razza>")
def stampaRazza(razza):
    data = getRazza(razza)
    return jsonify({"Mammiferi": data})



# Da modificare personlizzando per il mio database degli animali (mammiferi)












@app.route("/getAllDataInHtml")
def getAllDataClash():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

@app.route("/air_transport")
def airTransport():
    condizione = "Air"
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit where Transport = %s", (condizione,))
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

@app.route("/epic_units")
def epicUnits():
    condizione = "Epic"
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit where Rarity = %s", (condizione,))
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

@app.route("/count_x2")
def countX2():
    condizione = "x2"
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit where Count = %s", (condizione,))
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

@app.route("/target_ground")
def targetGround():
    condizione = "Ground"
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit where Target = %s", (condizione,))
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result