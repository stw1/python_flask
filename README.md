# python_flask
Python Flask gunicorn


based on the guide 
* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04

## Steps ##
* source web_nlp_env/bin/activate
* pip install gunicorn flask
* To launch the app
.* gunicorn --bind 0.0.0.0:8000 wsgi



## 520 Bad Gateway ##
* Most likely due to permissions
* Check nginx logs /var/log/nginx/error.lgo
* Check audit.log under /var/log/audit/audit.log
* Configure selinux
** setsebool -P httpd_can_network_connect 1

