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



from tags import Melody, Section, MelPhrase, LexPhrase, Syllable, Rest

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
    try:
        tree = ET.fromstring(xml_str)    
        if tree:
            schema = SCHEMAS[TagNames.doc]
            schema.validate(tree)
        
            root = tree
            melody = root.find('.//melody')

        def iterate_recursively(el):
            print(el.tag, el, el.attrib, el.text)
            try:
                if isinstance(obj, Syllable) or isinstance(obj, Rest):
                    pass

                obj = TAGS_FACTORY[TagNames.by_tag(el.tag)]
                print(obj)
                if isinstance(obj, Syllable) or isinstance(obj, Rest):

#                     <class 'tags.Syllable'>
# lyric <Element 'lyric' at 0x000001FEF34177C0> {} go
# lyric
# pitch <Element 'pitch' at 0x000001FEF3417A40> {} E4
# pitch
# duration <Element 'duration' at 0x000001FEF34179A0> {} 1/16
# duration
# rest <Element 'rest' at 0x000001FEF3400220> {}

            except:
                print(el.tag)
            if list(el):

                for child in el:
                    iterate_recursively(child)
            return el

        for child in melody:
            iterate_recursively(child)

    except ET.ParseError:
        raise InvalidXMLInputProvided(f'Invalid XML input provided')
    except XMLSchemaValidationError as e:
        raise XMLValidationError(f'Invalid XML\n{e}')
    except Exception as e:
        raise InvalidXMLInputProvided(f'Unexpected error: {e}')



st = """<?xml version="1.0" encoding="UTF-8"?>
<doc>
    <title>Good morning</title>
    <key>e major</key>
    <time_signature>4/4</time_signature>
    <melody>
        <section name="A">
            <melodic_phrase id="2">
                <lexical_phrase id="2" lyrics="gomema">
                    <syllable>
                        <lyric>go</lyric>
                        <pitch>E4</pitch>
                        <duration>1/16</duration>
                    </syllable>
                    <rest>
                        <duration>1/8</duration>
                    </rest>
                    <syllable>
                        <lyric>me</lyric>
                        <lyric>ma</lyric>
                        <pitch>A4</pitch>
                        <duration>1/16</duration>
                        <pitch>E4</pitch>
                        <duration>1/8</duration>
                    </syllable>
                </lexical_phrase>                    
                <lexical_phrase id="3" lyrics="me">
                    <syllable>
                        <lyric>me</lyric>
                        <pitch>A4</pitch>
                        <duration>1/16</duration>
                        <pitch>E4</pitch>
                        <duration>1/8</duration>
                    </syllable>
                </lexical_phrase>                    
            </melodic_phrase>                
        </section>            
        <section name="ko">
            <melodic_phrase id="1">
            </melodic_phrase>                
        </section>            
  </melody>
</doc>"""

parse_xml_to_obj(st)
