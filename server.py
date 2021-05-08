"""Server for donations site."""

from flask import (Flask, render_template, request, flash,
                session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/items')
def all_items():
    """View all items."""

    items = crud.get_items()

    return render_template('all_items.html', items=items)




if __name__ == "__main__": 
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)