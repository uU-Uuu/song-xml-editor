import os

import subprocess




lilypond_content = """
\\version "2.24.4"
\\header {
  title = "Good Morning"
}
\\markup {
  \\column {
    \\line { \\bold "Section Name 2" }
  }
}

\\score {
  \\header {
    piece = "Mel phrase id"
  }
  
  \\new Staff \\relative c' {
    \\key a \\major
    \\time 2/4
    c4 d e f |
    g a b c |
    }
}

\\markup {
  \\column {
    \\line { \\bold "Section Name 2" }
  }
}


\\score {
  \\header {
    piece = "Mel phrase id 2"
  }
  \\new Staff \\relative c' {
    \\key a \\major
    \\time 2/4
    c4 d e f |
    g a b c |
  }
}
"""

lily_file = 'lily.ly'
out_dir = 'try'

os.makedirs(out_dir, exist_ok=True)

with open('lily.ly', 'w') as file:
    file.write(lilypond_content)

subprocess.run([
    'lilypond',
    '--png',
    '--output=' + out_dir,
    lily_file
])

out_img = os.path.join(out_dir, 'lily.png')



