from flask import Flask, render_template, request, redirect, url_for, session
from calculator_db import CalculatorDB
from auth import auth

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Change this to something secure
app.register_blueprint(auth)

db = CalculatorDB()

def login_required(view_func):
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        return view_func(*args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    result = None
    user_id = session["user_id"]
    if request.method == "POST":
        try:
            a = float(request.form["num1"])
            b = float(request.form["num2"])
            op = request.form["operation"]
            result = db.calculate(user_id, op, a, b)
        except Exception as e:
            result = f"Error: {e}"

    history = db.read_all(user_id)
    return render_template("index.html", result=result, history=history, username=session["username"])

@app.route("/delete/<int:record_id>")
@login_required
def delete(record_id):
    db.delete(record_id, session["user_id"])
    return redirect(url_for("index"))

@app.route("/update/<int:record_id>", methods=["POST"])
@login_required
def update(record_id):
    try:
        new_result = float(request.form[f"new_result_{record_id}"])
        db.update(record_id, new_result, session["user_id"])
    except:
        pass
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

