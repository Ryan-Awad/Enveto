from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/about")
def about():
    return render_template("aboutpage.html")

if __name__ == "__main__":
    app.run(debug=True)