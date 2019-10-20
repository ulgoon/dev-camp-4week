# How to work with flask

1. `pip install flask`
2. Create new file `server.py`
3. flask init with server.py

```python
from flask import Flask


app = Flask(__name__)
@app.route('/')
def index():
    return "flask works!"

if __name__ == '__main__':
    app.run(port=8080, debug=True)
```

4. add route controller into server.py

```python
@app.route('/about')
def about():
    return "This is about page"
```

5. add render template

```python
from flask import render_template

def index():
    return render_template("index.html")
```
