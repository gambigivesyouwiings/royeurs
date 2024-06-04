from flask import Flask, render_template, request, url_for, flash


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/expertise")
def expertise():
    return render_template("expertise.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/tech")
def tech():
    return render_template("techcompanies.html")


@app.route("/influencers")
def influencers():
    return render_template("influencers.html")


@app.route("/finance")
def finance():
    return render_template("finance.html")


@app.route("/luxury")
def luxury():
    return render_template("luxury.html")


@app.route("/blog1")
def blog1():
    return render_template("blog1.html")


@app.route("/blog2")
def blog2():
    return render_template("blog2.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")


@app.route("/politicians")
def politicians():
    return render_template("politicians.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/hero")
def hero():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

