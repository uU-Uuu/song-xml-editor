
\version "2.24.4"
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
        piece = "Mel. phrase: 1"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key e \major
                    \time 4/4
                    e16 r8 a16 e8 a16 e8 |

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
                    e16 r8 a16 a16 e8 |

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                go mema me -
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
        piece = "Mel. phrase: 1"
    }
    <<
        \new Staff= "staff" {
            \new Voice = "mel" {
                \relative c' {
                    \key e \major
                    \time 4/4
                    e16 r8 a16 e8 a16 e8 |

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
                    e16 r8 a16 a16 e8 |

                    }
                }
        }  
        \new Lyrics \with { alignAboveContext = "staff"} {
            \lyricsto mel {
                go mema me -
            }
        }
    >>
}