import logging
from flask import request
from main import app
from api_client import handle_location_call


logger = logging.getLogger("my_location")

@app.route('/my-location', methods=['POST'])
def get_location():
    # The data object looks like this
    # {
    # "latitude": float,
    # "longitude": float,
    # "isNearHome": 'true' | 'false'
    # }
    logger.debug(f"Recieved Call: {request.get_json()}")
    data = request.get_json()
    handle_location_call(data['isNearHome'])
    
    return '', 200

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    logger.warning(f"Got unauthorized request: {request.method} {request.remote_addr} {path}")
    ip = request.remote_addr
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    details = f'{ip} /{path} {request.method}'
    write_to_file(details)
    return 'Not Found', 404

def write_to_file(data):
    with open('unauthorized_requests.txt', 'a') as f:
        f.write(data+'\n')