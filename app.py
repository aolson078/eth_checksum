from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template('index.html', title="Home", active_page='home')

if __name__ == '__main__':
    app.run()