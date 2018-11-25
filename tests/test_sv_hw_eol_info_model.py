# -*- coding: utf-8 -*-
import unittest
from tps.eol.sv_hw_eol_info_model import left_join
from tps.eol.sv_hw_eol_info_model import make_create_sql
from tps.eol.sv_hw_eol_info_model import make_insert_sql
from tps.eol.sv_hw_eol_info_model import dict_list_to_value_tuple_list
from tps.eol.sv_hw_eol_info_model import make_left_outer_join_select_columns
from tps.eol.sv_hw_eol_info_model import make_left_outer_join_sql
from tps.eol.sv_hw_eol_info_model import value_tuple_list_to_dict_list
from tps.eol.sv_hw_eol_info_model import value_tuple_to_dict


class TestFunction(unittest.TestCase):

    def test_left_join_normal_case1(self):
        left_normal_case1 = [{'key': 'a', 'data': '0'},
                             {'key': 'b', 'data': '1'},
                             {'key': 'a', 'data': '2'},
                             {'key': 'b', 'data': '3'},
                             {'key': 'c', 'data': '4'},
                             {'key': 'a', 'data': '5'}]
        right_normal_case1 = [{'key': 'a', 'data': '0'},
                              {'key': 'b', 'data': '1'},
                              {'key': 'd', 'data': '2'}]
        self.assertEqual(left_join('left',
                                   left_normal_case1,
                                   'key',
                                   'right',
                                   right_normal_case1,
                                   'key'),
                         [{'left.data': u'0', 'left.key': u'a', 'right.data': u'0', 'right.key': u'a'},
                          {'left.data': u'1', 'left.key': u'b', 'right.data': u'1', 'right.key': u'b'},
                          {'left.data': u'2', 'left.key': u'a', 'right.data': u'0', 'right.key': u'a'},
                          {'left.data': u'3', 'left.key': u'b', 'right.data': u'1', 'right.key': u'b'},
                          {'left.data': u'4', 'left.key': u'c', 'right.data': None, 'right.key': None},
                          {'left.data': u'5', 'left.key': u'a', 'right.data': u'0', 'right.key': u'a'}])

    def test_make_create_sql_normal_case1(self):
        self.assertEqual(make_create_sql('test', ['aa', 'bb']),
                         'create table test (aa,bb)')

    def test_make_insert_sql_normal_case1(self):
        self.assertEqual(make_insert_sql('test', ['aa', 'bb']),
                         'insert into test values (?,?)')

    def test_dict_list_to_value_tuple_list_normal_case1(self):
        normal_case1 = [{'key': 'a', 'data': '0'},
                        {'key': 'b', 'data': '1'}]
        self.assertEqual(dict_list_to_value_tuple_list(normal_case1, normal_case1[0].keys()),
                         [('0', 'a'), ('1', 'b')])

    def test_make_left_outer_join_select_columns_normal_case1(self):
        self.assertEqual(make_left_outer_join_select_columns('test1',
                                                             ['aa', 'bb'],
                                                             'test2',
                                                             ['cc', 'dd']),
                         ['test1.aa', 'test1.bb', 'test2.cc', 'test2.dd'])

    def test_make_left_outer_join_sql_normal_case1(self):
        self.assertEqual(make_left_outer_join_sql('test1',
                                                  ['aa', 'bb'],
                                                  'aa',
                                                  'test2',
                                                  ['cc', 'dd'],
                                                  'cc'),
                         'select test1.aa,test1.bb,test2.cc,test2.dd from test1 left outer join test2 on test1.aa = test2.cc')

    def test_value_tuple_list_to_dict_list_normal_case1(self):
        self.assertEqual(value_tuple_list_to_dict_list([('aa', 'bb'), ('cc', 'dd')], ['test1', 'test2']),
                         [{'test1': 'aa', 'test2': 'bb'}, {'test1': 'cc', 'test2': 'dd'}])

    def test_value_tuple_to_dict_normal_case1(self):
        self.assertEqual(value_tuple_to_dict(('aa', 'bb'), ['test1', 'test2']),
                         {'test1': 'aa', 'test2': 'bb'})


if __name__ == '__main__':
    unittest.main()
