# Analyze-SciCode
Analyze scientific code by finding affected variables.

Built to analyze Fortran code (round parenthesis, ...) in the WRF weather forecasting model.

Example call:
```
>>> ./analyze.py /User/Downloads/WRFV3.9.1/phys/module_mp_thompson.F Nt_c --lvl=2
------------
variable: "Nt_c"; level: 2
affects 5 variables:  ['ncten', 'xnc', 'nc', 'mu_c', 'nc1d']
------------
variable: "ncten"; level: 1
affects 4 variables:  ['xnc', 'ncten', 'nc', 'nc1d']
------------
variable: "xnc"; level: 1
affects 7 variables:  ['nu_c', 'pnc_wcd', 'lamc', 'pni_iha', 'pni_inu', 'ncten', 'niten']
------------
variable: "nc"; level: 1
affects 26 variables:  ['nu_c', 'nc', 'pni_wfz', 'pni_iha', 'pni_inu', 'A', 'pnc_scw', 'lamc', 'pnc_wcd', 'pnc_rcw', 'pnc_wau', 'ncten', 'READ(iunit_mp_th1,ERR', '(KIND', 'nwfaten', 'C', 'B', 'D', 'inu_c', 'xDc', 'sed_n', 'pnc_gcw', 'xnc', 'idx_n', 'niten', 'nc1d']
------------
variable: "mu_c"; level: 1
affects 1 variables:  ['mu_c']
------------
variable: "nc1d"; level: 1
affects 6 variables:  ['lamc', 'nu_c', 'nc', 'xnc', 'ncten', 'nc1d']
```

```
Search for variables affected by another variable.
Usage:
  analyze.py <file> <variable> [--lvl=<level>]
  analyze.py (-h | --help)
  analyze.py --version
Options:
  -h --help          Show this screen.
  --version          Show version.
  --lvl=<level>      Recursion level
``` 
