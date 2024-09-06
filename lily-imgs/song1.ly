
\version "2.24.4"
\header {
    title = "None"
}

\markup {
\column {
    \line { \bold "" }
    }
}

\score {
    \header {
        piece = "Mel. phrase: 4"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key  \
                    \time None
                     |

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                
            }
        }
    >>
}