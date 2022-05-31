class NotFound(Exception):
    code = 404
    text = 'Page Not Found'


class NotAllowed(Exception):
    code = 405
    text = 'HTTP method no allowed'