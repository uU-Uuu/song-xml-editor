from xml_utils.tags import Melody, Section, MelPhrase, LexPhrase, Syllable, Rest


PITCHES = {
    'CBtn': 'C',
    'DBtn': 'D',
    'EBtn': 'E', 
    'FBtn': 'F', 
    'GBtn': 'G',
    'ABtn': 'A',
    'BBtn': 'B'
}
PITCH_MOD = {
    'sharpBtn': '#',
    'flatBtn': 'b'
}
DURATIONS = {
    'syllableDur1Btn': '1/1',
    'syllableDur2Btn': '1/2',
    'syllableDur4Btn': '1/4',
    'syllableDur8Btn': '1/8',
    'syllableDur16Btn': '1/16',
    'restDur1Btn': '1/1',
    'restDur2Btn': '1/2',
    'restDur4Btn': '1/4',
    'restDur8Btn': '1/8',
    'restDur16Btn': '1/16'
}
DOTTED = {
    'syllableDottedBtn': '.',
    'restDottedBtn': '.',
}
OCTAVES = {
    'octave3Btn': '3',
    'octave4Btn': '4',
    'octave5Btn': '5',
    'octave6Btn': '6'
}
TAGS_FACTORY = {
    'newSectionOKBtn': Section, 
    'newMelPhraseOKBtn': MelPhrase,
    'newLexPhraseOKBtn': LexPhrase,
    'newSyllableOKBtn': Syllable, 
    'newRestOKBtn': Rest
}

PARENTS_FACTORY = {
    2: Melody(),
    3: Section(),
    4: MelPhrase().reset_counter(),
    5: LexPhrase().reset_counter()
}

FILENAME_REQUIREMENTS = """\t - starting from lowercase or uppercase alphabetic characters
\t - allowed: a-z A-Z 0-9 _\n\t - extension: optional"\n\t - maximum length: 255 characters"""
