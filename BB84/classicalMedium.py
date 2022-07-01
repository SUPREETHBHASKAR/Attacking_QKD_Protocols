from flask import Flask, request

app = Flask(__name__)

users = {}

@app.route('/')
def login():
    name = dict(request.form)["name"]
    users[name] = request.remote_addr
    return f"Hi {name}!"


# @app.route('/<name>')
# def show_user(name):
#     # Greet the user
#     return f'Hello {name} !'


app.run(
    # host = "192.168.0.100",
    host = "localhost",
	port = 5000,
	debug = True,
 )