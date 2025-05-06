from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from calculator_db import CalculatorDB

auth = Blueprint("auth", __name__)
db = CalculatorDB()

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = db.validate_user(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if db.register_user(username, password):
            flash("Registration successful. Please login.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash("Username already exists", "danger")
    return render_template("register.html")

@auth.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))
