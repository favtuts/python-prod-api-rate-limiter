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