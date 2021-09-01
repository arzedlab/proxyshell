from app import app
from flask import render_template, request, flash,redirect
from database import Hosts
from main import index_post

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        index_post()