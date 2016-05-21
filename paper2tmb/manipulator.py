import os
from datetime import datetime
import hashlib
import subprocess


class Manipulator(object):

    def __init__(self, input_file, dirname=None):
        self.input_file = input_file
        self._last = self.input_file
        self.dirname = dirname
        self._num_page = None

        if self.dirname is None:
            raw = self.input_file + str(datetime.now())
            self.dirname = hashlib.sha224(raw.encode('utf-8')).hexdigest()

    def __enter__(self):
        self.mkdir()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def mkdir(self):
        if not os.path.isdir(self.dirname):
            os.mkdir(self.dirname)

    def close(self):
        subprocess.call(['rm', '-rf', self.dirname])

    def pdf2png(self, trim=None, density=None):
        assert trim is None or "x" in trim, "trim parameter is wrong"

        f = os.path.join(self.dirname, "pdf2png.png")
        command = ["convert", "-background", "white", "-alpha", "remove"]

        if trim is not None:
            trim_command = ['-gravity', 'northwest', '-chop', trim, '-gravity', 'southeast', '-chop', trim]
            command += trim_command

        if density is not None:
            density_command = ['-density', "{}x{}".format(density, density)]
            command += density_command

        command += [self._last, f]
        subprocess.call(command)

        self._last = f

        self._num_page = 0
        for f in os.listdir(self.dirname):
            if "pdf2png" in f:
                self._num_page += 1

    def stack(self, col=None, row=None):
        assert "pdf2png" in self._last
        assert col * row <= self._num_page, "Number of pages is {}".format(self._num_page)

        png_list = [os.path.join(self.dirname, "pdf2png-{}.png".format(i)) for i in range(self._num_page)]
        rows = []
        for i in range(row):
            f = os.path.join(self.dirname, "stack_row_{}.png".format(i))
            rows.append(f)
            subprocess.call(["convert", "+append"] + png_list[i * col: (i + 1) * col] + [f])

        f = os.path.join(self.dirname, "stack.png")
        subprocess.call(["convert", "-append"] + rows + [f])

        self._last = f

    def resize(self, size=None):
        assert "pdf2png" not in self._last
        assert size is not None, "size is not set"

        f = os.path.join(self.dirname, "resize_{}.png".format(size))
        subprocess.call(["convert", "-scale", size, self._last, f])

        self._last = f

    def top(self, _reduce="50%"):
        assert "pdf2png" in self._last

        assert '%' in _reduce
        assert "." not in _reduce

        p = 100 - int(_reduce.rstrip("%"))

        f = os.path.join(self.dirname, "top_{}.png".format(_reduce))
        base, ext = os.path.splitext(self._last)
        _input = base + "-0" + ext

        subprocess.call(["convert", "-crop", "100%x{:d}%".format(p), _input, f])

        base, ext = os.path.splitext(f)
        self._last = base + "-0" + ext

    def out(self, output_file):
        subprocess.call(["cp", self._last, output_file])
