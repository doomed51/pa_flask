
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import git

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from desktop +_ood++ webhook!'

## route for updating on github push
@app.route('/gitupdate', methods=['POST'])
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

took()
