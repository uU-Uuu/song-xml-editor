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
      initializes new XMLDoc instance and appends it to the self.documents attribute
      """

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
    

    def write_xml(self, starting_with= '', non_empty=False):
        """create an xml string
        
        Parameters:
        - starting_with (str): the beginning of the string
            - default ''
        - non-empty (bool): if True, does not include attributes (tags) with empty values 
            - default False
        """
        xml_string = starting_with
        for attr, value in vars(self).items():
            if not attr.startswith('_'):
                if non_empty:
                    if value:
                        xml_string += f'<{attr}>{value}</{attr}>\n'
                else:
                    xml_string += f'<{attr}>{value}</{attr}>\n'
        return xml_string
    

    def write_metadata_xml(self, version='1.0', encoding='UTF-8', non_empty=False):
        """create a metadata xml string
        
        Parameters:
        - version (str): default '1.0'
        - encoding (str): default 'UTF-8'
        - non-empty (bool): if True does not include attributes (tags) with empty values 
            - default False
        """
        xml_string = f'<?xml version="{version}" encoding="{encoding}"?>\n'
        return self.write_xml(starting_with=xml_string, non_empty=non_empty)


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


class Tag:

    _depths = {'melody': 0, 'section': 1, 'melodic-phrase': 2, 
              'lexical-phrase': 3, 'syllable': 4, 'rest': 4
              }

    """an XML tag parent class"""
    def __init__(self, tag_name:str):
        self.tag_name = tag_name
        self.depth = Tag._depths[tag_name]
        self.children = []

    def write_xml(self,  inner='', depth=-1):
        """create an xml string for the tag class instance
        
        Parameters:
        - *args: attributes of the class that are collections
            - allowed data types: 
                - list, tuple, set
                - the above ones with dict elements
            - by default Syllable.lyric, Syllable.notes, Rest.duration
        """

        curr_depth = depth if depth >= 0 else self.depth
        tab_l, tab_r = '\t' * curr_depth, '\t' * curr_depth
        if not inner:
            inner = '\n'.join(el.write_xml(depth=el.depth) for el in self.children)

        attr_string = ''
        sep = ['', ' '][attr_string != '']
        xml_string = f'{tab_l}<{self.tag_name}{sep}{attr_string}>' \
                     + f'\n{inner}\n' \
                     + f'{tab_l}</{self.tag_name}>{tab_r}' 
        return xml_string
    
    @classmethod
    def depths(cls):
        return cls._depths

    
class TagWithAttr(Tag):
    """a child of the Tag class of tags with attributes
    
    <tag attr="value"></tag>
    """
    
    def write_xml(self, non_empty=True, inner='', depth=-1):
        """create an xml string for the tag with attributes class instance
        
        Parameters:
        - non_empty (bool): if True does not include empty fields
            - default True
        """

        tag_depth = depth if depth >= 0 else self.depth
        tab_l, tab_r = '\t' * tag_depth, '\t' * (tag_depth + 1)

        if not inner:
            inner = '\n'.join(el.write_xml(depth=el.depth) for el in self.children)

        attr_string = ''
        for attr, value in vars(self).items():
            if not attr.startswith('_') \
                    and attr not in ('tag_name', 'depth', 'multi', 'children'):
                if non_empty:
                    if value:
                        attr_string += f' {attr}="{value}"'
                else:
                    attr_string += f' {attr}="{value}"'
        xml_string = f'{tab_l}<{self.tag_name}{attr_string}>' \
                     + f'\n{inner}\n' \
                     + f'{tab_l}</{self.tag_name}>{tab_r}' 
        return xml_string
    
class MultiElTag(Tag):

    def __init__(self, tag_name, multi):
        super().__init__(tag_name)
        self.multi = multi

    def write_xml(self, depth=-1):
        """create an xml string for the tag class instance
        
        Parameters:
        """
        tag_depth = depth if depth >= 0 else self.depth
        tab_l, tab_r = '\t' * tag_depth, '\t' * (tag_depth + 1)

        xml_string = f'{tab_l}<{self.tag_name}>\n{tab_r}'
        for attr, value in self.__dict__.items():
            if not attr.startswith('_') \
                    and attr not in ('tag_name', 'depth', 'multi', 'children'):
                if attr in self.multi:
                    for el in value:

                        if isinstance(el, dict):
                            for key, val in el.items():
                                xml_string += f'<{key}>{val}</{key}>\n{tab_r}'
                        else:
                            xml_string += f'<{attr}>{el}</{attr}>\n{tab_r}'

                else:
                    xml_string += f'<{attr}>{value}</{attr}>\n{tab_r}'

        xml_string = xml_string[:-1] + f'</{self.tag_name}>'
        return xml_string
    


class Melody(Tag):
    """a class representing the only melody instance within a document"""

    def __init__(self):
        super().__init__('melody')

    def add_section(self, section):
        self.children.append(section)
        


class Section(TagWithAttr):
    """a class representing one logical or musical section within a melody"""

    def __init__(self, name:str=''):
        super().__init__('section')
        self.name = name
    
    def add_mel_phrase(self, mel_phrase):
        self.children.append(mel_phrase)

    def __repr__(self):
        return f'Section: {self.name}'    
    


class MelPhrase(Tag):
    """a class representing one melodic phrase within a section"""

    def __init__(self, mel_p_id:str=''):
        super().__init__('melodic-phrase')
        self.id = mel_p_id

    def add_lex_phrase(self, lex_phrase):
        self.children.append(lex_phrase)


class LexPhrase(TagWithAttr):
    """a class representing one lexical phrase within a melodic phrase"""

    _lex_ph_count = 0

    def __init__(self):
        super().__init__('lexical-phrase')
        LexPhrase._lex_ph_count += 1
        self.id = LexPhrase._lex_ph_count 
        self.lyrics = ''


    def add_syllable(self, syllable):
        self.children.append(syllable)
        self.lyrics = ''.join(''.join(syl.lyric) for syl in self.children
                              if isinstance(syl, Syllable))

    def add_rest(self, rest):
        self.children.append(rest)

    def __repr__(self):
        return f'Lexical Phrase: {self.lyrics}'
    

class Syllable(MultiElTag):
    """a class typically representing one sung syllable within a lexical phrase"""

    def __init__(self, *args):
        super().__init__('syllable', ('lyric', 'notes'))
        self.lyric = args
        self.notes = []

    def add_note(self, pitch:str, duration:str):
        """add a note: pitch and duration

        Parameters:
        - pitch (str): C2, A3, E4, B7, ...
        - duration (str): 1/1, 1/2, 1/4, 1/8, 1/16, ...
        """
        self.notes.append({'pitch': pitch, 'duration': duration})

    def is_melisma(self):
        """check if the syllable has multiple notes = (is a melisma)"""
        return len(self.notes) > 1       

    def __repr__(self):
        notes_repr = ', '.join(note['pitch'] + ' - ' + note['duration'] 
                               for note in self.notes)
        lyric_repr = ''.join(lyr for lyr in self.lyric)
        return f'Syllable: {lyric_repr}  {notes_repr}'


class Rest(MultiElTag):
    """a class representing a rest within a lexical phrase"""

    def __init__(self, *args):
        super().__init__('rest', ('duration'))
        self.duration = args
        
    def __repr__(self):
        return f'Rest:  {" - ".join(dur for dur in self.duration)}'



syl1 = Syllable('go')
syl1.add_note('E4', '1/16')

rest1 = Rest('1/8')

syl2 = Syllable('me')
syl2.add_note('A4', '1/16')
syl2.add_note('E4', '1/8')

syl3 = Syllable('me', 'ma')
syl3.add_note('A4', '1/16')
syl3.add_note('E4', '1/8')

lp1 = LexPhrase()
lp1.add_syllable(syl1)
lp1.add_rest(rest1)
lp1.add_syllable(syl3)

lp2 = LexPhrase()
lp2.add_syllable(syl2)

mp1 = MelPhrase()
mp1.add_lex_phrase(lp1)
mp1.add_lex_phrase(lp2)

sec1 = Section('A')
sec1.add_mel_phrase(mp1)

mel = Melody()
mel.add_section(sec1)
