from . import main

from .. import fd


# @fd.view.route('/test', methods=['get', 'post', 'put', 'delete'])
# def test():
#     return "hello"


@main.route("/")
def index():
    return "micro penis"
