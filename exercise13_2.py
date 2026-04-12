import mariadb
from flask import Flask

app = Flask(__name__)

connection = mariadb.connect(
    host="localhost",
    database="flight_game",
    user="root",
    password="moni2061",
    autocommit=True
)


@app.route('/airport/<icao_code>')
def fetch_airport(icao_code):
    try:
        sql = "SELECT ident AS ICAO, name, municipality AS location FROM airport WHERE ident=%s"
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, (icao_code,))
        response = cursor.fetchone()
        if response is None:
            return {"status": "error", "message": "No airport found"}, 404

        return response

    except Exception:
        return {"status": "error", "message": "Database error occurred"}, 400


@app.errorhandler(404)
def entry_not_found(error):
    return ({"message": "Invalid web address"}), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
