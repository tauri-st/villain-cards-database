from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask("app")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///villain.db"

db = SQLAlchemy(app)

@app.route("/")
def hello_world():
  return render_template("villain.html")

app.run(host='0.0.0.0', port=8080)