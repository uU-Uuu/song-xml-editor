
\version "2.24.4"
\paper {
    #(set-default-paper-size "a9")
}
\header {
    title = "mew"
}

\markup {
\column {
    \line { \bold "" }
    }
}

\score {
    \header {
        piece = "Mel. phrase: 3"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                hj
            }
        }
    >>
}