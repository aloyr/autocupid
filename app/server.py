from flask import Flask, render_template, request
from vsn import VSN

app = Flask(__name__)

vsn = VSN()

@app.route('/', methods=['GET', 'POST'])
def index():
	matches = None
	msg = None
	vsnid = request.form.get('search')
	if (vsnid != None):
		if (vsn.sanitize(vsnid)):
			matches = vsn.search(vsnid)
		else:
			msg = 'Wrong VSN format entered. Please try again.'
	return render_template('index.html', matches = matches, msg=msg)

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/data')
def datatest():
	return vsn.getTable()

@app.route('/search/<vsnid>')
def searchVSN(vsnid):
	matches = None
	msg = None
	if (vsn.sanitize(vsnid)):
		matches = vsn.search(vsnid)
	else:
		msg = 'Wrong VSN format entered. Please try again.'
	return render_template('search.html', matches=vsn.search(vsnid), msg=msg)

if __name__ == '__main__':
	app.run(debug=True)