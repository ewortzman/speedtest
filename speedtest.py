from flask import Flask
import os
app = Flask(__name__)

with open('junk.data') as f:
  dat = f.read()

@app.route('/ping')
def ping():
  return ''

@app.route('/data')
def data():
  return dat


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(port=port)
