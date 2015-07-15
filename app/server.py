from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('kitchen_sink.html')

@app.route('/welcome')
def welcome():
  return render_template('welcome.html')

@app.route('/testpage')
def testpage():
  return render_template('test.html')

if __name__ == '__main__':
  app.run(debug=True)