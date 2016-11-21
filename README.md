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
