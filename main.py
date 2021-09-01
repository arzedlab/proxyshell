import csv
import socket 
from app import db
from flask import render_template, request, flash
from database import Hosts
import re



def index_post():
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

def host_create():
    from database import Hosts
    with open('microsoft-exchange.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader =  csv.DictReader(csv_file,delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                print('go')  
            host = Hosts(ip=row['ip'],
                domains=row['domains'],
                hostnames=row['hostnames'],
                org=row['org'],
                version=row['version'], 
                port=row['port'],
                country=row['country'],
                city=row['city']
                )
                
            line_count += 1
            db.session.add(host)
            
        print(f'Processed {line_count} lines.')
        db.session.commit()