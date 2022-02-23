# flaskr/resource.py

from flask import (
    Blueprint, request, jsonify
)

from .core import limiter  # <------------ New line

bp = Blueprint('resource', __name__, url_prefix='/resource')

# Set a default limit of 1 request per second,
# which can be changed granurarly in each route.
limiter.limit('1/second')(bp)      # <------------ New line

@bp.route('/test', methods=('GET','POST'))
def test():
    if request.method == 'POST':
        response = {'message': 'This was a POST'}
    else:
        response = {'message': 'This was a GET'}
    return jsonify(response), 200

