# from flask_featureflags import FeatureFlag
from flask import Blueprint
from flask import Blueprint, jsonify
from flask.views import MethodView
from flask_login import LoginManager
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_datatables import FlaskDatatables
from flask_googlemaps import GoogleMaps
# # TODO: find a way to bypass the CORS package.
# from flask_cors import CORS
# from flask_wtf.csrf import CsrfProtect
fd = FlaskDatatables()
# csrf = CsrfProtect()
bootstrap = Bootstrap()
# feature_flags = FeatureFlag()

db = SQLAlchemy()


gm = GoogleMaps(key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'

    app.config['FLASK_CONFIG'] = config_name

    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    bootstrap.init_app(app)

    db.init_app(app)

    fd.init_app(app)

    gm.init_app(app)

    login_manager.init_app(app)
    # print('take')
    # for rule in app.url_map.iter_rules():
    #     print rule

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/mana')
    
    from app.googlemaps import gmaps as gmaps_blueprint
    app.register_blueprint(gmaps_blueprint, url_prefix='/gmaps')

    # from flask_datatables.datatables import datatables as datatables_blueprint
    # app.register_blueprint(datatables_blueprint, url_prefix='/datatables')
    
    # datatables_blueprint.add_url_rule("/test", view_func=Test.as_view("test"), methods=['GET', 'POST', 'PUT', 'DELETE'])

    # print(fd.module)

    # @app.route('/dd')
    # def dd():
    #     return 'micro vagina'

    # hey = fd.register_blueprint(app)

    # fd.add_view()
    print(app.url_map)
    print('[-]  list of blueprints')

    for rule in app.url_map.iter_rules():
        print rule

    return app


class Test(MethodView):

    def get(self):
        return jsonify({"status":"OK"})

    def post(self):
        return jsonify({"status":"OK"})

    def put(self):
        return jsonify({"status":"OK"})

    def delete(self):
        return jsonify({"status":"OK"})
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
