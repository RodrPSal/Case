class Result:
    
    def __init__(self, success, returnValue=None, message=None):
        self.success = success
        self.returnValue = returnValue
        self.message = message