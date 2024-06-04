from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask("app")

@app.route("/")
def hello_world():
  return render_template("villain.html")

app.run(host='0.0.0.0', port=8080)