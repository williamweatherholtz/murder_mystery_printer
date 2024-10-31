\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{murdermystery}

\LoadClass{report}

\newcommand{\charheading}[2]{\textbf{Act #2}: \textit{#1}}

\newcommand{\cuthere}{\hbox to \textwidth{\leaders\hbox to 25pt{\hss . \hss}\hfil}}
\newcommand{\privateitem}[1]{\\ \IfFileExists{symbols/private}{\includegraphics[height=0.4in]{symbols/private}}{\includegraphics[height=0.4in]{murder_mystery_printer/symbols/private}} & $\bullet$ #1 \\}
\newcommand{\publicitem}[1]{\\ & $\bullet$  #1 \\ }

% character name, act, logo file, infos
\newcommand{\charentry}[4]{
\begin{tabular}[t]{m{2in} m{5in}}
\includegraphics[height=1in, width=2in,keepaspectratio]{#3}\newline\charheading{#1}{#2}& 
\begin{tabular}{m{.375in} m{4.375in}}
        #4
\end{tabular}
\end{tabular}

\vspace{2mm}
\cuthere
\vspace{2mm}
}

\RequirePackage[margin=.375in]{geometry}
\RequirePackage{graphicx}
\RequirePackage{array}

\pagenumbering{gobble}