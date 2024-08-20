from xml.etree import ElementTree as ET
from xmlschema import XMLSchema, XMLSchemaValidationError
from enum import Enum


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



SCHEMAS = {
    TagNames.doc: XMLSchema('../../xml_utils/xml_schemas/doc_schema.xsd'),
    TagNames.melody: XMLSchema('../../xml_utils/xml_schemas/melody_schema.xsd'),
    TagNames.section: XMLSchema('../../xml_utils/xml_schemas/section_schema.xsd'),
    TagNames.melodic_phrase: XMLSchema('../../xml_utils/xml_schemas/melphr_schema.xsd'),
    TagNames.lexical_phrase: XMLSchema('../../xml_utils/xml_schemas/lexphr_schema.xsd'),
    TagNames.syllable: XMLSchema('../../xml_utils/xml_schemas/syllable_schema.xsd'),
    TagNames.rest: XMLSchema('../../xml_utils/xml_schemas/rest_schema.xsd')
}


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


