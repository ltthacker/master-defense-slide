% \LoadClass[10pt,aspectratio=169]{beamer}
\LoadClass[10pt]{beamer}
\usetheme{cambridge}

% For Japanese
\usepackage{CJKutf8}

% For citation
\usepackage[style=ieee]{biblatex}
\addbibresource{./main.bib}

% Table of content at begin of each section
\AtBeginSection[]
{
    \begin{frame}<beamer>
    \frametitle{Agenda}
    \tableofcontents[currentsection]
    \end{frame}
}
\AtBeginSubsection[]{
  \frame<beamer>{
    \frametitle{Agenda}
    \tableofcontents[currentsection,currentsubsection]
  }
}

% For figure with number
\usepackage{graphicx}
\setbeamertemplate{caption}[numbered]
\usepackage{subcaption}

% For table
\usepackage{booktabs}

% For page number
\setbeamertemplate{footline}[frame number]

% For removing navigation
\beamertemplatenavigationsymbolsempty

% For checkmark
\usepackage{tikz}
\def\checkmark{\tikz\fill[scale=0.4](0,.35) -- (.25,0) -- (1,.7) -- (.25,.15) -- cycle;} 