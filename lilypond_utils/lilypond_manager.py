import os
import subprocess

from xml_utils.xml_to_lilypond import XMLToLily


class LilyImgGenerator:
    def __init__(self, lily_file='lily', out_dir='lily-imgs', img_file='lily'):
        self.lily_file = os.path.join(out_dir, lily_file + '.ly')
        self.out_dir = out_dir
        self.img_file = img_file + '.png'
        os.makedirs(out_dir, exist_ok=True)

    def from_file(self, xml_file):
        with open(self.lily_file, 'w') as file:
            lily_converter = XMLToLily(xml_file)
            lily_script = lily_converter.xml_to_lily()
            file.write(lily_script)
        self.convert()

    def from_string(self, lily_script):
        with open(self.lily_file, 'w') as file:
            file.write(lily_script)
        self.convert()

    def convert(self):
        subprocess.run([
    'lilypond',
    '--png',
    '--output=' + self.out_dir,
    self.lily_file
])
        out_img = os.path.join(self.out_dir, self.img_file)
        return out_img




