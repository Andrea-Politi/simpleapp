# simpleapp
Project to create a simple webapp which will extract data from a mysql db using python2.7 + uwsgi + flask and nginx inside a docker container based on ubuntu 16.04, importing a dataset from an external repo, everything deployed via chef-solo

INSTALLATION

Clone the repo:

git clone https://github.com/Andrea-Politi/simpleapp

Install Chef binaries:

$ sudo true && curl -L https://www.opscode.com/chef/install.sh | sudo bash

Then edit the 'chef_repo_path' inside the simpleapp/solo.rb with the app path inside your newly created repo (default is: /home/user/git/simpleapp ) and copy it to /etc/chef/solo.rb. Remember to take a backup if already existing:

& vim simpleapp/solo.rb

Save, then:

$ sudo cp simpleapp/solo.rb /etc/chef/

Clone the external cookbooks:

$ cd simpleapp/cookbooks && git clone https://github.com/chef-cookbooks/mysql
$ git clone https://github.com/chef-cookbooks/docker

Launch Chef solo:

$ sudo chef-solo

After is finished, open the browser on your host to:

http://<host_IP>:8000

That's it!

Note1: the app is using Chef to deploy everything, the test was not very clear, it would have been possible to build everything in order to deploy the whole app under Docker, but it seems a bit overkill to me, plus I believe this solution is more elegant.

Note2: the query extract just the values of: 'last_name', 'first_name' and 'emp_no'. Again, the test is not very clear on this point, the "select" statement can be easily changed inside the app.py file (and the docker image rebuilt) to get different results:

mysql> desc employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| emp_no     | int(11)       | NO   | PRI | NULL    |       |
| birth_date | date          | NO   |     | NULL    |       |
| first_name | varchar(14)   | NO   |     | NULL    |       |
| last_name  | varchar(16)   | NO   |     | NULL    |       |
| gender     | enum('M','F') | NO   |     | NULL    |       |
| hire_date  | date          | NO   |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
6 rows in set (0.01 sec)

Note3: having the passwd in clear for the mysql user is not that great, anyway it got just the select grants and can connect only from localhost, so it's not a big issue I believe.


FILES:
