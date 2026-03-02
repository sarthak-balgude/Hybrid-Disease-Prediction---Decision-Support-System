from flask import request, render_template,session,flash,redirect,url_for
from . import auth_bp



@auth_bp.route("/login", methods=["POST"])
def login():
    email=request.form.get("email")
    password=request.form.get("password")

    if not email or not password:
        return render_template("home.html", error="Email and password are required.")
    
    session["email"]=email
    session["password"]=password

    flash("login successful")

    return redirect(url_for("main.home"))

