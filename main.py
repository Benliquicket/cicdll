import git
from flask import Flask, render_template, request

from modules.citation import Citation

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./')
        origin = repo.remotes.origin
        repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return '', 200
    else:
        return '', 400


@app.route('/')
def index():
    citation = Citation(50)
    citation.pay(40)
    return render_template(
        "index.html",
        fine=citation.fine,
        balance=citation.balance,
        status=citation.status
    )


if __name__ == "__main__":
    app.run(debug=True)
