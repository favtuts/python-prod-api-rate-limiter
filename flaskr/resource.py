# flaskr/resource.py

from flask import (
    Blueprint, request, jsonify
)

bp = Blueprint('resource', __name__, url_prefix='/resource')

@bp.route('/test', methods=('GET','POST'))
def test():
    if request.method == 'POST':
        response = {'message': 'This was a POST'}
    else:
        response = {'message': 'This was a GET'}
    return jsonify(response), 200

