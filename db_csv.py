import csv

#ip;domains;hostnames;version;org;port;data;country;city

def db_creater():
    with open('microsoft-exchange.csv', mode='r') as csv_file:
        csv_reader =  csv.DictReader(csv_file,delimiter=';')
        line_count = 0
        print(csv_reader)
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'No: {line_count}')
            print(f'\t{row["ip"]} {row["domains"]}')
            line_count += 1
        print(f'Processed {line_count} lines.')