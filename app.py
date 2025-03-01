from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Ana Sayfa</h1>"

@app.route("/hakkimda")
def hakkimda():
    return render_template("hakkimda.html")

if __name__ == "__main__":
    app.run(debug=True)
