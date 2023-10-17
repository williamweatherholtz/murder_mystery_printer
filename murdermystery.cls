\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{murdermystery}

\LoadClass{report}

\newcommand{\charheading}[2]{\textbf{Act #2}: \textit{#1}}

\newcommand{\cuthere}{\hbox to \textwidth{\leaders\hbox to 25pt{\hss . \hss}\hfil}}
\newcommand{\privateitem}[1]{\\ \includegraphics[height=0.4in]{symbols/private} & $\bullet$ #1 \\}
\newcommand{\publicitem}[1]{\\ & $\bullet$  #1 \\ }

% character name, act, logo file, infos
\newcommand{\charentry}[4]{
\begin{tabular}[t]{m{2in} m{5in}}
\includegraphics[height=1in]{#3}\newline\charheading{#1}{#2}& 
\begin{tabular}{m{1in} m{3.5in}}
        #4
\end{tabular}
\end{tabular}

\vspace{2mm}
\cuthere
\vspace{2mm}
}

\RequirePackage[margin=.5in]{geometry}
\RequirePackage{graphicx}
\RequirePackage{array}

\pagenumbering{gobble}