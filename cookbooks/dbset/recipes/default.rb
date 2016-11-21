git "/tmp/dbset/" do
  repository "git://github.com/datacharmer/test_db"
  reference "master"
  action :sync
end

#ENV["path"] = '/tmp/dbset/'
Dir["/tmp/dbset/"].each do |path|
execute "sql files" do
command "cd #{path} && mysql -S /run/mysql-default/mysqld.sock < employees.sql"
end
end


execute "create appuser" do
  command "touch /tmp/appuser.lock && mysql -S /run/mysql-default/mysqld.sock < #{Chef::Config['chef_repo_path']}/appuser.sql"
  not_if "test -f /tmp/appuser.lock"
end
