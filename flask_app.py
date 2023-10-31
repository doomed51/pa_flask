
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import git

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="doomed51",
    password="sc4recr0w",
    hostname="doomed51.mysql.pythonanywhere-services.com",
    databasename="doomed51$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("test_page.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()

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

