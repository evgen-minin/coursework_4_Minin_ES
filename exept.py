class DifaultException(Exception):
    def __init__(self, message):
        self.message = message


class HTTPError(DifaultException):
    pass