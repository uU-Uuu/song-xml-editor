
\version "2.24.4"
\header {
  title = "Good Morning"
}
\markup {
  \column {
    \line { \bold "Section Name 2" }
  }
}

\score {
  \header {
    piece = "Mel phrase id"
  }
  
  \new Staff \relative c' {
    \key a \major
    \time 2/4
    c4 d e f |
    g a b c |
    }
}

\markup {
  \column {
    \line { \bold "Section Name 2" }
  }
}


\score {
  \header {
    piece = "Mel phrase id 2"
  }
  \new Staff \relative c' {
    \key a \major
    \time 2/4
    c4 d e f |
    g a b c |
  }
}
