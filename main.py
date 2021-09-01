import csv
import socket 
from app import db
from flask import render_template, request, flash
from database import Hosts

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