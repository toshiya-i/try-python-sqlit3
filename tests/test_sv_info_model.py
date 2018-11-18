# -*- coding: utf-8 -*-
import unittest
from tps.eol.sv_info_model import ServerInfo, ServerInfoList


class TestServerInfo(unittest.TestCase):

    def test_get_dict_normal_case1(self):
        normal_case1 = 'aa01\tbb02\tcc03'
        self.assertEqual(ServerInfo(normal_case1).get_dict(),
                         {'asset_id': 'aa01',
                          'server_id': 'bb02',
                          'hogehoge': 'cc03'})

    def test_get_dict_error_case1(self):
        error_case1 = 'aa01\tbb02'
        with self.assertRaises(IndexError):
            ServerInfo(error_case1).get_dict()


class TestServerInfoList(unittest.TestCase):

    def test_get_dict_normal_case1(self):
        self.assertEqual(ServerInfoList('tests/sample_file/sv_info_file_eucjp_sample.tsv', 'euc_jp').get_list(),
                         [{'asset_id': u'as001', 'server_id': u'sv001', 'hogehoge': u'as001hogehoge'},
                          {'asset_id': u'as002', 'server_id': u'sv002', 'hogehoge': u''},
                          {'asset_id': u'as003', 'server_id': u'', 'hogehoge': u'as003hogehoge'},
                          {'asset_id': u'', 'server_id': u'sv004', 'hogehoge': u'as004hogehoge'},
                          {'asset_id': u'', 'server_id': u'', 'hogehoge': u'as005hogehoge'},
                          {'asset_id': u'', 'server_id': u'sv006', 'hogehoge': u''},
                          {'asset_id': u'as007', 'server_id': u'', 'hogehoge': u''},
                          {'asset_id': u'', 'server_id': u'', 'hogehoge': u''},
                          {'asset_id': u'as009', 'server_id': u'sv九', 'hogehoge': u'as009hogehoge'}])

    def test_get_dict_normal_case2(self):
        self.assertEqual(ServerInfoList('tests/sample_file/sv_info_file_sjis_sample.tsv', 'shift_jis').get_list(),
                         [{'asset_id': u'as001', 'server_id': u'sv001', 'hogehoge': u'as001hogehoge'},
                          {'asset_id': u'as002', 'server_id': u'sv002', 'hogehoge': u''},
                          {'asset_id': u'as003', 'server_id': u'', 'hogehoge': u'as003hogehoge'},
                          {'asset_id': u'', 'server_id': u'sv004', 'hogehoge': u'as004hogehoge'},
                          {'asset_id': u'', 'server_id': u'', 'hogehoge': u'as005hogehoge'},
                          {'asset_id': u'', 'server_id': u'sv006', 'hogehoge': u''},
                          {'asset_id': u'as007', 'server_id': u'', 'hogehoge': u''},
                          {'asset_id': u'', 'server_id': u'', 'hogehoge': u''},
                          {'asset_id': u'as009', 'server_id': u'sv九', 'hogehoge': u'as009hogehoge'}])

    def test_get_dict_normal_case3(self):
        self.assertEqual(ServerInfoList('tests/sample_file/sv_info_file_utf8_sample.tsv', 'utf_8').get_list(),
                         [{'asset_id': u'as001', 'server_id': u'sv001', 'hogehoge': u'as001hogehoge'},
                          {'asset_id': u'as002', 'server_id': u'sv002', 'hogehoge': u''},
                          {'asset_id': u'as003', 'server_id': u'', 'hogehoge': u'as003hogehoge'},
                          {'asset_id': u'', 'server_id': u'sv004', 'hogehoge': u'as004hogehoge'},
                          {'asset_id': u'', 'server_id': u'', 'hogehoge': u'as005hogehoge'},
                          {'asset_id': u'', 'server_id': u'sv006', 'hogehoge': u''},
                          {'asset_id': u'as007', 'server_id': u'', 'hogehoge': u''},
                          {'asset_id': u'', 'server_id': u'', 'hogehoge': u''},
                          {'asset_id': u'as009', 'server_id': u'sv九', 'hogehoge': u'as009hogehoge'}])

    def test_get_dict_error_case1(self):
        with self.assertRaises(IOError):
            ServerInfoList('tests/sample_file/non.tsv', 'utf_8').get_list()

    def test_get_dict_error_case2(self):
        with self.assertRaises(LookupError):
            ServerInfoList('tests/sample_file/sv_info_file_utf8_sample.tsv', 'ed_error').get_list()


if __name__ == '__main__':
    unittest.main()
