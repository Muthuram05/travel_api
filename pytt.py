from flask import Flask, request
import json

# some JSON:

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    x = '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    return y
@app.route('/hii', methods=['GET', 'POST'])
def hii():
    x = '{ "name":"hi", "age":3, "city":"New"}'
    y = json.loads(x)
    return y
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        x = str(request.data)
        print(x)
        y  = '{ "name": "hi", "age":3, "city":"New"}'
        y = json.loads(y)
        return y

if __name__ == "__main__":
    app.run(debug=True)