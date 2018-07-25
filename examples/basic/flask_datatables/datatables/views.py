from . import datatables

from flask import render_template

from flask import Blueprint, jsonify

from flask.views import MethodView


# class Test(MethodView):

#     def get(self):
#         return jsonify({"status":"OK"})

#     def post(self):
#         return jsonify({"status":"OK"})

#     def put(self):
#         return jsonify({"status":"OK"})

#     def delete(self):
#         return jsonify({"status":"OK"})
        

# datatables.add_url_rule("/test", view_func=Test.as_view("test"), methods=['GET', 'POST', 'PUT', 'DELETE'])
