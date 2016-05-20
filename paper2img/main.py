# -*- coding: utf-8 -*-

""" Convert academic papers (pdf) to nice looking images

Usage:
  paper2img [--size=<size>] [--num-col] [--num-row] <input-file> <output-file>
  paper2img (-h | --help)
  paper2img --version

Options:
  --size=<size>         Set the size (e.g., 100x)
  --num-col=<num-col>   Set the number of col
  --num-row=<num-row>   Set the number of row
  -h --help             Show this screen.
  --version             Show version.
"""

import os
from .manipulator import Manipulator
from docopt import docopt


def main():
    args = docopt(__doc__, version='paper2img 0.0.1')
    print(args)

    assert '*' not in args['<input-file>'], "You cannot use *. parse2img should have one input file."
    assert os.path.splitext(args['<input-file>'])[-1] == '.pdf', "Input ext should be .pdf"
    assert os.path.splitext(args['<output-file>'])[-1] == '.png', "Output ext should be .png"

    m = Manipulator(args['input_file'])
    # some manipulations
    m.out(args['output_file'])


if __name__ == '__main__':
    main()
