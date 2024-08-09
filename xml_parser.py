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


SCHEMAS = {
    TagNames.doc: XMLSchema('xml_schemas/doc_schema.xsd'),
    TagNames.melody: XMLSchema('xml_schemas/melody_schema.xsd'),
    TagNames.section: XMLSchema('xml_schemas/section_schema.xsd'),
    TagNames.melodic_phrase: XMLSchema('xml_schemas/melphr_schema.xsd'),
    TagNames.lexical_phrase: XMLSchema('xml_schemas/lexphr_schema.xsd'),
    TagNames.syllable: XMLSchema('xml_schemas/syllable_schema.xsd'),
    TagNames.rest: XMLSchema('xml_schemas/rest_schema.xsd')
}


class XMLValidationError(Exception):
    pass


class InvalidXMLInputProvided(Exception):
    pass


def validate_xml(tag_name: TagNames, xml_file='', xml_str=''):
    try:
        if xml_file:
            tree = ET.parse(xml_file)            
        elif xml_str:
            tree = ET.fromstring(xml_str)
        else:
            raise InvalidXMLInputProvided('No XML input provided')

        if tree:
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
