import os

import subprocess




lilypond_content = """
\version "2.24.4"
\relative {
    \time 3/4
    e16 e4. e16' a4,
    r8 r4.
}
"""

lily_file = 'lily.ly'
out_dir = 'f'

os.makedirs(out_dir, exist_ok=True)

with open('lily.ly', 'w') as file:
    file.write(lilypond_content)

subprocess.run([
    'lilypond',
    '--png',
    '--output' + out_dir,
    lily_file
])

out_img = os.path.join(out_dir, 'lily.png')



