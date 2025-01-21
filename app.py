import os

from cs50 import SQL
from datetime import datetime, timedelta
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

from helpers import apology


# Configure application
app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///todo.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
#@login_required
def index():

    if not session.get("name"):
        return redirect("/login")

    if request.method == "POST":

        user_id = session["name"]

        # Add the user's entry into the database
        date = request.form.get("date")
        topic = request.form.get("topic")
        desc = request.form.get("desc")
        if not topic:
            return apology("no topic given")
        if not desc:
            return apology("no description given")
        if not date:
            return apology("no date given")
        #db.execute("INSERT INTO todo (date, topic, desc) VALUES (?, ?, ?)", date, topic, desc)
        db.execute("INSERT INTO todo (date, topic, desc, user_id) VALUES (?, ?, ?, ?)", date, topic, desc, user_id)

        return redirect("/")

    else:
        message = ""
        color = "green"

        # TODO: Display the entries in the database on index.html
        user_id = session["name"]

        data = db.execute("SELECT date, topic, desc FROM todo WHERE user_id = (?) ORDER BY date asc", user_id)
        disp = db.execute("SELECT message, color, topic, desc FROM display")

        #if not disp:
        db.execute("DELETE FROM display")
            #for row in disp:
                #db.execute("DELETE FROM display WHERE desc=(?)", row["desc"])
        now = datetime.now()
        for row in data:
            topic = row["topic"]
            desc = row["desc"]
            date = row["date"]

            date = datetime.strptime(date,'%Y-%m-%d')

            diff = date - now
            color = "green"
            days = int(diff.days) + 1
            #hours = int(diff.hours)
            #minutes = int(diff.minutes)
            #if weeks > 0:
             #   message = f"{weeks} to go"
            #elif weeks < 0:
            #    message = f"{weeks} ago"
            #    color = "red"
            if days > 0:
                message = f"{days} day(s) to go"
                color = "green"
            elif days < 0:
                message = f"{days} day(s) ago"
                color = "red"
            else:
                message = "today"
                color = "red"
            #elif hours > 0:
            #    message = f"{hours} to go"
            #elif hours < 0:
            #    message = f"{hours} ago"
            #    color = "red"
            #elif minutes > 0:
            #    message = f"{minutes} to go"
            #elif minutes < 0:
            #    message = f"{minutes} ago"
             #   color = "red"
            db.execute("INSERT INTO display (message, color, topic, desc) VALUES (?,?,?,?)", message, color, topic, desc)

        disp = db.execute("SELECT message, color, topic, desc FROM display LIMIT 10;")
        return render_template("index.html", disp=disp)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route("/done", methods=["POST"])
def done():

    # erase task from database
    topic = request.form.get("topic")
    if id:
        db.execute("DELETE FROM todo WHERE topic = (?)", topic)
    return redirect("/")
