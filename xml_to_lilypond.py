import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
import re


OCTAVES = {3: "",
           4: "'",
           5: "''"}

xml_filename = 'try/tryxml.xml'


def parseXML(xml_file):
    def get_root(func):
        def inner(*args, **kwargs):
            tree = ET.parse(xml_file)
            root = tree.getroot()
            res = func(root, *args, **kwargs)
            return res
        return inner
    return get_root
    

def note_formatter(raw_pitch, raw_duration):
    pitch, octave = re.match(r'(\w+)([0-9]$)', raw_pitch).groups()
    pitch_o = pitch.lower() + OCTAVES[int(octave) - 1]
    return pitch_o + duration_formatter(raw_duration, rest=False)


def duration_formatter(raw_duration, rest=True):
    numer, denom  = list(map(int, raw_duration.split('/')))
    dotted = numer == 3 and (denom & (denom - 1)) == 0
    duration = f'{denom}{["", "."][dotted]}'
    return f'{["", "r"][rest]}{duration}'


@parseXML(xml_filename)
def parse_xml_meta(root):
    meta = './/title', './/time_signature'
    title, time_s = (root.find(tag).text for tag in meta)
    key, mode = root.find('.//key').text.lower().split()
    return title, time_s, key, mode


def parse_xml_lex_phr(mel_phr):
    for lex_phr in mel_phr.findall('.//lexical_phrase'):
        lex_notes = []

        for syllable in lex_phr.findall('.//syllable'):
            lyric = syllable.find('.//lyric').text
            notes_raw = list(zip(
                (pitch.text for pitch in syllable.findall('.//pitch')),
                (dur.text for dur in syllable.findall('.//duration'))
            ))
            lex_notes.append(' '.join(note_formatter(p, d) 
                                    for (p, d) in notes_raw))
                    
        for rest in lex_phr.findall('.//rest'):
            for duration in rest.findall('.//duration'):
                lex_notes.append(duration_formatter(duration.text))

        return ' '.join(lex_notes)
    

def parse_xml_mel_phr(section, relative="c"+OCTAVES[4]):
    time_s, key, mode, = parse_xml_meta()[1:]
    for mel_phr in section.findall('.//melodic_phrase'):
        piece = f'Mel. phrase: {mel_phr.attrib["id"]}'
        mel_notes = []
        mel_notes.append(parse_xml_lex_phr(mel_phr))
        mel_phr_piece = ' |\n'.join(mel_notes)
        mel_phr_str = f"""
\\score {{
    \\header {{
      piece = "{piece}"
    }}
    \\new Staff \\relative {relative} {{
      \\key {key} \\{mode}
      \\time {time_s}
      {mel_phr_piece} |
    }}
}}
"""
        return mel_phr_str



@parseXML(xml_filename)
def parse_xml_section(root):
    for section in root.findall('.//section'):
        subtitle = f'Section: {section.attrib["name"]}'
    section_str = f"""
\\markup {{
  \\column {{
    \\line {{ \\bold "{subtitle}" }}
    }}
}}
{parse_xml_mel_phr(section)}
"""
    return section_str

    
def xml_to_lily(filename):
    global xml_filename
    xml_filename = filename
    title = parse_xml_meta()[0]
    lily_script = f"""
\\version "2.24.4"
\\header {{
    title = "{title}"
}}
{parse_xml_section()}
"""
    return lily_script



xml_filename = 'try/tryxml.xml'


if __name__ == '__main__':
    xml_filename = 'try/tryxml.xml'