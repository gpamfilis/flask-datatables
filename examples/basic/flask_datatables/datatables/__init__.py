from flask import Blueprint

datatables = Blueprint('datatables', __name__, template_folder='templates/datatables')

from . import views
