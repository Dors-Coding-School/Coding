import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show all the emails received"""
    userId = session["user_id"]
    usernameDB = db.execute("SELECT username FROM users WHERE id = ?", userId)
    username = usernameDB[0]["username"]
    emails = db.execute("SELECT * FROM emails WHERE recipient = ?", username)
    return render_template("sent.html", emails=emails)


@app.route("/compose", methods=["GET", "POST"])
@login_required
def compose():
    """Write an email to someone"""
    if request.method == "GET":
        userId = session["user_id"]
        senderDB = db.execute("SELECT username FROM users WHERE id = ?", userId)
        sender = senderDB[0]["username"]
        return render_template("compose.html", sender=sender)
    else:
        sender = request.form.get("sender")
        recipient = request.form.get("recipient")
        subject = request.form.get("subject")
        body = request.form.get("body")

        if not recipient or not subject or not body:
            return apology("Missing fields")

        db.execute("INSERT INTO emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)", sender, recipient, subject, body)

        return redirect("/sent")


@app.route("/sent")
@login_required
def sent():
    """Show history of transactions"""
    userId = session["user_id"]
    usernameDB = db.execute("SELECT username FROM users WHERE id = ?", userId)
    username = usernameDB[0]["username"]
    emails = db.execute("SELECT * FROM emails WHERE sender = ?", username)
    return render_template("sent.html", emails=emails)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/email", methods=["GET", "POST"])
@login_required
def email():
    """View email details."""
    if request.method == "POST":
        emailId = request.form.get("emailId")
        emailDetailDB = db.execute("SELECT * FROM emails WHERE id =?", emailId)
        emailDetail = emailDetailDB[0]
        return render_template("email.html", emailDetail=emailDetail)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST
    if request.method == "POST":

        # Ensure new username was submitted
        username = request.form.get("username")
        if not username:
            return apology("Must create a username")

        # Check if new user name isn't already taken
        check = db.execute("SELECT username FROM users WHERE username = ?", username)
        #if any of the rows returns a match, then username is already taken
        if len(check) > 0:
            return apology("This username is already taken")

        # Ensure new password was submitted
        password = request.form.get("password")
        if not password:
            return apology("Must create a password")

        # Ensure new password is confirmed
        confirm = request.form.get("confirmation")
        if confirm != password:
            return apology("Password doesn't match")

        # Submit password to database, hashed for privacy
        hashed_password = generate_password_hash(request.form.get("password"))

        # Insert new resgistrant into users
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashed_password)

        # Query database for new username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Remember new user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page, where portifolio is.
        return redirect("/")
    # User reached route vie GET
    if request.method == "GET":
        return render_template("register.html")


@app.route("/reply", methods=["GET", "POST"])
@login_required
def reply():
    """Reply the email on email detail view."""
    if request.method == "POST":
        emailId = request.form.get("emailId")
        emailDetailDB = db.execute("SELECT * FROM emails WHERE id =?", emailId)
        emailDetail = emailDetailDB[0]
        return render_template("reply.html", emailDetail=emailDetail)
