import os
import subprocess

from xml_utils.xml_to_lilypond import XMLToLily


class LilyImgGenerator:
    def __init__(self, lily_file='lily', out_dir='lily_files', img_file='lily'):
        self.out_dir = out_dir
        self.ly_out_dir = os.path.join(out_dir, 'ly')
        print(self.ly_out_dir)
        self.img_out_dir = os.path.join(out_dir, 'img')
        os.makedirs(out_dir, exist_ok=True)
        os.makedirs(self.ly_out_dir, exist_ok=True)
        os.makedirs(self.img_out_dir, exist_ok=True)
        self.img_file = img_file + '.png'
        self.lily_file = os.path.join(self.ly_out_dir, lily_file + '.ly')

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
    '--output=' + self.img_out_dir,
    self.lily_file
])
        out_img = os.path.join(self.img_out_dir, self.img_file)
        return out_img




