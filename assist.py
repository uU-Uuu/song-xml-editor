import re


FILENAME_REQUIREMENTS = """\t - starting from lowercase or uppercase alphabetic characters
\t - allowed: a-z A-Z 0-9 _\n\t - extension: optional"\n\t - maximum length: 255 characters"""


class InvalidFilename(Exception):
    """Raised when filename does not match predetermined regex and/or extension"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


   
