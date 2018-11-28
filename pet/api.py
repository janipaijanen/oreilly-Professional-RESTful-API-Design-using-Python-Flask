from flask.views import MethodView
from flask import jsonify, request, abort

class PetAPI(MethodView):
    pets = [
        {"id":1, "name": u"mac"},
        {"id":2, "name": u"leo"},
        {"id":3, "name": u"brownie"},
    ]

    def get(self):
        return jsonify({"pets": self.pets})
