docker_service 'default' do
  action [:create, :start]
end

docker_image 'sampleapp' do
#tag 'v0.1.0'
source '/home/andrew/dkr'
action :build_if_missing
end

docker_container 'default' do
repo 'sampleapp'
volumes '/run/mysql-default:/var/run/mysqld'
network_mode 'host'
action :run_if_missing
end
