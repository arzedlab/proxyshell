from flask.helpers import url_for
from app import app
from flask import render_template, request, flash,redirect
from database import Hosts
import socket
import re

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        search = request.form.get('search')
        ip_pattern = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        if bool(re.findall(ip_pattern,search)):
            if Hosts.query.filter_by(ip=search).first():
                print(search)
                host = Hosts.query.filter_by(ip=search).first()
                if search == host.ip:
                    result = [host.ip,host.domains,host.version,host.org,host.port,host.country,host.city]
                    return render_template('result.html',result=result, host=host)
                else:
                    flash('Good! Not in the database.')
                    return render_template('index.html')
            else:
                flash('Good! Not in the database.')
                return render_template('index.html')
        else:
            try:
                ip_host = socket.gethostbyname(search)
                host = Hosts.query.filter_by(ip=ip_host).first()
                if host == None:
                    flash('Good! Not in the database.')
                    return render_template('index.html')
                elif ip_host == host.ip:
                    #ip;domains;hostnames;version;org;port;data;country;city
                    result = [host.ip,host.domains,host.version,host.org,host.port,host.country,host.city]
                    return render_template('result.html',result=result, host=host)
                else:
                    flash('Good! Not in the database.')
                    return render_template('index.html')
            except:
                flash('Invalid domain name.')
                return render_template('index.html')
@app.errorhandler(404)
def not_found(e):
  return redirect(url_for('index'))