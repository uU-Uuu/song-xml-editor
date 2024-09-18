
\version "2.24.4"
\paper {
    #(set-default-paper-size "a9")
}
\header {
    title = "example"
}

\markup {
\column {
    \line { \bold "Section: Verse1" }
    }
}

\score {
    \header {
        piece = "Mel. phrase: 1"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \major
                    \time 2/4
                    dis16.e4 r2

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                a -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 3"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \major
                    \time 2/4
                    c,2

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                la
            }
        }
    >>
}