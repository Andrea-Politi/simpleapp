root = File.absolute_path(File.dirname(__FILE__))

chef_repo_path "/home/andrew/project" 
cookbook_path "#{chef_repo_path}/cookbooks"
  json_attribs "#{chef_repo_path}/node.json"
  source 'https://supermarket.chef.io'
