#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
import MySQLdb
import sys
#import uwsgi
from flask import Flask
from flask import render_template
#    return render_template('index.html')
#application = Flask(__name__)
application = Flask(__name__)

#data = cursor.fetchall()
#return render_template('db.html', data = data)

@application.route("/")
#def db():
#	connection =  MySQLdb.connect (host = "localhost", user = "root", passwd = "!Giamal76", db = "employees")
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
#connection = MySQLdb.connect (host = "localhost", user = "root", passwd = "!Giamal76", db = "employees")
# prepare a cursor object using cursor() method
#	cursor = connection.cursor ()
# execute the SQL query using execute() method.
#	cursor.execute ("select * from employees.employees where birth_date='1965-02-01' and gender='M' and hire_date>'1990-01-01' order by last_name;")
# fetch all of the rows from the query
def db():
    db = MySQLdb.connect(host = "localhost", user = "appuser", passwd = "!Temp123", db = "employees" )

    cursor = db.cursor()

    cursor.execute("select  first_name,last_name  from employees.employees where birth_date='1965-02-01' and gender='M' and hire_date>'1990-01-01' order by last_name;")
    #data = cursor.fetchall()
    #return render_template('db.html', data = data)

    rows = []

    for row in cursor:
	rows.append(row)
        #print(row)
	#print row[2], row[3]

	#return rows
	data = cursor.fetchall()    
	return render_template('db.html', data = data)
# print the rows
#for row in data :
#	print row[2], row[3]
# close the cursor object
#cursor.close ()
# close the connection
#connection.close ()
#db.close ()
# exit the program
#sys.exit()
if __name__ == '__main__':
    application.run()
