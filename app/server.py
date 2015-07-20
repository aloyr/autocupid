import random
from flask import Flask, render_template, request, session, redirect, url_for
from vsn import VSN
from string import ascii_letters, digits

app = Flask(__name__)
app.secret_key = ''.join([random.choice(ascii_letters+digits) for i in range(32)])

vsn = VSN()

@app.route('/', methods=['GET', 'POST'])
def index():
	matches = None
	msg = None
	vsnid = None
	vsnid_post = request.form.get('search')
	if (vsnid_post != None):
		session['vsnid'] = vsnid_post
		return redirect(url_for('index'))
	if ('vsnid' in session.keys()):
		vsnid = session['vsnid']
		session['msg'] = str(vsn.search(vsnid))
		if (vsn.sanitize(vsnid)):
			matches = vsn.search(vsnid)
		else:
			msg = 'Wrong VSN format entered. Please try again.'
	return render_template('index.html', matches=matches, msg=msg, session=str(session), vsnid=vsnid)

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