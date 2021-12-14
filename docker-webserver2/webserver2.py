#!/usr/bin/env python3

from flask import  Flask 

app = Flask("webserver")

@app.route("/")
def hello():
  return '<html><body><a href="http://localhost:8080\"> Link To App1 </a></body><html>'

app.run(port=8081, host="0.0.0.0")



