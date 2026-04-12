from flask import Flask

app = Flask(__name__)


@app.route('/prime_number/<int:number>')
def check_prime(number):
    if number <= 1:
        is_Prime = False
    else:
        is_Prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_Prime = False
                break

    return ({
        "Number": number,
        "is_Prime": is_Prime
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
