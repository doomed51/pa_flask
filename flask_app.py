
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
#import test as tst
import main as mn

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from desktop - webhook!'

@app.route('/test')
def test():
    #tst.run()
    doc = mn.load()
    return doc

