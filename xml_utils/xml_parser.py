from xml.etree import ElementTree as ET
from xmlschema import XMLSchema, XMLSchemaValidationError
from enum import Enum

# from xml_utils.constants import TAGS_FACTORY, SCHEMAS

class TagNames(Enum):
    doc = 'doc'
    melody = 'melody'
    section = 'section'
    melodic_phrase = 'melodic_phrase'
    lexical_phrase = 'lexical_phrase'
    syllable = 'syllable'
    rest = 'rest'

    @classmethod
    def tags(cls):
        return {
            'doc': cls.doc,
            'melody': cls.melody,
            'section': cls.section,
            'melodic_phrase': cls.melodic_phrase,
            'lexical_phrase': cls.lexical_phrase,
            'syllable': cls.syllable,
            'rest': cls.rest
        }

    @classmethod
    def by_tag(cls, tag_name: str):
        tags_ = cls.tags()
        el = tags_.get(tag_name)
        return el if el else None


class XMLValidationError(Exception):
    pass


class InvalidXMLInputProvided(Exception):
    pass


def validate_xml(tag_name, xml_file='', xml_str=''):
    try:
        if xml_file:
            tree = ET.parse(xml_file)            
        elif xml_str:
            tree = ET.fromstring(xml_str)
        else:
            raise InvalidXMLInputProvided('No XML input provided')

        if tree:
            if isinstance(tag_name, str):
                TagNames.by_tag(tag_name)
            elif isinstance(tag_name, TagNames):
                schema = SCHEMAS.get(tag_name)
                if not schema:
                    raise InvalidXMLInputProvided(f'Invalid tag_name: {tag_name}')

                schema.validate(tree)

    except ET.ParseError:
        raise InvalidXMLInputProvided(f'Invalid XML input provided')
    except XMLSchemaValidationError as e:
        raise XMLValidationError(f'Invalid XML: {tag_name}\n{e}')
    except Exception as e:
        raise InvalidXMLInputProvided(f'Unexpected error: {e}')



from xml_utils.tags import Melody, Section, MelPhrase, LexPhrase, Syllable, Rest

TAGS_FACTORY = {
    TagNames.melody: Melody,
    TagNames.section: Section, 
    TagNames.melodic_phrase: MelPhrase,
    TagNames.lexical_phrase: LexPhrase,
    TagNames.syllable: Syllable, 
    TagNames.rest: Rest
}

SCHEMAS = {
    TagNames.doc: XMLSchema('xml_utils/xml_schemas/doc_schema.xsd'),
    TagNames.melody: XMLSchema('xml_utils/xml_schemas/melody_schema.xsd'),
    TagNames.section: XMLSchema('xml_utils/xml_schemas/section_schema.xsd'),
    TagNames.melodic_phrase: XMLSchema('xml_utils/xml_schemas/melphr_schema.xsd'),
    TagNames.lexical_phrase: XMLSchema('xml_utils/xml_schemas/lexphr_schema.xsd'),
    TagNames.syllable: XMLSchema('xml_utils/xml_schemas/syllable_schema.xsd'),
    TagNames.rest: XMLSchema('xml_utils/xml_schemas/rest_schema.xsd')
}




def parse_xml_to_obj(xml_str):

    print(xml_str)

    try:
        tree = ET.fromstring(xml_str)    
        if tree:
            schema = SCHEMAS[TagNames.doc]
            schema.validate(tree)
        
            root = tree
            melody = root.find('.//melody')
            all_els, extra_children = [], []
            temp_save_obj = None

        def iterate_recursively(el):
            nonlocal all_els
            nonlocal extra_children
            nonlocal temp_save_obj

            obj_key = TAGS_FACTORY.get(TagNames.by_tag(el.tag))

            if obj_key:
                obj = obj_key()

                for key, val in el.attrib.items():
                    obj.__dict__[key] = val

                if extra_children:
                    note_dict = {'pitch': None, 'duration': None}
                    for child in extra_children:
                        for key, val in child.items():
                            if isinstance(temp_save_obj, Rest) and key == 'duration':
                                    temp_save_obj.add_duration(val)

                            elif isinstance(temp_save_obj, Syllable):
                                if key == 'lyric':
                                    temp_save_obj.add_lyric(val)
                                else:
                                    note_dict[key] = val
                                    if note_dict['pitch'] and note_dict['duration']:
                                        temp_save_obj.add_note(pitch=note_dict['pitch'],
                                                               duration=note_dict['duration'])
                                        note_dict['pitch'] = note_dict['duration'] = None

                    extra_children.clear()
                    all_els.append(temp_save_obj)
                    temp_save_obj = None
                
                if isinstance(obj, Syllable) or isinstance(obj, Rest):
                    temp_save_obj = obj
                else:
                    all_els.append(obj)

            else:
                extra_children.append({el.tag: el.text})

            if list(el):
                for child in el:
                    iterate_recursively(child)
            return el

        for child in melody:
            iterate_recursively(child)

        if extra_children:
            note_dict = {'pitch': None, 'duration': None}
            for child in extra_children:
                for key, val in child.items():
                    if isinstance(temp_save_obj, Rest) and key == 'duration':
                            temp_save_obj.add_duration(val)

                    elif isinstance(temp_save_obj, Syllable):
                        if key == 'lyric':
                            temp_save_obj.add_lyric(val)
                        else:
                            note_dict[key] = val
                            if note_dict['pitch'] and note_dict['duration']:
                                temp_save_obj.add_note(pitch=note_dict['pitch'],
                                                        duration=note_dict['duration'])
                                note_dict['pitch'] = note_dict['duration'] = None
            extra_children.clear()
            all_els.append(temp_save_obj)

        return all_els

    except ET.ParseError:
        raise InvalidXMLInputProvided(f'Invalid XML input provided')
    except XMLSchemaValidationError as e:
        raise XMLValidationError(f'Invalid XML\n{e}')
    except Exception as e:
        raise InvalidXMLInputProvided(f'Unexpected error: {e}')
