
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
                    e16 e8 e16 e16 e16 e16 e16e4 e16 e16 e16 e16 f16 f16 a8a2 r4

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
                    e16 e8 e16 e16 e16 e16 e16e4 e16 e16 e16 e16 f8 e16 b16b2 r4

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
                    e16 e8 e16 e16 e16 e16 e16e4 e16 e16 e16 e16 f16 f16 a8a2 r4

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
                    b16 b8 b16 b16 b16 b16 b16b4 e16 e16 f16 a16 a1

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
                    f16 f16 f16 f16  a16 a16 a16a4 r16 f16 f16 f16 e8 e8 c8 e2 r4

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
\score {
    \header {
        piece = "Mel. phrase: 6"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    a16 a16 a16 a16a16 a16 a16 a16  a16 a16 a16 b8 a16 b16b4.

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                や ぶ れ た - あ み は と い さ し あ み か -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 7"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    c16. b16 a2 r8 a16 b16b8 d8 f16f1

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                い ま じゃ は ま - べ で -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 8"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 d16 e16 d16 e4 e16 d16 e16 d16 e8 c8 b2

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                オ ン ボ ロ ロ オ ン ボ ロ ボ ロ ロ
            }
        }
    >>
}
\markup {
\column {
    \line { \bold "Section: C" }
    }
}

\score {
    \header {
        piece = "Mel. phrase: 9"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 e8 e16 e16 e16 e16 e16e4 r16 e16 e16 e16 f16 a16.a2 r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                お き を と お る は - お さ と ま る -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 10"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 e8 e16 e16 e16 e16 e16e4 e16 e16 e16 e16 f16 e16 e8e2

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                わ た しゃ な み だ で - 二 シ ン ぐ も り の -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 11"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 d16 c16 b16 a4. r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                そ ら を み る
            }
        }
    >>
}
\markup {
\column {
    \line { \bold "Section: A" }
    }
}

\score {
    \header {
        piece = "Mel. phrase: 12"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 e8 e16 e16 e16 e16 e16e4 e16 e16 e16 e16 f16 f16 a8a2 r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                も え ろ か が り び - あ さ り の は ま に -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 13"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 e8 e16 e16 e16 e16 e16e4 e16 e16 e16 e16 f8 e16 b16b2 r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                う み は ぎ ん い ろ - 二 シ ン の い ろ よ -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 14"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16e16 e16 e16 e16 e16 e16e16e4 e16 e16 e16 e16 f16 f16 a8a2 r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                ソ - ラ ン ぶ し に - - ほ ほ そ め な が ら -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 15"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    b16 b8 b16 b16 b16 b16 b16b4 e16 e16 f16 a16 a1

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                わ た しゃ た い りょう の - あ み を ひ く
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
        piece = "Mel. phrase: 16"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    f16 f16 f16 f16  a16 a16 a16a4 r16 f16 f16 f16 e8 e8 c8 e2 r4

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
\score {
    \header {
        piece = "Mel. phrase: 17"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    a16 a16 a16 a16 a16 a16 a16 a16  a16 a16 a16 b8 a16 b16b4.

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                オ タ モ イ み さ き の 二 シ ン ご て ん も -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 18"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    c16. b16 a2 r8 a16 b16b8 d8 f16f1

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                い ま じゃ さ び - れ て -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 19"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 d16 e16 d16 e4 e16 d16 e16 d16 e8 c8 b2

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                オ ン ボ ロ ロ オ ン ボ ロ ボ ロ ロ
            }
        }
    >>
}
\markup {
\column {
    \line { \bold "Section: C" }
    }
}

\score {
    \header {
        piece = "Mel. phrase: 20"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 e8 e16 e16e16 e16 e16 e16e4 r16 e16 e16 e16 f16 a16.a2 r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                か わ ら ぬ - も の は - こ だ い も じ -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 21"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 e8 e16 e16 e16 e16 e16e4 e16 e16 e16 e16 f16 e16 e8e2

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                わ た しゃ な み だ で - む す め ざ か り の -
            }
        }
    >>
}
\score {
    \header {
        piece = "Mel. phrase: 22"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key a \minor
                    \time 4/4
                    e16 d16 c16 b16 a4. r4

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                ゆ め を み る
            }
        }
    >>
}