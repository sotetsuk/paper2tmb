import os
import unittest
import subprocess

from paper2img.manipulator import Manipulator


class TestManipulator(unittest.TestCase):

    def test_init(self):
        m = Manipulator('test.pdf')
        self.assertTrue(os.path.isdir(m.dirname))

        m.close()

    def test_pdf2png(self):
        m = Manipulator("paper2img/tests/testdata/1412.6785v2.pdf")
        m.pdf2png()

        for i in range(12):
            self.assertTrue(os.path.exists(os.path.join(m.dirname, "pdf2png-{}.png".format(i))))

        m._num_page = 12
        self.assertTrue(m._last == os.path.join(m.dirname, "pdf2png.png"))

        m.close()

    def test_pdf2png_trim(self):
        m = Manipulator("paper2img/tests/testdata/1412.6785v2.pdf")
        m.pdf2png(trim="100x100")

        for i in range(12):
            self.assertTrue(os.path.exists(os.path.join(m.dirname, "pdf2png-{}.png".format(i))))

        m._num_page = 12
        self.assertTrue(m._last == os.path.join(m.dirname, "pdf2png.png"))

        m.close()

    def test_stack(self):
        m = Manipulator("paper2img/tests/testdata/1412.6785v2.pdf")
        m.pdf2png()

        m.stack(4, 2)

        self.assertTrue(os.path.exists(os.path.join(m.dirname, "stack_row_0.png")))
        self.assertTrue(os.path.exists(os.path.join(m.dirname, "stack_row_1.png")))
        self.assertTrue(os.path.exists(os.path.join(m.dirname, "stack.png")))

        self.assertTrue(m._last == os.path.join(m.dirname, "stack.png"))

        m.close()

    def test_stack(self):
        m = Manipulator("paper2img/tests/testdata/1412.6785v2.pdf")
        m.pdf2png(trim="100x60")
        m.stack(6, 2)
        m.resize("x400")

        self.assertTrue(os.path.exists(os.path.join(m.dirname, "resize_x400.png")))
        self.assertTrue(m._last == os.path.join(m.dirname, "resize_x400.png"))

        m.close()

    def test_out(self):
        m = Manipulator("paper2img/tests/testdata/1412.6785v2.pdf")
        target = "paper2img/tests/testdata/out.pdf"
        m.out(target)
        m.close()

        self.assertTrue(os.path.exists(target))
        subprocess.call(["rm", target])
