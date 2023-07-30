from flask import request
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def parse_request():
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
