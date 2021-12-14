#!/usr/bin/env python3

from flask import  Flask 

app = Flask("webserver")

@app.route("/")
def hello():
  return '<html><body><a href="http://localhost:8081\"> Link To App2 </a></body><html>'

app.run(port=8080, host="0.0.0.0")



