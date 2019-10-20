from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "flask works!"

@app.route('/about')
def about():
    return "This is about page"

if __name__ == '__main__':
    app.run(port=8080, debug=True)
