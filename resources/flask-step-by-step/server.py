from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "flask works!"

if __name__ == '__main__':
    app.run(port=8080, debug=True)
