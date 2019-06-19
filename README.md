## The PyTuroChamp, *Plankalkül*, SOMA, Bernstein, and *El Ajedrecista* Python chess engines

Python implementations of Alan Turing's [TUROCHAMP](https://chessprogramming.org/Turochamp) (1950), John Maynard Smith's [SOMA](https://chessprogramming.org/SOMA) (1961), [The Bernstein Chess Program](https://chessprogramming.org/The_Bernstein_Chess_Program) (1957), Leonardo Torres y Quevedo's [*El Ajedrecista*](https://en.wikipedia.org/wiki/El_Ajedrecista) (1912), and some related engines

### Prerequisites

* PyPy 3 is best, but regular Python 3 or 2 also works
* [python-chess](https://github.com/niklasf/python-chess) (Note that since v0.24, python-chess is for Python 3 only.)

### Quick start

Install python-chess and then either run one of the chess engines with the UCI/XBoard interface (mainly for chess GUIs), e.g.:

 $ pypy3 ptc_xboard.py soma

The parameter to ptc_xboard.py, in this case "soma", selects the engine to use; if you leave it out, PTC is selected.

| Parameter | Engine | Notes |
| ---       | ---    | ---   |
| adapt     | Simple Adaptive Engine | Needs an UCI engine with MultiPV (Stockfish by default) |
| bare      | Bare-bones engine | Has piece-square tables for positional play; is the strongest engine here |
| bern      | The Bernstein chess program | Selects plausible moves to prune search tree |
| newt      | Newt | Includes an opening book and other experimental features |
| plan      | Plankalkül | Is set to a higher search depth than e.g. the Java implementation by default to make it a bit stronger |
| ptc       | TUROCHAMP (Default) | The Turing/Champernowne engine after which this repo is named |
| rmove     | Random Mover | All other engines should win or draw against this |
| shannon   | Shannon chess engine | Pretty much an engine that maximizes mobility |
| soma      | The Smith One-Move Analyzer | Swap-off instead of tree search-based engine |
| torres    | *El Ajedrecista* by Torres y Quevedo | Plays only as White like the real machine! (Random moves as Black.) |

Or run an engine with the console interface (Unicode output; enter your moves as e.g. "e2e4"; use black on white text in the terminal for correct piece colors):

 $ pypy3 pyturochamp.py

See the [chess GUI page](http://mdoege.github.io/PyTuroChamp/gui.html) for details on how to set up the chess engines in e.g. Cute Chess or Arena.

### Documentation

Full documentation at [mdoege.github.io/PyTuroChamp/](http://mdoege.github.io/PyTuroChamp/)

### PyTuroChamp binaries created with [PyInstaller](https://github.com/pyinstaller/pyinstaller)

* Windows EXE: [pyturochamp.exe.zip](https://drive.google.com/open?id=1Tye_42KCrsTzMbKmUO6yp63CIGY5MJhn)
* macOS binary: [pyturochamp_mac.zip](https://drive.google.com/open?id=1OVESRVpugTCenzO6I6daIpQWPHlbr7wi)
* Linux ELF binary: [pyturochamp_linux.tar.gz](https://drive.google.com/open?id=1TrvkMkuuCsScVVR_PTzM_q5OmrOZZ5j0)

### Web browser version

There are also browser-based versions of most of these engines (with a Python backend) at [github.com/mdoege/TUROjs](https://github.com/mdoege/TUROjs).

### License

* Public Domain
* The opening book is licensed under the GPL.
