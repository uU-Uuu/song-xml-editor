import xml.etree.ElementTree as ET
import re


class XMLToLily:
    _OCTAVES = {3: "",
           4: "'",
           5: "''"}
    
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.root = self._get_root()

    @staticmethod
    def _note_formatter(raw_pitch, raw_duration):
        if raw_pitch and raw_duration:
            pitch, octave = re.match(r'(\w+)([0-9]$)', raw_pitch).groups()
            pitch_o = pitch.lower() + XMLToLily._OCTAVES[int(octave) - 1]
            return pitch_o + XMLToLily._duration_formatter(raw_duration, rest=False)

    @staticmethod
    def _duration_formatter(raw_duration, rest=True):
        if raw_duration:
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
        lex_notes, lyrics = [], []
        for lex_phr in mel_phr.findall('.//lexical_phrase'):
            for child in lex_phr:
                if child.tag == 'syllable':
    
                    lyrics_text = [lyric.text for lyric in child.findall('.//lyric')]
                    pitches = [pitch.text for pitch in child.findall('.//pitch')]
                    # 1 syll - 2+ notes or 2 syll - 1 note
                    len_diff = len(lyrics_text) - len(pitches)
                    if len_diff < 0:
                        lyrics_text += '-' * (abs(len_diff))
                    elif len_diff > 0:
                        lyrics_text = lyrics_text[:len_diff - 1] + [''.join(lyrics_text[len_diff - 1:])]
                    lyrics.extend(lyrics_text)

                    notes_raw = list(zip(
                    (pitch.text for pitch in child.findall('.//pitch')),
                    (dur.text for dur in child.findall('.//duration'))
                    ))
                    lex_notes.append(' '.join(self._note_formatter(p, d) 
                                        for (p, d) in notes_raw))  
                    
                elif child.tag == 'rest':
                    for duration in child.findall('.//duration'):
                        lex_notes.append(self._duration_formatter(duration.text))

        return (' '.join(lex_notes) + ' |\n', 
                   ' '.join(lyrics))
        
        
    def _parse_xml_mel_phr(self, section, relative="c"+_OCTAVES[4]):
        time_s, key, mode, = self._parse_xml_meta()[1:]
        mel_phr_inner_str = ''
        for mel_phr in section.findall('.//melodic_phrase'):

            piece_var = f'Mel. phrase: {mel_phr.attrib["id"]}'

            mel_notes, mel_lyrics = self._parse_xml_lex_phr(mel_phr)
            mel_phr_inner_str += self._write_mel_phr_inner(piece_var, 
                                        relative, key, mode, time_s, 
                                        mel_notes, mel_lyrics)
        
        return mel_phr_inner_str


    @staticmethod
    def _write_mel_phr_inner(piece_var, relative, key, mode, time_s, mel_notes, mel_lyrics):
        mel_phr_inner_str = f"""
\\score {{
    \\header {{
        piece = "{piece_var}"
    }}
    <<
        \\new Staff= "staff" {{
            \\new Voice = "mel" {{
                \\relative {relative} {{
                    \\key {key} \\{mode}
                    \\time {time_s}
                    {mel_notes}
                    }}
                }}
        }}  
        \\new Lyrics \\with {{ alignAboveContext = "staff"}} {{
            \\lyricsto mel {{
                {mel_lyrics}
            }}
        }}
    >>
}}"""
        return mel_phr_inner_str

    

    def _parse_xml_section(self):
        section_str = ''
        for section in self.root.findall('.//section'):
            subtitle = f'Section: {section.attrib["name"]}'
            inner = self._parse_xml_mel_phr(section)

            section_str += f"""
\\markup {{
\\column {{
    \\line {{ \\bold "{subtitle}" }}
    }}
}}
{inner}"""
        return section_str

        
    
    def xml_to_lily(self):
        title = self._parse_xml_meta()[0]
        lily_script = f"""
\\version "2.24.4"
\\header {{
    title = "{title}"
}}
{self._parse_xml_section()}"""
        return lily_script




if __name__ == '__main__':
    xml_filename = 'try/tryxml.xml'
    converter = XMLToLily(xml_filename)
    # converter.xml_to_lily()
    print(converter.xml_to_lily())