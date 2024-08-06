
class Tag:
    """A parent class Tag for all XML tags other than title, key and time_signature

    Attributes:
    - tag_name (str): name of the tag
    - depth (int): depth level (the deeper the bigger value, starting from 0)
    - children (list): a list of children tags
    
    Methods:
    - __init__(self, tag_name)
    - write_xml(self, inner='', depth=-1):
        - create an XML string for the tag class instance
    - depth(cls): a classmethod to get the depth values for children tags
      

    """

    _depths = {'melody': 1, 'section': 2, 'melodic_phrase': 3, 
              'lexical_phrase': 4, 'syllable': 5, 'rest': 5
              }

    def __init__(self, tag_name:str):
        self.tag_name = tag_name
        self.depth = Tag._depths[tag_name]
        self.children = []

    def write_xml(self,  inner='', depth=-1):
        """create an XML string for the tag class instance
        
        Parameters:
        - inner(str, optional): a string with children tag XML notation
            - default: ''
            - if not indicated, automatically tries to retrieve children XML string
        - depth(int, optional): depth value which determines the number of \\t in the XML
            - default: -1
            - if not specified, automatically takes self.depth
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
    """A child of the Tag class for tags with attributes <tag attr="value"></tag>

    Methods:
    - write_xml(self, non_empty=True, inner='', depth=-1)
        - create an XML string for the tag with attributes class instance
    """
    
    def write_xml(self, non_empty=True, inner='', depth=-1):
        """create an XML string for the tag with attributes class instance
        
        Parameters:
        - non_empty (bool): if True does not include empty fields
            - default True
        - inner(str, optional): a string with children tag XML notation
            - default: ''
            - if not indicated, automatically tries to retrieve children XML string
        - depth(int, optional): depth value which determines the number of \\t in the XML
            - default: -1
            - if not specified, automatically takes self.depth
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
    """A child of the Tag class for tags with multiple elements
    
    Attributes:
    - tag_name(str): name of the tag
    - multi: storing the names of attributes with mulptiple values

    Methods:
    - __init__(self, tag_name:str, multi)
    - write_xml(self, depth=-1)
        - create an xml string for the instance
    """

    def __init__(self, tag_name:str, multi):
        super().__init__(tag_name)
        self.multi = multi

    def write_xml(self, depth=-1):
        """create an xml string for the tag class instance
        
        Parameters:
        - depth(int, optional): depth value which determines the number of \\t in the XML
            - default: -1
            - if not specified, automatically takes self.depth
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
    """A Tag child class representing the only melody instance within a document
    
    Methods:
    - __init__(self)
    - add_section(self, section):
        - add a Section instance to the children list
    """

    def __init__(self):
        super().__init__('melody')

    def add_section(self, section):
        """add a Section instance into the children list"""
        self.children.append(section)
        


class Section(TagWithAttr):
    """A TagWithAttr child class representing one logical or musical section within a melody  

    Attributes:
    - name(str, optional): name of the section

    Methods:
    - __init__(self, name:str='')
    - add_mel_phrase(self, mel_phrase):
         - add a MelPhrase instance to the children list
    """

    def __init__(self, name:str=''):
        super().__init__('section')
        self.name = name
    
    def add_mel_phrase(self, mel_phrase):
        """add a MelPhrase instance to the children list"""
        self.children.append(mel_phrase)

    def __repr__(self):
        return f'Section: {self.name}'    
    


class MelPhrase(TagWithAttr):
    """A TagWithAttr child class representing one melodic phrase within a section  

    Attributes:
    - id(str): autoincrementing id of the melodic phrase


    Methods:
    - __init__(self)
    - add_lex_phrase(self, lex_phrase):
         - add a LexPhrase instance to the children list
    """
    _mel_ph_count = 0

    
    def __init__(self):
        super().__init__('melodic_phrase')
        MelPhrase._mel_ph_count += 1        
        self.id = MelPhrase._mel_ph_count
 

    def add_lex_phrase(self, lex_phrase):
        """add a LexPhrase instance to the children list"""
        self.children.append(lex_phrase)


class LexPhrase(TagWithAttr):
    """A TagWithAttr child class representing one lexical phrase within a melodic phrase 

    Attributes:
    - id(str): autoincrementing id of the lexical phrase
    - lyrics(str): concatenated lyrics string of children 

    Methods:
    - __init__(self)
    - add_syllable(self, syllable):
         - add a Syllable instance to the children list
    - add_rest(self, rest):
        - add a Rest instance to the children list
    """
    _lex_ph_count = 0


    def __init__(self):
        super().__init__('lexical_phrase')
        LexPhrase._lex_ph_count += 1
        self.id = LexPhrase._lex_ph_count 
        self.lyrics = ''


    def add_syllable(self, syllable):
        """add a Syllable instance to the children list"""
        self.children.append(syllable)
        self.lyrics = ''.join(''.join(syl.lyric) for syl in self.children
                              if isinstance(syl, Syllable))

    def add_rest(self, rest):
        """add a Rest instance to the children list"""
        self.children.append(rest)

    def __repr__(self):
        return f'Lexical Phrase: {self.lyrics}'
    

class Syllable(MultiElTag):
    """A MultiElTag child class typically representing one sung syllable within a lexical phrase

    Attributes:
    - lyric(tuple): lyric syllables
    - notes(list): notes with pitch and duration

    Methods:
    - __init__(self, *args)
        - args* = lyrics syllables
    - add_note(self, pitch:str, duration:str):
        - add a note: pitch and duration    
    - is_melisma(self):
        - check if the syllable has multiple notes = (is a melisma) 
    """

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
    """A MultiElTag child class representing a rest within a lexical phrase
    
    Attributes:
    - duration (tuple): rest duration values
    
    Methods:
    - __init__(self, *args)
        - *args = duration values
    """

    def __init__(self, *args):
        super().__init__('rest', ('duration'))
        self.duration = args
        
    def __repr__(self):
        return f'Rest:  {" - ".join(dur for dur in self.duration)}'
