import os
import subprocess

from xml_utils.xml_to_lilypond import XMLToLily


lily_file = 'lily.ly'
out_dir = 'try'
xml_file = 'try/tryxml.xml'
img_file = 'lily.png'

os.makedirs(out_dir, exist_ok=True)


with open(lily_file, 'w') as file:
    lily_converter = XMLToLily(xml_file)
    lilypond_content = lily_converter.xml_to_lily()
    file.write(lilypond_content)


subprocess.run([
    'lilypond',
    '--png',
    '--output=' + out_dir,
    lily_file
])

out_img = os.path.join(out_dir, img_file)



