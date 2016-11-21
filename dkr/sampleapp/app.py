#!/usr/bin/python
# import modules
import MySQLdb
import sys
from flask import Flask
from flask import render_template
application = Flask(__name__)


@application.route("/")
# define a db connection
def db():
    db = MySQLdb.connect(host = "localhost", user = "appuser", passwd = "!Temp123", db = "employees" )

    cursor = db.cursor()

    cursor.execute("select  first_name,last_name,emp_no  from employees.employees where birth_date='1965-02-01' and gender='M' and hire_date>'1990-01-01' order by last_name;")

    rows = []

    for row in cursor:
        rows.append(row)
#return rows
        data = cursor.fetchall()
        return render_template('db.html', data = data)
# run flask
if __name__ == '__main__':
    application.run()

