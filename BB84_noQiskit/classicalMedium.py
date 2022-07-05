from flask import Flask, request

users = {}

app = Flask(__name__)

@app.route('/')
def login():
    name = request.form["name"]
    users[name] = request.remote_addr
    return f"Hi {name}!"








app.run(
    # host = "192.168.0.100",
    host = "localhost",
	port = 5000,
	debug = True,
 )