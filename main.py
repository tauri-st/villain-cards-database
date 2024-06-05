from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask("app")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///villain.db"

db = SQLAlchemy(app)


class Villain(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(250), nullable=False)
  interests = db.Column(db.String(250), nullable=False)
  url = db.Column(db.String(250), nullable=False)
  date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return "<Villain " + self.name + ">"


with app.app_context():
  db.create_all()
  db.session.commit()


@app.route("/")
def hello_world():
  return render_template("villain.html")
  
@app.route("/add", methods=["GET"])
def add_villain():
  return render_template("addvillain.html", errors=[])
  
@app.route("/addVillain", methods=["POST"])
def add_user():
  errors = []
  name = request.form.get("name")
  if not name:
    errors.append("Oops! Looks like you forgot a name!")
  description = request.form.get("description")
  if not description:
    errors.append("Oops! Looks like you forgot a description!")
  interests = request.form.get("interests")
  if not interests:
    errors.append("Oops! Looks like you forgot some interests!")
  url = request.form.get("url")
  if not url:
    errors.append("Oops! Looks like you forgot an image!")

app.run(host='0.0.0.0', port=8080)