create user 'appuser'@'localhost' identified by '!Temp123';
grant select on employees.* to 'appuser'@'localhost';
flush privileges;
