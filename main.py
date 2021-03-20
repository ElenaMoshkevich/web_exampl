from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route("/")
def index():
    return """<html>
    <h1>Привет от приложения Flask Елене!!!!!</h1>
    </html>"""


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=port)
    serve(app,host='0.0.0.0', port=5000 )

