import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from passlib.apps import custom_app_context as pwd_context

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Homepage when you're logged in
@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Create a table for index
    rows = db.execute("SELECT symbol, SUM(shares) FROM transactions WHERE user_id=:user_id GROUP BY symbol HAVING SUM(shares) > 0", user_id=session["user_id"])

    # Creates a place to save the informations
    holdings = []
    all_total = 0

    for row in rows:
        stock = lookup(row['symbol'])
        sum_value = (stock["price"] * row["SUM(shares)"])
        holdings.append({"symbol": stock["symbol"], "name": stock["name"], "shares": row["SUM(shares)"], "price": usd(stock["price"]), "total": usd(sum_value)})
        all_total += stock["price"] * row["SUM(shares)"]

    rows = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
    cash = rows[0]["cash"]
    all_total += cash

    return render_template("index.html", holdings=holdings, cash=usd(cash), all_total=usd(all_total))

# Display a form for the user to type in what stock they want to buy
# and also handling the logic of actually purchasing a stock
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure stock was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        # Ensure shares was submitted
        elif not request.form.get("shares"):
            return apology("must provide shares", 403)

        # Ensure shares is greater than 0
        elif int(request.form.get("shares")) < 0:
            return apology("must provide a valid number of shares", 403)

        # Ensure shock exists
        if not request.form.get("symbol"):
            return apology("must provide an existing symbol", 403)

        # Lookup function
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)

        # Value of transaction
        shares = int(request.form.get("shares"))
        transactionb = shares * stock['price']

        # Check if user has enough cash for transaction
        user_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = user_cash[0]["cash"]

        # Subtract user_cash by value of transaction
        updt_cash = cash - transactionb

        if updt_cash < 0:
            return apology("you do not have enough cash", 403)

        # Update how much left in his account (cash) after the transaction
        db.execute("UPDATE users SET cash=:updt_cash WHERE id=:id", updt_cash=updt_cash, id=session["user_id"]);
        # Update de transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)", user_id=session["user_id"], symbol=stock['symbol'], shares=shares, price=stock['price'])
        flash("Bought!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


# Display the history of all the transactions
@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT symbol, shares, price, transacted FROM transactions WHERE user_id=:user_id", user_id=session["user_id"])
    for i in range(len(transactions)):
        transactions[i]["price"] = usd(transactions[i]["price"])
    return render_template("history.html", transactions=transactions)

# CS50 already did for me!!
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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure name of stock was submitted
        if not request.form.get("symbol"):
            return apology("must provide stock symbol")

        # Use the lookup function
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)

        # Check if stock is valid
        if stock == None:
            return apology("Stock symbol not valid", 400)

        # If its valid
        else:
            return render_template("quoted.html", stockSpec = {'name': stock['symbol'], 'price': usd(stock['price'])})

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure password was submitted
        elif not request.form.get("password_confirm"):
            return apology("must provide password confirmation", 403)

        # Ensure confirmation password is equal to password
        elif request.form.get("password") != request.form.get("password_confirm"):
            return apology("password dont match", 403)
        try:
            # Add into db
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

        except:
            # Check if its unique
            return apology("username is already registered", 403)

        # Remember the user
        session["user_id"] = new_user

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure stock was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        # Ensure shares was submitted
        elif not request.form.get("shares"):
            return apology("must provide shares", 403)

        # Ensure shares is greater than 0
        elif int(request.form.get("shares")) < 0:
            return apology("must provide a valid number of shares", 403)

        # Ensure shock exists
        if not request.form.get("symbol"):
            return apology("must provide an existing symbol", 403)

        # Lookup function
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)

        rows = db.execute("SELECT symbol, SUM(shares) FROM transactions WHERE user_id=:user_id GROUP BY symbol HAVING SUM(shares) > 0", user_id=session["user_id"])

        # Value of transaction
        shares = int(request.form.get("shares"))
        for row in rows:
            if row["symbol"] == symbol:
                if shares > row["SUM(shares)"]:
                    return apology("you're doing something wrong", 403)

        transaction = shares * stock['price']

        # Check if user has enough cash for transaction
        user_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = user_cash[0]["cash"]

        # Subtract user_cash by value of transaction
        updt_cash = cash + transaction

        # Update how much left in his account (cash) after the transaction
        db.execute("UPDATE users SET cash=:updt_cash WHERE id=:id", updt_cash=updt_cash, id=session["user_id"]);
        # Update de transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)", user_id=session["user_id"], symbol=stock['symbol'], shares= -1 * shares, price=stock['price'])
        flash("Sold!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        rows = db.execute("SELECT symbol FROM transactions WHERE user_id=:user_id GROUP BY symbol HAVING SUM(shares) > 0", user_id=session["user_id"])
        return render_template("sell.html", symbols = [row["symbol"] for row in rows])


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
