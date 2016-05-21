import os
import unittest
import subprocess

from paper2tmb.manipulator import Manipulator


class TestManipulator(unittest.TestCase):

    def test_init(self):
        with Manipulator('test.pdf') as m:
            self.assertTrue(os.path.isdir(m.dirname))

    def test_pdf2png(self):
        with Manipulator("paper2tmb/tests/testdata/1412.6785v2.pdf") as m:
            m.pdf2png()

            for i in range(12):
                self.assertTrue(os.path.exists(os.path.join(m.dirname, "pdf2png-{}.png".format(i))))

            self.assertTrue(m._last == os.path.join(m.dirname, "pdf2png.png"))

    def test_pdf2png_trim(self):
        with Manipulator("paper2tmb/tests/testdata/1412.6785v2.pdf") as m:
            m.pdf2png(trim="100x100")

            for i in range(12):
                self.assertTrue(os.path.exists(os.path.join(m.dirname, "pdf2png-{}.png".format(i))))

            self.assertTrue(m._last == os.path.join(m.dirname, "pdf2png.png"))

    def test_pdf2png_density(self):
        with Manipulator("paper2tmb/tests/testdata/1412.6785v2.pdf") as m:
            m.pdf2png(density="20")

            for i in range(12):
                self.assertTrue(os.path.exists(os.path.join(m.dirname, "pdf2png-{}.png".format(i))))

            self.assertTrue(m._last == os.path.join(m.dirname, "pdf2png.png"))

    def test_pdf2png_both_trim_density(self):
        with Manipulator("paper2tmb/tests/testdata/1412.6785v2.pdf") as m:
            m.pdf2png(trim="300x300", density="10")

            for i in range(12):
                self.assertTrue(os.path.exists(os.path.join(m.dirname, "pdf2png-{}.png".format(i))))

            self.assertTrue(m._last == os.path.join(m.dirname, "pdf2png.png"))

    def test_stack(self):
        with Manipulator("paper2tmb/tests/testdata/1412.6785v2.pdf") as m:
            m.pdf2png()

            m.stack(4, 2)

            self.assertTrue(os.path.exists(os.path.join(m.dirname, "stack_row_0.png")))
            self.assertTrue(os.path.exists(os.path.join(m.dirname, "stack_row_1.png")))
            self.assertTrue(os.path.exists(os.path.join(m.dirname, "stack.png")))

            self.assertTrue(m._last == os.path.join(m.dirname, "stack.png"))

    def test_stack(self):
        with Manipulator("paper2tmb/tests/testdata/1412.6785v2.pdf") as m:
            m.pdf2png(trim="100x60")
            m.stack(6, 2)
            m.resize("x400")

            self.assertTrue(os.path.exists(os.path.join(m.dirname, "resize_x400.png")))
            self.assertTrue(m._last == os.path.join(m.dirname, "resize_x400.png"))

    def test_top(self):
        with Manipulator("paper2tmb/tests/testdata/1412.6785v2.pdf") as m:
            m.pdf2png(trim="400x240", density="300x300")
            m.top("60%")

            self.assertTrue(os.path.exists(os.path.join(m.dirname, "top_60%-0.png")))
            self.assertTrue(m._last == os.path.join(m.dirname, "top_60%-0.png"))

    def test_out(self):
        with Manipulator("paper2tmb/tests/testdata/1412.6785v2.pdf") as m:
            target = "paper2tmb/tests/testdata/out.pdf"
            m.out(target)

        self.assertTrue(os.path.exists(target))
        subprocess.call(["rm", target])
