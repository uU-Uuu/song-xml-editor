import xml.etree.ElementTree as ET
import xml.dom.minidom
import os


# need to create 1 root for xml else error
# or do sth with melody
def parse_xml(xml_file):
    
    tree = ET.parse(xml_file)
    root = tree.getroot()

    xml_str = ET.tostring(root, encoding='unicode')
    parsed = xml.dom.minidom.parseString(xml_str)
    print(parsed.toprettyxml(indent=' '))

    for syll in root.findall('.//syllable'):
        print(syll.find('lyric').text)
       

parse_xml('f/2.xml')