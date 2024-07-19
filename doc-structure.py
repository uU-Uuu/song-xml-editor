import os
import re


from assist import InvalidFilename, FILENAME_REQUIREMENTS


class Workspace:
    """A class to manage workspace within a specified working directory
    
    Attributes:
    - name (str): the workspace name
    - base_directory (str): the base directory where documents will be saved
    - documents (list): a list of XMLDocuments instances in the workspace
    
    Methods:
    - __init__(self, name, base_directory)
    - add_document(self, filename)
      initializes new XMLDoc instance and appends it to the self.documents attribute"""

    def __init__(self, name, base_directory):
        self._name = name
        self._base_directory = base_directory
        self._documents = []

    @property
    def name(self):
        """workspace name getter"""
        return self._name

    @name.setter
    def name(self, new_name):
        """workspace name setter"""
        if new_name:
            self._name = new_name

    @property
    def base_directory(self):
        """workspace base_directory getter"""
        return self._base_directory
    
    @base_directory.setter
    def base_directory(self, new_directory):
        """workspace base_directory setter"""
        if new_directory:
            self._base_directory = new_directory
    
    @property
    def documents(self):
        """workspace documents getter"""
        return self._documents
    
    @documents.setter
    def documents(self, documents_list):
        """workspace documents getter"""
        if documents_list:
            self._documents = documents_list
    

    def add_document(self, filename, path=''):
        """add document to the workspace with filename and path"""
        full_path = os.path.join(self._base_directory, path)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        new_document = XMLDoc(filename, full_path)
        self.documents.append(new_document)




class XMLDoc:
    """XML Document object class
    
    Attributes:
    - filename (str)
    - path (str): relative path
    - title (str, optional): document title
    - key (str, optional): melody key value
    - time_signature (str, optional): time signature value 
    
    Methods:
    - __init__(self, filename, path, title, key, time_signature)
    - create(self)
      creates and saves the document backbone to self.path in the workspace directory
    """

    def __init__(self, filename, path, title='', key='', time_signature=''):
        self.filename = filename
        self.path = path
        self.title = title
        self.key = key
        self.time_signature = time_signature


    @staticmethod
    def filename_validation(filename_to_check, pattern=r'(?=^[a-zA-Z]\w+)(\w+){1,255}(\.xml)?$', extension='.xml', check=False):
        """a static method to validate filename with regex pattern and file extension
        
        Parameters:
        - filename (str): Filename to be validated 
        - pattern (str, optional): regex r'' pattern
            - default r'(?=^[a-zA-Z]\w+)(\w+)(\.xml)?$'
        - extension (str, optional): Indended file extension
            - default '.xml'
        - check (bool): when True returns True if the filename is valid else InvalidFilename Exception
            - default False
        
        Output:
        - when check=False:  valid filename (str) or InvalidFilename Exception
        - when check=True:   True if valid filename or InvalidFilename Exception
        """
        check_filename = re.match(pattern, filename_to_check)
        if check_filename:
            if check_filename.group(2) == extension:
                if check:
                    return True
                valid_filename = filename_to_check
            else:
                valid_filename = filename_to_check + extension
        else:
            raise InvalidFilename(f'Invalid filename: {filename_to_check}\n\tRequirements:\n{FILENAME_REQUIREMENTS}')
        return valid_filename
    

    def create(self, non_empty=False):
        """create and save an xml file with metadata backbone
        
        Parameters:
        - non_empty (bool): when True does not include empty title, key, time_signature in the file
            - default False
        """
        try:
            if XMLDoc.filename_validation(self.filename, check=True):
                self.path = os.path.join(self.path, self.filename)
                try:
                    with open(self._path, 'w') as file:
                        file.write(self.write_metadata_xml(non_empty=non_empty))
                except IOError as _:
                    print(f'Error when trying to save file\n\t {_}')
        except InvalidFilename as e:
            print(e)


    def set_metadata(self, title:str='', key:str='', time_signature:str=''):
        """set title, key and time_signature parameters
        
        Parameters:
        - title (str, optional): default ''
        - key (str, optional): default ''
        - time_signature (str, optional): default ''
        """
        self.title = title if title else self.title
        self.key = key if key else self.key
        self.time_signature = time_signature if time_signature else self.time_signature
    

    def write_metadata_xml(self, version='1.0', encoding='UTF-8', non_empty=False):
        """create a metadata xml string
        
        Parameters:
        - version (str): default '1.0'
        - encoding (str): default 'UTF-8'
        - non-empty (bool): when True does not include attributes (tags) with empty values 
            - default False
        """
        xml_string = f'<?xml version="{version}" encoding="{encoding}"?>\n'
        for attr, value in vars(self).items():
            if not attr.startswith('_'):
                if non_empty:
                    if value:
                        xml_string += f'<{attr}>{value}</{attr}>\n' 
                else:
                    xml_string += f'<{attr}>{value}</{attr}>\n'
        return xml_string
    

    def update_file(self, title:str='', key:str='', time_signature:str=''):
        """overwrite the file with the current state of the object
        
         Parameters:
        - title (str, optional): default ''
        - key (str, optional): default ''
        - time_signature (str, optional): default ''
        """
        try:
            if title or key or time_signature:
                self.set_metadata(title, key, time_signature)
            with open(self._path, 'w') as file:
                file.write(self.write_metadata_xml())
        except IOError as _:
                print(f'Error when trying to update the file\n\t {_}')

    
    def delete_file(self):
        """delete the file from path if exists"""
        if os.path.exists(self.path):
            try:
                os.remove(self.path)
                print(f'File deleted: {self.path}')
            except Exception as _:
                print(f'Error deleting file: {_}')
        else:
            print(f'File not found or does not exit.\n{self.path}')
        

    @property
    def filename(self):
        """document filename getter"""
        return self._filename
    
    @filename.setter
    def filename(self, new_filename:str):
        """document filename setter"""
        try:
            self._filename = XMLDoc.filename_validation(str(new_filename))
        except InvalidFilename as _:
            print(f'Cannot change the filename. {_}')
    
    @property
    def path(self):
        """document path getter"""
        return self._path 

    @path.setter
    def path(self, new_path:str):
        """document path setter"""
        if new_path:
            self._path = str(new_path)


workspace = Workspace('current_workspace', os.getcwd())

workspace.add_document('myxml', 'f')
for doc in workspace.documents:
    doc.create()
    doc.set_metadata('ishikaribanka', 'A minor', '4/4')
    doc.update_file(title='A')



# xml = XMLDoc('myxml', 'f')
# xml.filename = '67'
# print(xml.filename)


