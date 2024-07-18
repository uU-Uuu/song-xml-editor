import re


FILENAME_REQUIREMENTS = """\t - starting from lowercase or uppercase alphabetic characters
\t - allowed: a-z A-Z 0-9 _\n\t - extension: optional"""


class InvalidFilename(Exception):
    """Raised when filename does not match predetermined regex and/or extension"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



def filename_validation(filename, pattern=r'(?=^[a-zA-Z]\w+)(\w+)(\.xml)?$', extension='.xml'):
    """validate filename with regex pattern and extension
    
    Parameter:
    - filename (str): Filename to be validated 
    - pattern (str, optional): regex r'' pattern
        - default r'(?=^[a-zA-Z]\w+)(\w+)(\.xml)?$'
    - extension (str, optional): Indended file extension
        - default '.xml'

    """
    check_filename = re.match(pattern, filename)
    if check_filename:
        if check_filename.group(2) == extension:
            valid_filename = filename
        else:
            valid_filename = filename + extension
    else:
        raise InvalidFilename(f'Invalid filename: {filename}\n\tRequirements:\n{FILENAME_REQUIREMENTS}')
    return valid_filename

        