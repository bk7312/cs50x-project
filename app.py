from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# activate the environment
# terminal $ . .venv/bin/activate

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        if request.form.get("reset") == "reset":
            session.clear()
            message = "Game reset done, please feel free to play again."
        return render_template("index.html", message=message)
    
    else:
        if session.get("win"):
            message = "...and you won! So what's next? You could always reset the game and play again if you want."
        elif session.get("user_created"):
            message = "Congrats on creating a username and password, onwards to the login page!"
        else:
            message = "Don't have a username and password? Find a way to register!"

        return render_template("index.html", message=message)


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("login.html", message="Must enter a valid username.")
        
        username = request.form.get("username")

        if session.get("user_created") and session["username"] == username and not request.form.get("password"):
            session["win"] = True
            return render_template("win.html")
                
        return render_template("login.html", message="Must enter a valid username/password.")

    else:
        if session.get("user_created"):
            message = "Congrats on creating a username and password. Now for the final challenge, login and win the game! You still remember your username and password right?"
        else:
            message = "Don't have a username and password? Find a way to register!"

        return render_template("login.html", message=message)


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        if not request.form.get("validate"):
            return render_template("register.html", message="Looks like something went wrong, let's start over!")
        
        type = request.form.get("validate").lower()


        match type:
            case "username":
                if not request.form.get("username"):
                    return render_template("register.html", message="Must enter a valid username")
                
                username = request.form.get("username")

                if len(username) == 16:
                    session["username"] = username
                    return render_template("register_pwd.html", message="Congrats on getting that username!")
                
                return render_template("register.html", message="Username must be exactly 16 characters long.")
            

            case "password":
                if not request.form.get("password") and not request.form.get("confirm"):
                    return render_template("register_survey.html", message="Congrats on entering an empty password!")
                
                return render_template("register_pwd.html", message="Please find a way to submit a blank password.")
            

            case "survey":
                if not request.form.get("survey"):
                    return render_template("register_survey.html", message="Please choose a color.")
                
                color = request.form.get("survey")

                if color.lower() == 'pink':
                    return render_template("register_em.html", message="Glad to know you like pink!")
                
                return render_template("register_survey.html", message="Please select pink.")
            

            case "email":
                if not request.form.get("email"):
                    return render_template("register_em.html", message="Please enter your email.")
                
                email = request.form.get("email")

                if email == '#me&email*net':
                    return render_template("register_disagree.html", message="What a unique email address!")
                
                return render_template("register_em.html", message="Please enter the correct email.")
            

            case "agree":
                if not request.form.get("terms"):
                    return render_template("register_disagree.html", message="Please tick the box.")
                
                return render_template("register_disagree.html", message="Please disagree.")


            case "disagree":
                if not request.form.get("terms"):
                    return render_template("register_disagree.html", message="Please tick the box.")
                
                session["user_created"] = True

                return render_template("register_ok.html", message="Congrats on registering!")


            case _:
                return render_template("register.html", message="Looks like something went wrong, let's start over!")
        
    else:
        return render_template("register.html", message="Congrats on reaching the registration page!")


@app.route("/about")
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404