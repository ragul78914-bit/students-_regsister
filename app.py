from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",   # change if needed
    database="company"
)

cursor = db.cursor()

# Home page (form)
@app.route("/")
def home():
    return render_template("index.html")

# Add employee
@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form["name"]
    age = request.form["age"]
    job = request.form["job"]
    email = request.form["email"]
    password = request.form["password"]

    query = "INSERT INTO employees (name, age, job, email, password) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age, job, email, password)

    cursor.execute(query, values)
    db.commit()

    return redirect("/")

# View employees
@app.route("/employees")
def view_employees():
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    return render_template("employees.html", employees=data)

if __name__ == "__main__":
    app.run(debug=True)