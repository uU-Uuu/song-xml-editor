import os
import re
from wsgiref import validate


from xml_utils.utils import InvalidFilename
from xml_utils.constants import FILENAME_REQUIREMENTS
from xml_utils.tags import Melody, Section, MelPhrase, LexPhrase, Syllable, Rest


class Workspace:
    """A class to manage workspace within a specified working directory
    
    Attributes:
    - name (str): the workspace name
    - base_directory (str): the base directory where documents will be saved
    - documents (list): a list of XMLDocuments instances in the workspace
    
    Methods:
    - __init__(self, name, base_directory)
    - add_document(self, filename, path=''):
      initialize new XMLDoc instance and append it to the self.documents attribute
    - add_documents(self, *args):
        - add documents to the workspace (append documents as XMLDoc instances)
    - remove_documents(self, *args):
        - remove documents from the workspace
      """

    def __init__(self, name, base_directory):
        self._name = name
        self._base_directory = base_directory
        if not os.path.exists(self._base_directory):
            os.makedirs(self._base_directory)
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
    
    def add_documents(self, *args):
        """add documents to the workspace (append documents as XMLDoc instances)"""
        for doc in args:
            if isinstance(doc, XMLDoc):
                self._documents.append(doc)

    def add_document(self, filename, path=''):
        """add document to the workspace with filename, path"""
        full_path = os.path.join(self._base_directory, path)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        new_document = XMLDoc(filename, full_path)
        self._documents.append(new_document)
        return new_document
    
    def remove_documents(self, *args):
        """remove documents from the workspace"""
        for doc in args:
            if doc in self._documents:
                self._documents.remove(doc)

    


class XMLDoc:
    """XML Document object class
    
    Attributes:
    - filename (str)
    - path (str): relative path
    - title (str, optional): document title
    - key (str, optional): melody key value
    - time_signature (str, optional): time signature value 
    - melody (Melody): Melody class instance
    
    Methods:
    - __init__(self, filename, path, title, key, time_signature)
    - create(self, non_empty=False):
        - create and save the document backbone to self.path in the workspace directory
    - set_metadata(self, title, key, time_signature):
        - set title, key and time_signature attributes for the instance
    - write_xml(self, starting_with= '', non_empty=False):
        - write an XML string from attributes
    - write_metadata_xml(self, version='1.0', encoding='UTF-8', non_empty=False):
        - create a metadata XML string
    - update_file(self, title:str='', key:str='', time_signature:str=''):
        - overwrite the XML file with the current state of the instance
    - delete_file(self):
        - delete the file from path if exists    
    """

    def __init__(self, filename, path, title='', key='', time_signature=''):
        self._filename = filename
        self.path = path
        self.title = title
        self.key = key
        self.time_signature = time_signature
        self._melody = None


    @staticmethod
    def filename_validation(filename_to_check, 
                            pattern=r'^([a-zA-Z]\w{0,254})(\.xml)?$', 
                            extension='.xml', check=False):
        """a static method to validate filename with regex pattern and file extension
        
        Parameters:
        - filename (str): Filename to be validated 
        - pattern (str, optional): regex r'' pattern
            - default r'(?=^[a-zA-Z]\w+)(\w+)(\.xml)?$'
        - extension (str, optional): Indended file extension
            - default '.xml'
        - check (bool): if True returns True if the filename is valid else InvalidFilename Exception
            - default False
        
        Output:
        - if check=False:  valid filename (str) or InvalidFilename Exception
        - if check=True:   True if valid filename or InvalidFilename Exception
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
        - non_empty (bool): if True does not include empty title, key, time_signature in the file
            - default False
        """
        try:
            if XMLDoc.filename_validation(self.filename, check=True):
                self.path = os.path.join(self.path, self.filename)
                try:
                    with open(self._path, 'w', encoding='utf-8') as file:
                        file.write(self.write_metadata_xml(non_empty=non_empty))
                except IOError as _:
                    print(f'Error when trying to save file\n\t {_}')
        except InvalidFilename:
            raise Exception


    def set_metadata(self, title:str='', key:str='', time_signature:str=''):
        """set title, key and time_signature attributes
        
        Parameters:
        - title (str, optional): default ''
        - key (str, optional): default ''
        - time_signature (str, optional): default ''
        """
        self.title = title if title else self.title
        self.key = key if key else self.key
        self.time_signature = time_signature if time_signature else self.time_signature
    

    def write_xml(self, starting_with= '', ending_with='', non_empty=False):
        """create an XML string from attributes
        
        Parameters:
        - starting_with (str): the beginning of the string (opening tags)
            - default ''
        - ending_with (str): the ending of the string (closing tags)
            - default ''
        - non-empty (bool): if True, does not include attributes (tags) with empty values 
            - default False
        """
        xml_string = starting_with
        for attr, value in self.__dict__.items():
            if not attr.startswith('_'):
                if non_empty:
                    if value:
                        xml_string += f'\t<{attr}>{value}</{attr}>\n'
                else:
                    xml_string += f'\t<{attr}>{value}</{attr}>\n'
        return xml_string + ending_with
    

    def write_metadata_xml(self, version='1.0', encoding='UTF-8', 
                           non_empty=False, closed=True):
        """create a metadata XML string
        
        Parameters:
        - version (str, optional): default '1.0'
        - encoding (str, optional): default 'UTF-8'
        - non-empty (bool, optional): if True does not include attributes (tags) with empty values 
            - default False
        - closed (bool, optional): if False returns xml string and closing tag separately
            - default True
        """
        st_xml_string = f'<?xml version="{version}" encoding="{encoding}"?>\n<doc>\n'
        fin_xml_string = '\n</doc>'

        if not closed:
            return (self.write_xml(starting_with=st_xml_string, non_empty=non_empty), 
                    fin_xml_string)
    
        return self.write_xml(starting_with=st_xml_string, ending_with=fin_xml_string,
                              non_empty=non_empty)
    

    def read_file(self, prettify_indent=True, from_indent='\t', to_indent='   '):
        with open(self._path, 'r', encoding='utf-8') as file:
            data = file.read()
            if prettify_indent:
                try:
                    pretty_data = data.replace(str(from_indent), str(to_indent))
                except TypeError:
                    pass
                else:
                    return f'{pretty_data}\n'
            return data
    
    @staticmethod
    def delete_empty_lines(txt):
        split_txt = txt.splitlines()
        clear_txt = '\n'.join(line for line in split_txt
                              if line.strip() and line.strip('\t'))
        return clear_txt
                

    def update_file(self, title:str='', key:str='', time_signature:str=''):
        """overwrite the file with the current state of the instance
        
         Parameters:
        - title (str, optional): default ''
        - key (str, optional): default ''
        - time_signature (str, optional): default ''
        """
        try:
            if title or key or time_signature:
                self.set_metadata(title, key, time_signature)
            with open(self._path, 'w', encoding='utf-8') as file:
                meta, closing = self.write_metadata_xml(closed=False)
                mel = self.melody.write_xml()
                file.write(f'{meta}{mel}{closing}')
        except IOError as _:
                print(f'Error when trying to update the file\n\t {_}')

    def save_edited_file(self, edited_data):
        edited_path = f'{self._path.split(".xml")[0]}_edited.xml'
        with open(f'{edited_path}', 'w', encoding='utf-8') as file:
            file.write(edited_data)
        return edited_data

    def save_file(self, data):
        with open(self._path, 'w', encoding='utf-8') as file:
            file.write(data)
        return self._path


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

    @property
    def melody(self):
        return self._melody

    @melody.setter    
    def melody(self, melody:Melody):
        if isinstance(melody, Melody):
            self._melody = melody




# syl1 = Syllable('go')
# syl1.add_note('E4', '1/16')

# rest1 = Rest('1/8')

# syl2 = Syllable('me')
# syl2.add_note('A4', '1/16')
# syl2.add_note('E4', '1/8')

# syl3 = Syllable('me', 'ma')
# syl3.add_note('A4', '1/16')
# syl3.add_note('E4', '1/8')

# lp1 = LexPhrase()
# lp1.add_syllable(syl1)
# lp1.add_rest(rest1)
# lp1.add_syllable(syl3)

# lp2 = LexPhrase()
# lp2.add_syllable(syl2)

# mp1 = MelPhrase()
# mp1.add_lex_phrase(lp1)
# mp1.add_lex_phrase(lp2)

# sec1 = Section('A')
# sec1.add_mel_phrase(mp1)

# mel = Melody()
# mel.add_section(sec1)


# w_path = os.path.join(os.getcwd(), 'try')
# work1 = Workspace('Try', w_path)
# os.makedirs(w_path, exist_ok=True)

# doc1 = work1.add_document('tryxml', w_path)
# doc1.set_metadata('Good morning', 'e major', '4/4')

# doc2 = XMLDoc('try2', w_path, 'Hello', 'a minor', '2/2')
# work1.add_documents(doc2)

# doc1.create()
# doc1.melody = mel
# doc1.update_file()
