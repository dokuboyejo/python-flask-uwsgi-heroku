# python-flask-uwsgi-heroku

Build
```
python3 -m venv ./venv
source venv/bin/activate
pip3 install -r build/requirements.txt
```

Execute via uwsgi
```
venv/bin/uwsgi --ini build/uwsgi.ini  --log-master
check running port using `netstat -pltn | grep wsg`

curl -XGET http://127.0.0.1:<port>
```

Execute directly
```
export PYTHONPATH="$PYTHONPATH:." && python codes/wsgi_bootstrap.py

curl -XGET http://127.0.0.1:5000
```
