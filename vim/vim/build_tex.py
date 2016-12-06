#!/usr/bin/env python3
import sys
import re
import subprocess
import os


def main():
    if len(sys.argv) != 2:
        raise KeyError
    file_name = sys.argv[1]
    expression = r'^(.*)\.(\w+)$'
    base_name = re.match(expression, file_name).group(1)
    latexmk_args = ['latexmk', '--shell-escape', '-pdf', '-synctex=1', '-output-directory=/tmp/', file_name]
    subprocess.call(latexmk_args)
    mv_args = ['mv', '/tmp/' + base_name + '.pdf', './']
    subprocess.call(mv_args)
    os.system('evince ' + base_name + '.pdf' + ' > /dev/null 2>&1 &')


if __name__ == '__main__':
    main()
