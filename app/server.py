from flask import Flask, render_template
from vsn import VSN

app = Flask(__name__)

vsn = VSN()

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/welcome')
def welcome():
  return render_template('welcome.html')

@app.route('/data')
def datatest():
	return vsn.getTable()

@app.route('/search/<vsnid>')
def searchVSN(vsnid):
	return render_template('search.html', matches=vsn.search(vsnid))

if __name__ == '__main__':
  app.run(debug=True)