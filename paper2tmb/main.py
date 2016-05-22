# -*- coding: utf-8 -*-

"""Convert academic papers (pdf) to nice thumbnail (png)

Usage:
  paper2tmb stack [--trim=<trim>] [--size=<size>] <input-file> <output-file> <num-col> <num-row>
  paper2tmb top [--density=<density>] [--trim=<trim>] [--size=<size>] [--reduce=<reduce>] <input-file> <output-file>
  paper2tmb (-h | --help)
  paper2tmb --version

Options:
  <num-col>             Number of col
  <num-row>             Number of row
  --density=<density>   Resolution of image. The higher, the better (default=72)
  --size=<size>         Size of final output (e.g., 100x)
  --trim=<trim>         Trimming width and height for each page (e.g., 100x80)
  --reduce=<reduce>     Determines what % of lower region will be removed (e.g., 50%, default=50%)
  -h --help             Show this screen.
  --version             Show version.

Examples:
  paper2tmb stack --trim=100x60 --size=x400 arxiv-paper.pdf out.png
  paper2tmb top --size=x400 arxiv-paper.pdf out.png
"""

import os
import subprocess
from .manipulator import Manipulator
from docopt import docopt


def main():
    null = open(os.devnull, 'w')
    assert subprocess.call(["which", "convert"], stdout=null, stderr=subprocess.STDOUT) == 0, "ImageMagic:convert is required."

    args = docopt(__doc__, version='paper2tmb 0.0.1')

    assert '*' not in args['<input-file>'], "You cannot use *. parse2tmb should have one input file."
    assert os.path.splitext(args['<input-file>'])[-1] == '.pdf', "Input ext should be .pdf"
    assert os.path.splitext(args['<output-file>'])[-1] == '.png', "Output ext should be .png"

    if args['stack']:
        with Manipulator(args['<input-file>']) as m:
            m.pdf2png(trim=args["--trim"])
            m.stack(col=int(args["<num-col>"]), row=int(args['<num-row>']))
            if args['--size'] is not None:
                m.resize(args["--size"])
            m.out(args['<output-file>'])

    if args['top']:
        with Manipulator(args['<input-file>']) as m:
            m.pdf2png(trim=args["--trim"], density=args["--density"])
            m.top() if args['--reduce'] is None else m.top(args["--reduce"])
            m.out(args['<output-file>'])


if __name__ == '__main__':
    main()
