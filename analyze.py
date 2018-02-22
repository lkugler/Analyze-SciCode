#!/Users/lukaskugler/miniconda2/bin/python
"""Search for variables affected by another variable.

Usage:
  analyze.py <file> <variable> [--lvl=<level>]
  analyze.py (-h | --help)
  analyze.py --version

Options:
  -h --help          Show this screen.
  --version          Show version.
  --lvl=<level>      Recursion level
"""
import os, re
from docopt import docopt

def getvar(LHSofEqn):
    """Finds the variable which is defined in the LHS of an Eqn
    Supports round parenthesis
    """
    var = []
    debug = False
    var_started = False
    LHS = LHSofEqn
    i = len(LHS)-1
    if debug: print LHS
    while i >= 0:  # move from right to left
        if debug: print 'begin:', i, LHS[i]

        if not var_started and LHS[i] ==')':
            while not LHS[i] == '(':
                i -= 1
                if debug: print LHS[i], '-> forget'
            if var == ' ':
                NotImplementedError('Opened parenthesis not closed on line')

        # indexing finished in LHS
        if not var_started and LHS[i] == ' ':
            if debug: print '-> forget'
            pass
        if var_started and not LHS[i] == ' ':
            if debug: print LHS[i], '-> this is var'
            var += LHS[i]
        if not var_started and not LHS[i] == ' ' and not LHS[i]=='(':
            if debug: print LHS[i], '-> this is var'
            var += LHS[i]
            var_started = True
        if var_started and LHS[i] == ' ':
            if debug: print '-> var has ended'
            break
        i -= 1

    if debug: print 'result:', ''.join(var)[::-1]
    return ''.join(var)[::-1]

def main(filename, var, lvl):
    affected = []

    with open(filename, 'r') as f:
        #txt = f.read()
        for i, line in enumerate(f):
            #print line
            if re.search(var, line) and '=' in line:
                a = line.split('=')
                if var in ''.join(a[1:]):

                    left = a[0].lstrip()
                    right = ''.join(a[1:]).lstrip()
                    #print left
                    affected.append(getvar(left))
                    #print '------------'

    # remove duplicates
    affected = list(set(affected))


    print '------------'
    print 'variable: "'+str(var)+'"; level:', lvl
    print 'affects', len(affected), 'variables: ', affected
    #print 'throught', right, 'line(', i, ')'

    if lvl > 1:
        for var in affected:
            main(filename, var, lvl - 1)


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1')
    #print(args)
    #print '---------------------------'

    lvl = 1
    if args['--lvl']:
        lvl = int(args['--lvl'])

    main(args['<file>'], args['<variable>'], lvl)
