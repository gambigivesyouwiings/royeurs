from flask import Flask, render_template, request, url_for, flash


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio-details.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

