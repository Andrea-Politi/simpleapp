#uwsgi --ini app.ini &> /dev/null
service nginx start 
uwsgi --ini app.ini
