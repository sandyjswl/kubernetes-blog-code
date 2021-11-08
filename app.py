from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/check')
def vote():
    return "Hello World!"



if __name__ == '__main__':
        app.run(port=5000, debug=True, host='0.0.0.0')