from flask import render_template
from . import main_bp


@main_bp.route("/")
def home():
    return render_template("home/home.html")


@main_bp.route("/symptoms")
def symptoms():
    return render_template("home/symptoms.html")


@main_bp.route("/result")
def result():
    return render_template("home/result.html")