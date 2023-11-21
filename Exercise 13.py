# -1

from flask import Flask, Response
import json

app = Flask(__name__)


def is_prime(number):
    number = int(number)
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


@app.route('/check_prime/<int:number>')
def check_prime(number):
    number = int(number)
    prime_status = is_prime(number)
    response = {
        "Number": int(number),
        "isPrime": is_prime(number)
    }

    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=200)
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

# -2

