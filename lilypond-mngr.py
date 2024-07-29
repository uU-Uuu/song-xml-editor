import os
import subprocess

from xml_to_lilypond import xml_to_lily




# lilypond_content = """
# \\version "2.24.4"
# \\header {
#   title = "Good Morning"
# }
# \\markup {
#   \\column {
#     \\line { \\bold "Section Name 2" }
#   }
# }

# \\score {
#   \\header {
#     piece = "Mel phrase id"
#   }
  
#   \\new Staff \\relative c' {
#     \\key a \\major
#     \\time 2/4
#     c4 d e f |
#     g a b c |
#     }
# }

# \\markup {
#   \\column {
#     \\line { \\bold "Section Name 2" }
#   }
# }


# \\score {
#   \\header {
#     piece = "Mel phrase id 2"
#   }
#   \\new Staff \\relative c' {
#     \\key a \\major
#     \\time 2/4
#     c4 d e f |
#     g a b c |
#   }
# }
# """

lily_file = 'lily5.ly'
out_dir = 'try'

os.makedirs(out_dir, exist_ok=True)


with open('lily5.ly', 'w') as file:
    lilypond_content = xml_to_lily('try/tryxml.xml')
    file.write(lilypond_content)

subprocess.run([
    'lilypond',
    '--png',
    '--output=' + out_dir,
    lily_file
])

out_img = os.path.join(out_dir, 'lily.png')



