# python-prod-api-rate-limiter
Reproducible production-ready API with rate-limiter using Python Flash. More details on blog post: https://www.favtuts.com/build-a-production-ready-api-with-rate-limiter-in-15-minutes/


# setup environment

Create virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```

Install necessary libraries:
```
pip install flask
pip install flask-limiter
pip install gunicorn
pip freeze > requirements.txt
```

# run flash development

```
FLASK_APP=flaskr flask run
```

Test endpoints
```
> curl localhost:5000/test
> curl -XPOST localhost:5000/resource/test
> curl localhost:5000/resource/test
```

# run docker container

```
docker build -t prod-api .
docker run --rm -p 5000:5000 prod-api
```

# use Memcached service for production setup

Pull and run memcached container
```
docker pull memcached
docker run --rm -it --network host memcached
```

Check memcached service in new terminal
```
telnet localhost 11211
```

Install `pymemcache` library to communicate with Memcached service
```
pip install pymemcache
pip freeze > requirements.txt
```

Re-run Prod-API with `--network` options
```
docker build -t prod-api .
docker run --rm --network host prod-api
```