
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
import git

app = Flask(__name__)
app.config["DEBUG"] = True
comments = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("test_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))

@app.route('/hello_world', methods=["GET"])
def hello_world():
    return 'Hello from desktop +_ood++ webhook!'

## route for updating on github push
#@app.route('/gitupdate', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./')
        origin = repo.remotes.github
        origin.pull()
        return 'Updated PythonAnywhere Successfully', 200

    else:
        return 'Wrong event type', 400



def took():
    repo = git.Repo('./')

    origin = repo.remotes.github
    origin.pull()
    print(origin)

