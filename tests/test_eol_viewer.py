# -*- coding: utf-8 -*-
import unittest
from test.test_support import captured_stdout
from tps.eol.eol_viewer import EndOfLifeViewer


class TestEndOfLifeViewer(unittest.TestCase):

    def test_view_for_cli_normal_case1(self):
        normal_case1 = [
            ["aa01", "bb01", "cc01", "2019-01-01", "bb01", "cc01"],
            ["aa02", "bb02", "none", "2019-01-02", "bb02", "cc02"],
            ["aa03", "bb03", u"cc三", "2019-01-03", "bb03", u"cc三"]
        ]
        with captured_stdout() as stdout:
            EndOfLifeViewer(normal_case1).view_for_cli()
            lines = stdout.getvalue().splitlines()
        self.assertEqual(lines[0], 'aa01\tbb01\tcc01\t2019-01-01\tbb01\tcc01')
        self.assertEqual(lines[1], 'aa02\tbb02\tnone\t2019-01-02\tbb02\tcc02')
        self.assertEqual(lines[2], u'aa03\tbb03\tcc三\t2019-01-03\tbb03\tcc三')

    def test_view_for_cli_error_case1(self):
        error_case1 = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(TypeError):
            EndOfLifeViewer(error_case1).view_for_cli()

    def test_view_for_cli_error_case2(self):
        error_case2 = [1, 2, 3]
        with self.assertRaises(TypeError):
            EndOfLifeViewer(error_case2).view_for_cli()


if __name__ == '__main__':
    unittest.main()
