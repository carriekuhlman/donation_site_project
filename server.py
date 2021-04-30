"""Server for donations site."""

from flask import Flask 

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True)