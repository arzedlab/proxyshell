from re import DEBUG
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLITE_MAX_EXPR_DEPTH'] = 2000
db = SQLAlchemy(app)




if __name__ == '__main__':
    from view import *
    app.run(debug=True)
