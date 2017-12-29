from flask import Flask
app = Flask(__name__)

with open('junk.data') as f:
  dat = f.read()

@app.route('/ping')
def ping():
  return ''

@app.route('/data')
def data():
  return dat
