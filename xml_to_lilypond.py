import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
import re


class XMLToLily:
    _OCTAVES = {3: "",
           4: "'",
           5: "''"}
    
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.root = self._get_root()
   

    @classmethod
    def _note_formatter(cls, raw_pitch, raw_duration):
        pitch, octave = re.match(r'(\w+)([0-9]$)', raw_pitch).groups()
        pitch_o = pitch.lower() + cls._OCTAVES[int(octave) - 1]
        return pitch_o + cls._duration_formatter(raw_duration, rest=False)

    @classmethod
    def _duration_formatter(cls, raw_duration, rest=True):
        numer, denom  = list(map(int, raw_duration.split('/')))
        dotted = numer == 3 and (denom & (denom - 1)) == 0
        duration = f'{denom}{["", "."][dotted]}'
        return f'{["", "r"][rest]}{duration}'
    
    
    def _get_root(self):
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
        return root


    def _parse_xml_meta(self):
        meta = './/title', './/time_signature'
        title, time_s = (self.root.find(tag).text for tag in meta)
        key, mode = self.root.find('.//key').text.lower().split()
        return title, time_s, key, mode


    def _parse_xml_lex_phr(self, mel_phr):
        for lex_phr in mel_phr.findall('.//lexical_phrase'):
            lex_notes = []

            for syllable in lex_phr.findall('.//syllable'):
                lyric = syllable.find('.//lyric').text
                notes_raw = list(zip(
                    (pitch.text for pitch in syllable.findall('.//pitch')),
                    (dur.text for dur in syllable.findall('.//duration'))
                ))
                lex_notes.append(' '.join(self._note_formatter(p, d) 
                                        for (p, d) in notes_raw))
                        
            for rest in lex_phr.findall('.//rest'):
                for duration in rest.findall('.//duration'):
                    lex_notes.append(self._duration_formatter(duration.text))
            return ' '.join(lex_notes)
        

    def _parse_xml_mel_phr(self, section, relative="c"+_OCTAVES[4]):
        time_s, key, mode, = self._parse_xml_meta()[1:]
        for mel_phr in section.findall('.//melodic_phrase'):
            piece = f'Mel. phrase: {mel_phr.attrib["id"]}'
            mel_notes = []
            mel_notes.append(self._parse_xml_lex_phr(mel_phr))
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



    def _parse_xml_section(self):
        for section in self.root.findall('.//section'):
            subtitle = f'Section: {section.attrib["name"]}'
        section_str = f"""
\\markup {{
\\column {{
    \\line {{ \\bold "{subtitle}" }}
    }}
}}
{self._parse_xml_mel_phr(section)}
    """
        return section_str


    
    def xml_to_lily(self):
        title = self._parse_xml_meta()[0]
        lily_script = f"""
    \\version "2.24.4"
    \\header {{
        title = "{title}"
    }}
    {self._parse_xml_section()}
    """
        return lily_script






if __name__ == '__main__':
    xml_filename = 'try/tryxml.xml'
    converter = XMLToLily(xml_filename)
    print(converter.xml_to_lily())