from flask import request, render_template,session,flash,redirect,url_for
from . import auth_bp



@auth_bp.route("/login", methods=["POST"])
def login():
    username=request.form.get("username")
    password=request.form.get("password")

    if not username or not password:
        return render_template("home.html", error="Username and password are required.")
    
    session["username"]=username
    session["password"]=password

    flash("login succesful")

    return redirect(url_for("main.home"))

