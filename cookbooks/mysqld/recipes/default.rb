mysql_service 'default' do
  version '5.7'
  bind_address '0.0.0.0'
  port '3306'
  data_dir '/var/lib/mysql'
  initial_root_password 'Ch4ng3me'
  action [:create, :start]
end

