# Analyze-SciCode
Analyze scientific code by finding affected variables.

Built to analyze Fortran code (round parenthesis, ...) in the WRF weather forecasting model.

Example call:
	./analyze.py ../WRFV3.9.1/phys/module_mp_thompson.F Nt_c --lvl=2 


Search for variables affected by another variable.
Usage:
  analyze.py <file> <variable> [--lvl=<level>]
  analyze.py (-h | --help)
  analyze.py --version
Options:
  -h --help          Show this screen.
  --version          Show version.
  --lvl=<level>      Recursion level
