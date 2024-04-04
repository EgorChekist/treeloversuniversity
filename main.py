from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_migrate import Migrate
from tech_issues import db, Student


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db.init_app(app)
Migrate(app, db)

with app.app_context():
    db.create_all()

@app.route("/")
def home():

    return render_template("home.html")

@app.route("/auth-form", methods=["GET", "POST"])
def stdnt_frm():
    if request.method == "GET":
        return render_template("auth_form.html")
    elif request.method == "POST":
        name = request.form.get("name")
        lastname = request.form.get("lastname")
        curse = request.form.get("curse")
        level = request.form.get("level")
        faculty = request.form.get("faculty")

        user = Student(name = name, lastname = lastname, curse = curse, level = level, faculty = faculty)
        db.session.add(user)
        db.session.commit()
        return redirect("/great_form")

@app.route("/great_form")
def form():

    return render_template("great_form.html")

@app.route("/listing")
def listing():
    students = Student.query.all()
    return render_template("listing.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
