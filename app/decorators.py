from functools import wraps
from flask import request, jsonify
import datetime

from app.models import App, Access

def app_required(f):
    @wraps(f)
    def decorated_function(*args, **kvargs):
        #if request.headers.get('X-APP-ID') is None:
        #    return jsonify({}), 403

        app_id = request.headers.get('X-APP-ID')
        app_token = request.headers.get('X-APP-TOKEN')
        #app_secret = request.headers.get('X-APP-SECRET')
        #print (app_id, app_secret)

        if app_id is None or app_token is None:
            return jsonify({}), 403

        app = App.objects.filter(app_id=app_id).first()
        if not App:
            return jsonify({}), 403

        access = Access.objects.filter(app=app).first()
        if not access:
            return jsonify({}), 403

        if access.token != app_token:
            return jsonify({}), 403

        if access.expires < datetime.datetime.utcnow():
            return jsonify({'error': 'TOKEN_EXPIRED'}), 403

        return f(*args, **kvargs)
    return decorated_function
