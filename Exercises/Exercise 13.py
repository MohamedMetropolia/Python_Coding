from flask import Flask, json, Response
import mysql.connector

mydatabase = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    database='flight_game')
mycursor = mydatabase.cursor()

app = Flask(__name__)


@app.route('/prime/<num>', methods=['GET'])
def prime_num(num):
    prime = True
    num = int(num)
    if num <= 1:
        return "The prime number must be larger than 1."
    else:
        for i in range(2, num):
            if (num % i) == 0:
                prime = False
                break
        if prime:
            return {"Number": num, "isPrime": prime}
        else:
            return {"Number": num, "isPrime": prime}


@app.route('/airport/<icao>')
def airport(icao):
    try:
        mycursor.execute("""SELECT ident, name, municipality FROM flight_game.airport WHERE ident = %s""", (icao,))
        user = mycursor.fetchall()
        return user

    except ValueError:
        response = {
            "message": "Invalid ICAO code",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
