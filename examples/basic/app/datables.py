from . import fd


@fd.api.route('/test', methods=['get', 'post', 'put', 'delete'])
def test():
    return "hello"

