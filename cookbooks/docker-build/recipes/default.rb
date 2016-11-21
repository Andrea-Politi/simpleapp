docker_service 'default' do
  action [:create, :start]
end

docker_image 'sampleapp' do
source "#{Chef::Config['chef_repo_path']}/dkr"
action :build_if_missing
end

docker_container 'pythonapp' do
repo 'sampleapp'
volumes '/run/mysql-default:/var/run/mysqld'
network_mode 'host'
action :run_if_missing
end
