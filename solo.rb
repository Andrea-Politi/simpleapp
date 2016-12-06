
chef_repo_path "/home/user/project" 
cookbook_path "#{chef_repo_path}/cookbooks"
  json_attribs "#{chef_repo_path}/node.json"
  source 'https://supermarket.chef.io'
