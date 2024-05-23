from flask import Flask, render_template, request
from checksum import check_sum

app = Flask(__name__)

@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
	return render_template('index.html')

@app.route('/display', methods=("GET", "POST"), strict_slashes=False)
def display():
	valid = False
	if request.method == "POST":
		address = request.form.get('address_input')
		valid = check_sum(address)
	return render_template('display.html', valid=valid)


if __name__ == '__main__':
	app.run()