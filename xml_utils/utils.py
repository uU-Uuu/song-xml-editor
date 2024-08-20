import re


class InvalidFilename(Exception):
    """Raised when filename does not match predetermined regex and/or extension"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


   
