from flask import Flask, session, redirect, render_template, url_for
app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def index():
    if not 'visits' in session:
        session['visits'] = 1
    else:
        session['visits'] +=1
    return render_template("index.html")

@app.route("/count", methods = ["GET", "POST"])
def counter():
    session['visits'] +=1
    return redirect("/")

@app.route("/destroy_session")
def clear():
    session.clear()
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run(debug=True)

