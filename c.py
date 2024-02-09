from flask import Flask

app = Flask(name)


@app.route('/')
def counter():
    return 'Hello From Sandydev!'
