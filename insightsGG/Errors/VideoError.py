class MissingArgumentError(Exception):
    def __init__(self, message):
        super().__init__(message)

class FailureToCreateVod(Exception):
    def __init__(self, message):
        super().__init__(message)

class VodNotAnalyzed(Exception):
    def __init__(self, message):
        super().__init__(message)
