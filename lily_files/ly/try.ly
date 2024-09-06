
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
                    e16 r8 a16 e8 a16 e8

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                go me ma me -
            }
        }
    >>
}
\markup {
\column {
    \line { \bold "Section: ko" }
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
                    \key e \major
                    \time 4/4
                    c,1 r2 r2. eis'4 fes''16

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                j ak ko
            }
        }
    >>
}