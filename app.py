from flask import Flask, jsonify, request
import pyodbc
import collections
import json


# conn = pyodbc.connect('DRIVER={SQL Server};'
#                       'SERVER=tcp:csc3004.database.windows.net,1433;'
#                       'DATABASE=csc3004;UID=csc3004;PWD=Webcrawler3004;')
# cursor = conn.cursor()	
app = Flask(__name__)

@app.route("/")
def hello():
    return "csc3004 web server api"
