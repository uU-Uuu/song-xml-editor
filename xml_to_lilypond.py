import xml.etree.ElementTree as ET
import xml.dom.minidom
import os


def parse_xml(xml_file):
    
    tree = ET.parse(xml_file)
    root = tree.getroot()

    meta = './/title', './/time_signature'
    title, time_s = (root.find(tag).text for tag in meta)
    key, mode = root.find('.//key').text.lower().split()

    for sect in root.findall('.//section'):
        pass

    # for syll in root.findall('.//syllable'):
    #     print(syll.find('lyric').text)
       

def lilypond_script(title, key, mode, time_s):
    script = f"""
    \\version "2.24.4"
    \\header {{
        title = "{title}"
    }}

    \\score {{
        header {{
            
        }}
        \\new Staff \\relative c' {{
            \\key {key} \\{mode}
            \\time {time_s}
        }}
    }}
    """
    return script

print(lilypond_script("good", "a", "major", "4/4"))

parse_xml('try/tryxml.xml')



