import os


from assist import filename_validation, InvalidFilename


class Workspace:
    """A class to manage workspace within a specified working directory
    
    Attributes:
    - name (str): the workspace name
    - base_directory (str): the base directory where documents will be saved
    
    Methods:
    - __init__(self, name, base_directory)"""

    def __init__(self, name, base_directory):
        self._name = name
        self._base_directory = base_directory

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name:
            self._name = new_name

    @property
    def base_directory(self):
        return self._base_directory


class XMLDoc:
    """XML Document object class
    
    Attributes:
    - filename (str)
    - path (str): relative path
    - title (str): document title
    - key (str): melody key value
    - time_signature (str): time signature value 
    
    Methods:
    - __init__(self, filename, path)
    - create(self)
      creates and saves the document backbone to self.path in the workspace directory
    """

    def __init__(self, filename, path):
        self._filename = filename
        self._path = path
        self._title = None
        self._key = None
        self._time_signature = None


    def create(self):
        try:
            self._filename = filename_validation(self._filename)
            self._path = os.path.join(self._path, self._filename)
            try:
                with open(self._path, 'w') as file:
                    pass
            except IOError as _:
                print(f'Error when trying to save file\n\t {_}')
        except InvalidFilename as e:
            print(e)


    @property
    def filename(self):
        """document filename getter"""
        return self._title
    
    # filename setter not working
    @filename.setter
    def filename(self, new_filename:str):
        """document filename setter"""
        try:
            self._filename = filename_validation(str(new_filename))
        except InvalidFilename as _:
            print(f'Cannot change the filename. {_}')
    
    @property
    def path(self):
        """document path getter"""
        return self._path        
    
    @property
    def title(self):
        """document title getter"""
        return self._title
    
    @title.setter
    def title(self, new_title:str):
        """document title setter"""
        if new_title:
            self._title = new_title
    
    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, new_key:str):
        """document key setter"""
        if new_key:
            self._key = str(new_key)
    
    @property
    def time_signature(self):
        """document time_signature getter"""
        return self._time_signature
    
    @time_signature.setter
    def time_signature(self, new_time_signature):
        """document time_signature getter"""
        if new_time_signature:
            self._time_signature = new_time_signature


workspace = Workspace('try', os.getcwd())
print(workspace._base_directory)


xml = XMLDoc('myxml.xml', 'f')

# filename setter not working