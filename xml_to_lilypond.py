import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
import re


OCTAVES = {3: "",
           4: "'",
           5: "''"}


def note_formatter(raw_pitch, raw_duration):
    pitch, octave = re.match(r'(\w+)([0-9]$)', raw_pitch).groups()
    pitch_o = pitch.lower() + OCTAVES[int(octave) - 1]
    return pitch_o + duration_formatter(raw_duration, rest=False)


def duration_formatter(raw_duration, rest=True):
    numer, denom  = list(map(int, raw_duration.split('/')))
    dotted = numer == 3 and (denom & (denom - 1)) == 0
    duration = f'{denom}{["", "."][dotted]}'
    return f'{["", "r"][rest]}{duration}'

    

def parse_xml(xml_file):
    
    tree = ET.parse(xml_file)
    root = tree.getroot()

    meta = './/title', './/time_signature'
    title, time_s = (root.find(tag).text for tag in meta)
    key, mode = root.find('.//key').text.lower().split()

    for section in root.findall('.//section'):
        subtitle = f'Section: {section.attrib["name"]}'
        for mel_phr in section.findall('.//melodic_phrase'):
            piece = f'Mel. phrase: {mel_phr.attrib["id"]}'
            mel_notes = []
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

                mel_notes.append(' '.join(lex_notes))
            mel_notes_str = ' |\n'.join(mel_notes)
            






    # for syll in root.findall('.//syllable'):
    #     print(syll.find('lyric').text)
       

def lilypond_script(title, key, mode, time_s, relative="c"+OCTAVES[4]):
    script = f"""
    \\version "2.24.4"
    \\header {{
        title = "{title}"
    }}

    \\score {{
        header {{
            
        }}
        \\new Staff \\relative {relative} {{
            \\key {key} \\{mode}
            \\time {time_s}
        }}
    }}
    """
    return script

# print(lilypond_script("good", "a", "major", "4/4"))

parse_xml('try/tryxml.xml')



