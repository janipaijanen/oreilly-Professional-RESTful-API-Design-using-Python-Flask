from flask.views import MethodView
from flask import jsonify, request, abort

class PetAPI(MethodView):

    pets = [
        {"id":1, "name": u"mac", "links": [ {"rel": "self", "href": "/pets/1"} ] },
        {"id":2, "name": u"leo",  "links": [ {"rel": "self", "href": "/pets/2"} ] },
        {"id":3, "name": u"brownie", "links": [ {"rel": "self", "href": "/pets/3"} ] }
    ]

    def get(self, pet_id):
        if pet_id:
            # note: should the index
            return jsonify({"pet": self.pets[pet_id -1]}), 200
        else:
            return jsonify({"pets": self.pets}), 200

    def post(self):
        if not request.json or not 'name' in request.json:
            abort(400)
        pet = {
            'id': len(self.pets)+1,
            'name': request.json['name'],
            "links": [ {"rel": "self", "href": "/pets/" + str(len(self.pets)+1)} ]
        }
        self.pets.append(pet)
        return jsonify({'pet': pet}), 201

    def put(self, pet_id):
        if not request.json or not 'name' in request.json:
            abort(400)
        pet = self.pets[pet_id -1]
        pet["name"] = request.json["name"]
        return jsonify({"pet": pet}), 200

    def delete(self, pet_id):
        del self.pets[pet_id -1]
        return jsonify({}), 204
