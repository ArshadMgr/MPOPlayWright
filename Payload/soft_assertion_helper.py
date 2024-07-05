# soft_assertion_helper.py

class SoftAssertionError(Exception):
    pass

class SoftAssertContext:
    def __init__(self):
        self.errors = []

    def soft_assert(self, condition, message=''):
        try:
            assert condition, message
        except AssertionError as e:
            self.errors.append(str(e))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.errors:
            raise SoftAssertionError('\n'.join(self.errors))
