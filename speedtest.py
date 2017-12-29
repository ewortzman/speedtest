from flask import Flask
app = Flask(__name__)

import string, random
dat = ''
for x in range(0,20*1024*1024):
  dat += random.choice(string.letters+string.digits)

@app.route('/ping')
def ping():
  return ''

@app.route('/data')
def data():
  return dat
