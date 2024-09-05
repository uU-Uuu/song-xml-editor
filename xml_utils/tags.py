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
    _swapped = {val: key for key, val in _depths.items()}

    def __init__(self, tag_name:str):
        self.tag_name = tag_name
        self.depth = Tag._depths[tag_name]
        self.children = []
        self.parent = self.get_parent(tag_name)

    def write_xml(self,  inner='', depth=-1, indent='\t'):
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
        # tab_l, tab_r = '\t' * curr_depth, '\t' * curr_depth
        tab_l, tab_r = indent * curr_depth, indent * curr_depth
        if not inner:
            inner = '\n'.join(el.write_xml(depth=el.depth, indent=indent) for el in self.children)

        attr_string = ''
        sep = ['', ' '][attr_string != '']
        xml_string = f'{tab_l}<{self.tag_name}{sep}{attr_string}>' \
                     + f'\n{inner}\n' \
                     + f'{tab_l}</{self.tag_name}>{tab_r}' 
        return xml_string
    
    def write_xml_plain(self):
        pass
    
    def add_child(self, child):
        self.children.append(child)

    def delete_child(self, child):
        try:
            self.children.remove(child)
        except ValueError:
            pass
    
    def delete_child_recursive(self, rm_child):
        try:
            self.children.remove(rm_child)
        except ValueError:
            map(lambda el: el.delete_child(rm_child), self.children)
        

    def give_parent(self):
        from xml_utils.constants import PARENTS_FACTORY
    
        return PARENTS_FACTORY.get(self.depth - 1)

    def from_xml(self):
        pass
    
    @classmethod
    def depths(cls):
        return cls._depths
    
    @classmethod
    def get_parent(cls, tag_name):
        depth = cls._depths[tag_name]
        return cls._swapped.get(depth - 1)
        
    
class TagWithAttr(Tag):
    """A child of the Tag class for tags with attributes <tag attr="value"></tag>

    Methods:
    - write_xml(self, non_empty=True, inner='', depth=-1)
        - create an XML string for the tag with attributes class instance
    """
    
    def write_xml(self, non_empty=True, inner='', depth=-1, indent='\t'):
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
        # tab_l, tab_r = '\t' * tag_depth, '\t' * (tag_depth + 1)
        tab_l, tab_r = indent * tag_depth, indent * (tag_depth + 1)

        if not inner:
            inner = '\n'.join(el.write_xml(depth=el.depth, indent=indent) for el in self.children)

        attr_string = ''
        for attr, value in vars(self).items():
            if not attr.startswith('_') \
                    and attr not in ('tag_name', 'depth', 'multi', 'children', 'parent'):
                if non_empty:
                    if value or value == 0:
                        attr_string += f' {attr}="{value}"'
                else:
                    attr_string += f' {attr}="{value}"'
        xml_string = f'{tab_l}<{self.tag_name}{attr_string}>' \
                     + f'\n{inner}\n' \
                     + f'{tab_l}</{self.tag_name}>{tab_r}' 
        return xml_string
    
    def write_xml_plain(self):
        attr_string = ''
        for attr, value in vars(self).items():
            if not attr.startswith('_') \
                    and attr not in ('tag_name', 'depth', 'multi', 'children', 'parent'):
                attr_string += f' {attr}="{value}"'
        xml_string = f'<{self.tag_name}{attr_string}>\n' \
                      + f'</{self.tag_name}>'
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

    def write_xml(self, depth=-1, indent='\t'):
        """create an xml string for the tag class instance
        
        Parameters:
        - depth(int, optional): depth value which determines the number of \\t in the XML
            - default: -1
            - if not specified, automatically takes self.depth
        """
        tag_depth = depth if depth >= 0 else self.depth
        # tab_l, tab_r = '\t' * tag_depth, '\t' * (tag_depth + 1)
        tab_l, tab_r = indent * tag_depth, indent * (tag_depth + 1)

        xml_string = f'{tab_l}<{self.tag_name}>\n{tab_r}'
        for attr, value in self.__dict__.items():
            if not attr.startswith('_') \
                    and attr not in ('tag_name', 'depth', 'multi', 'children', 'parent'):
                if attr in self.multi:
                    for el in value:

                        if isinstance(el, dict):                        
                            for key, val in el.items():
                                if not val:
                                    val = ''
                                xml_string += f'<{key}>{val}</{key}>\n{tab_r}'
                        else:
                            xml_string += f'<{attr}>{el}</{attr}>\n{tab_r}'

                else:
                    xml_string += f'<{attr}>{value}</{attr}>\n{tab_r}'

        xml_string = xml_string[:-1] + f'</{self.tag_name}>'
        return xml_string
    
    def write_xml_plain(self):
        return self.write_xml(depth=0)


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

    def values_(self):
        return ''        


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
    
    def values_(self):
        return self.name
    


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
        self.id = str(MelPhrase._mel_ph_count)
 

    def add_lex_phrase(self, lex_phrase):
        """add a LexPhrase instance to the children list"""
        self.children.append(lex_phrase)

    def values_(self):
        return str(self.id)
    
    def __repr__(self):
        return f'Musical Phrase {self.id}'

    @classmethod
    def reset_counter(cls, init_value=0):
        try:
            if init_value >= 0:
                cls._mel_ph_count = int(init_value)
        except:
            pass



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
        self.id = str(LexPhrase._lex_ph_count) 
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
        return f'Lexical Phrase {self.id}: {self.lyrics}'
    
    def values_(self):
        return str(self.id)

    @classmethod
    def reset_counter(cls, init_value=0):
        try:
            if init_value >= 0:
                cls._lex_ph_count = int(init_value)
        except:
            pass

    

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
        self.lyric = list(args)
        self.notes = []
        self.check_dotted_duration()

    def add_note(self, pitch:str, duration:str):
        """add a note: pitch and duration

        Parameters:
        - pitch (str): C2, A3, E4, B7, ...
        - duration (str): 1/1, 1/2, 1/4, 1/8, 1/16, ...
        """
        self.notes.append({'pitch': pitch, 'duration': duration})
        self.check_dotted_duration()

    # def add_notes_chaotic(self, )

    def add_lyric(self, lyric):
        self.lyric.append(lyric)

    def is_melisma(self):
        """check if the syllable has multiple notes = (is a melisma)"""
        return len(self.notes) > 1       
    
    def check_dotted_duration(self):
        for note in self.notes:
            if note['duration'] and note['duration'].endswith('.'):
                numer, denom  = (int(note['duration'].split('/')[0]), 
                                 note['duration'].split('/')[1].strip('. '))
                note['duration'] = '/'.join((str(numer * 3), str(denom)))

    def __repr__(self):
        return f'Syllable: {self.values_()}'
    
    def add_child(self):
        pass

    def delete_child(self, child):
        return

    def values_(self):
        notes_repr = ', '.join(note['pitch'] + ' - ' + note['duration'] 
                               for note in self.notes 
                               if note['pitch'] and note['duration'])
        
        lyric_repr = ''.join(lyr for lyr in self.lyric if lyr)
        return f'{lyric_repr}  {notes_repr}'


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
        self.duration = list(args)
        self.check_dotted_duration()
        
    def __repr__(self):
        return f'Rest:  {self.values_()}'

    def add_duration(self, duration):
        self.duration.append(duration)
        self.check_dotted_duration()

    def check_dotted_duration(self):
        for indx in range(len(self.duration)):
            if self.duration[indx].endswith('.'):
                duration = self.duration[indx]
                numer, denom  = int(duration.split('/')[0]), duration.split('/')[1].strip('. ')
                self.duration[indx] = '/'.join((str(numer * 3), str(denom)))
                
    def add_child(self):
        pass

    def delete_child(self, child):
        return

    def values_(self):
        if self.duration:
            return " - ".join(dur if dur else '' for dur in self.duration)



