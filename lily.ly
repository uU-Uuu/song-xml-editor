
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
    \new Staff \relative c' {
      \key e \major
      \time 4/4
      e16 a16 e8 r8 |
    }
}


