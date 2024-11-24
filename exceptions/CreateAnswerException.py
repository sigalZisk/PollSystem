
class CreateAnswerException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AlreadyAnsweredException(CreateAnswerException):
    def __init(self, message):
        self.message = message
        super().__init__(self.message)

