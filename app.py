from flask import Flask, render_template

from modules.citation import Citation

app = Flask(__name__)


@app.route('/')
def index():
    citation = Citation(50)
    citation.pay(40)
    return render_template("index.html", data=citation.balance)


if __name__ == "__main__":
    app.run()
