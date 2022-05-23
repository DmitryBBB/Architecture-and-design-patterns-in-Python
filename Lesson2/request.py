class Request:
    def __init__(self, environ: dict):
        self.method = environ['REQUEST_METHOD'].lower()
        self.query_params = self._get_query_params(environ)
        self.path = environ['PATH_INFO']
        self.headers = self._get_headers(environ)

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP'):
                headers[key[5:]] = value

        return headers

    def _get_query_params(self, environ):
        query_params = {}
        qs = environ.get('QUERY_STRING')

        if not qs:
            return {}

        qs = qs.split('&')
        for q_str in qs:
            key, value = q_str.split('=')
            if query_params.get(key):
                query_params[key].append(value)
            else:
                query_params[key] = [value]

        return query_params
