class LLpyException(Exception):
    def __init__(self, msg, full=None):
        super(LLpyException, self).__init__('Exception: ' + msg)
        if full:
            self.full_exc = full
