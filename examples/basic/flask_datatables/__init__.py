from flask import Blueprint, jsonify
from flask.views import MethodView

# from .datatables import datatables
# from .api import api


class FlaskDatatables(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)
        self.module = None

    def init_app(self, app):
        self.module = Blueprint(
            "datatables", __name__, template_folder="templates"
        )
        app.register_blueprint(self.module)

        try:
            self.module.add_url_rule("/test", view_func=Test.as_view('test'), methods=['GET', 'POST', 'PUT', 'DELETE'])
        except Exception as e:
            print(e)

        return self.module
        # self.register_blueprint(app)

    # def register_blueprint(self, app):
    #     self.module = Blueprint(
    #         "datatables", __name__, template_folder="templates"
    #     )
    #     app.register_blueprint(self.module)

    #     try:
    #         self.module.add_url_rule("/test", view_func=Test.as_view('test'), methods=['GET', 'POST', 'PUT', 'DELETE'])
    #     except Exception as e:
    #         print(e)

    #     return self.module

    # def add_view(self):
    #     # print('[--] adding url rule: ', name)
    #     pass
    #     # try:
    #     #     self.module.add_url_rule("/test", view_func=Test.as_view('test'), methods=['GET', 'POST', 'PUT', 'DELETE'])
    #     # except Exception as e:
    #     #     print(e)




class Test(MethodView):

    def get(self):
        return jsonify({"status":"OK"})

    def post(self):
        return jsonify({"status":"OK"})

    def put(self):
        return jsonify({"status":"OK"})

    def delete(self):
        return jsonify({"status":"OK"})
