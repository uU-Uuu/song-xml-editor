
\version "2.24.4"
\paper {
    #(set-default-paper-size "a9")
}
\header {
    title = "Good morning"
}

\markup {
\column {
    \line { \bold "Section: A" }
    }
}

\score {
    \header {
        piece = "Mel. phrase: 2"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key e \major
                    \time 4/4
                    e16 r8 a16e8 a16e8 b4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                go me ma me - jk
            }
        }
    >>
}