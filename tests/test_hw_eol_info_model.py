# -*- coding: utf-8 -*-
import unittest
from datetime import datetime
from tps.eol.hw_eol_info_model import HardwareEOLInfo, HardwareEOLInfoList


class TestHardwareEOLInfo(unittest.TestCase):

    def test_init_error_case(self):
        with self.assertRaises(AttributeError):
            HardwareEOLInfo(None, datetime.strptime('2018/01/01', '%Y/%m/%d'))

    def test_is_enable_normal_case1(self):
        normal_case1 = 'aa01\tbb02\tcc03\t2017/12/31'
        self.assertEqual(HardwareEOLInfo(normal_case1,
                                         datetime.strptime('2017/12/31', '%Y/%m/%d')).is_enable(),
                         True)
        self.assertEqual(HardwareEOLInfo(normal_case1,
                                         datetime.strptime('2018/01/01', '%Y/%m/%d')).is_enable(),
                         True)
        normal_case1 = 'aa01\tbb02\tcc03\t2018/01/01'
        self.assertEqual(HardwareEOLInfo(normal_case1,
                                         datetime.strptime('2017/12/31', '%Y/%m/%d')).is_enable(),
                         False)
        normal_case1 = 'aa01\tbb02\tcc03\t2020/02/29'
        self.assertEqual(HardwareEOLInfo(normal_case1,
                                         datetime.strptime('2020/03/01', '%Y/%m/%d')).is_enable(),
                         True)

    def test_is_enable_error_case1(self):
        with self.assertRaises(IndexError):
            HardwareEOLInfo('aa01\tbb02\tcc03',
                            datetime.strptime('2018/01/01', '%Y/%m/%d')).is_enable()
        with self.assertRaises(ValueError):
            HardwareEOLInfo('aa01\tbb02\tcc03\tabc',
                            datetime.strptime('2018/01/01', '%Y/%m/%d')).is_enable()
        with self.assertRaises(ValueError):
            HardwareEOLInfo('aa01\tbb02\tcc03\t2018/02/29',
                            datetime.strptime('2018/01/01', '%Y/%m/%d')).is_enable()

    def test_get_dict_normal_case1(self):
        normal_case1 = 'aa01\tbb02\tcc03\t2018/01/01\thoge04'
        self.assertEqual(HardwareEOLInfo(normal_case1,
                                         datetime.strptime('2018/01/01', '%Y/%m/%d')).get_dict(),
                         {'asset_id': 'aa01',
                          'hardware_name': 'cc03',
                          'hogehoge': 'hoge04',
                          'limit': datetime.strptime('2018/01/01', '%Y/%m/%d'),
                          'server_id': 'bb02'})

    def test_get_dict_error_case1(self):
        with self.assertRaises(IndexError):
            HardwareEOLInfo('aa01\tbb02\tcc03\t2018/01/01',
                            datetime.strptime('2018/01/01', '%Y/%m/%d')).get_dict()
        with self.assertRaises(ValueError):
            HardwareEOLInfo('aa01\tbb02\tcc03\tabc\thoge04',
                            datetime.strptime('2018/01/01', '%Y/%m/%d')).get_dict()
        with self.assertRaises(ValueError):
            HardwareEOLInfo('aa01\tbb02\tcc03\t2018/02/29\thoge04',
                            datetime.strptime('2018/01/01', '%Y/%m/%d')).get_dict()


class TestHardwareEOLInfoList(unittest.TestCase):

    def test_get_list_normal_case1(self):
        self.assertEqual(HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_utf8_sample.tsv', 'utf8').get_list(),
                         [{'asset_id': u'as001', 'hogehoge': u'as001hogehoge', 'server_id': u'sv001', 'limit': datetime(2018, 1, 1, 0, 0), 'hardware_name': u'hn001'},
                          {'asset_id': u'as002', 'hogehoge': u'', 'server_id': u'sv002', 'limit': datetime(2018, 2, 2, 0, 0), 'hardware_name': u'hn002'},
                          {'asset_id': u'as003', 'hogehoge': u'as003hogehoge', 'server_id': u'sv003', 'limit': datetime(2018, 3, 3, 0, 0), 'hardware_name': u''},
                          {'asset_id': u'as004', 'hogehoge': u'as004hogehoge', 'server_id': u'', 'limit': datetime(2018, 4, 4, 0, 0), 'hardware_name': u'hn004'},
                          {'asset_id': u'', 'hogehoge': u'as005hogehoge', 'server_id': u'sv005', 'limit': datetime(2018, 5, 5, 0, 0), 'hardware_name': u'hn005'},
                          {'asset_id': u'', 'hogehoge': u'', 'server_id': u'', 'limit': datetime(2018, 6, 6, 0, 0), 'hardware_name': u''},
                          {'asset_id': u'as007', 'hogehoge': u'as007hogehoge', 'server_id': u'sv007', 'limit': datetime(2999, 12, 30, 0, 0), 'hardware_name': u'hn007'},
                          {'asset_id': u'as008', 'hogehoge': u'as008hogehoge', 'server_id': u'sv008', 'limit': datetime(2999, 12, 31, 0, 0), 'hardware_name': u'hn008'},
                          {'asset_id': u'as010', 'hogehoge': u'as010hogehoge', 'server_id': u'sv010', 'limit': datetime(2017, 12, 31, 0, 0), 'hardware_name': u'hn010'},
                          {'asset_id': u'as011', 'hogehoge': u'as011hogehoge', 'server_id': u'sv011', 'limit': datetime(2020, 2, 29, 0, 0), 'hardware_name': u'hn011'},
                          {'asset_id': u'as012', 'hogehoge': u'as012hogehoge', 'server_id': u'sv十二', 'limit': datetime(2018, 1, 12, 0, 0), 'hardware_name': u'hn十二'}])

    def test_get_list_normal_case2(self):
        self.assertEqual(HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_utf8_sample.tsv', 'utf8', datetime(2017, 12, 30, 0, 0)).get_list(),
                         [])

    def test_get_list_normal_case3(self):
        self.assertEqual(HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_utf8_sample.tsv', 'utf8', datetime(2017, 12, 31, 0, 0)).get_list(),
                         [{'asset_id': u'as010', 'hogehoge': u'as010hogehoge', 'server_id': u'sv010', 'limit': datetime(2017, 12, 31, 0, 0), 'hardware_name': u'hn010'}])

    def test_get_list_normal_case4(self):
        self.assertEqual(HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_eucjp_sample.tsv', 'euc_jp').get_list(),
                         [{'asset_id': u'as001', 'hogehoge': u'as001hogehoge', 'server_id': u'sv一', 'limit': datetime(2018, 1, 1, 0, 0), 'hardware_name': u'hn一'}])

    def test_get_list_normal_case5(self):
        self.assertEqual(HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_sjis_sample.tsv', 'shift_jis').get_list(),
                         [{'asset_id': u'as001', 'hogehoge': u'as001hogehoge', 'server_id': u'sv一', 'limit': datetime(2018, 1, 1, 0, 0), 'hardware_name': u'hn一'}])

    def test_get_dict_error_case1(self):
        with self.assertRaises(IOError):
            HardwareEOLInfoList('tests/sample_file/non.tsv', 'utf_8').get_list()

    def test_get_dict_error_case2(self):
        with self.assertRaises(LookupError):
            HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_utf8_sample.tsv', 'ed_error').get_list()


if __name__ == '__main__':
    unittest.main()
