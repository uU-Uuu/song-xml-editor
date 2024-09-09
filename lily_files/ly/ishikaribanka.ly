
\version "2.24.4"
\paper {
    #(set-default-paper-size "a9")
}
\header {
    title = "ishikaribanka"
}

\markup {
\column {
    \line { \bold "Section: A" }
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
                    \key a \minor
                    \time 4/4
                    e16 e8 e16 e16 e16 e16 e16 e4 e16 e16 e16 e16 f16 f16 a8 a2 r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                ご め が な く か ら - 二 シ ン が く る と -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 2"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 e8 e16 e16 e16 e16 e16 e4 e16 e16 e16 e16 f8 e16 b16 b2 r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                あ か い つ っ ぽ の - ヤ ン しゅう が さ わ ぐ -
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
                    \key a \minor
                    \time 4/4
                    e16 e8 e16 e16 e16 e16 e16 e4 e16 e16 e16 e16 f16 f16 a8 a2 r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                ゆ き に う も れ た - ば ん や の す み で -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 4"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    b16 b8 b16 b16 b16 b16 b16 b4 e16 e16 f16 a16 a1

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                わ た しゃ よ ど お し - め し を た く
            }
        }
    >>
}
\markup {
\column {
    \line { \bold "Section: B" }
    }
}

\score {
    \header {
        piece = "Mel. phrase: 5"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    f16 f16 f16 f16  a16 a16 a16 a4 r16 f16 f16 f16 e8 e8 c8 e2 r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                あ れ か ら 二 シ ン は - ど こ へ いっ た や ら
            }
        }
    >>
}