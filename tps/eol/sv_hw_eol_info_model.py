# -*- coding: utf-8 -*-
import sqlite3
from contextlib import closing


class ServerHardwareEndOfLifeInfoList:

    def __init__(self,
                 sv_info_list,
                 hw_eol_info_list,
                 eol_viewer):
        self.sv_info_list = sv_info_list
        self.hw_eol_info_list = hw_eol_info_list
        self.eol_viewer = eol_viewer

    def create_list(self):
        print(left_join(self.sv_info_list.get_id(),
                        self.sv_info_list.get_list(),
                        self.sv_info_list.get_key(),
                        self.hw_eol_info_list.get_id(),
                        self.hw_eol_info_list.get_list(),
                        self.hw_eol_info_list.get_key()))


def left_join(left_table_name,
              left_data,
              left_key,
              right_table_name,
              right_data,
              right_key):
    result = []
    with closing(sqlite3.connect(":memory:")) as con:
        cur = con.cursor()
        lkeys = left_data[0].keys()
        cur.execute(make_create_sql(left_table_name, lkeys))
        cur.executemany(make_insert_sql(left_table_name, lkeys),
                        dict_list_to_value_tuple_list(left_data, lkeys))
        rkeys = right_data[0].keys()
        cur.execute(make_create_sql(right_table_name, rkeys))
        cur.executemany(make_insert_sql(right_table_name, rkeys),
                        dict_list_to_value_tuple_list(right_data, rkeys))
        cur.execute(make_left_outer_join_sql(left_table_name,
                                             lkeys,
                                             left_key,
                                             right_table_name,
                                             rkeys,
                                             right_key))
        result = value_tuple_list_to_dict_list(cur.fetchall(),
                                               make_left_outer_join_select_columns(left_table_name,
                                                                                   lkeys,
                                                                                   right_table_name,
                                                                                   rkeys))
    return result


def make_create_sql(table_name, keys):
    return 'create table {} ({})'.format(table_name, ','.join(keys))


def make_insert_sql(table_name, keys):
    return 'insert into {} values ({})'.format(table_name, ','.join(map(lambda x: '?', keys)))


def dict_list_to_value_tuple_list(dict_list, keys):
    result = []
    for dict_data in dict_list:
        result.append(tuple(map(lambda x: dict_data[x], keys)))
    return result


def make_left_outer_join_select_columns(left_table_name, left_columns, right_table_name, right_columns):
    return map(lambda x: left_table_name + '.' + x, left_columns) + map(lambda x: right_table_name + '.' + x, right_columns)


def make_left_outer_join_sql(left_table_name, left_columns, left_key, right_table_name, right_columns, right_key):
    select_columns = ','.join(make_left_outer_join_select_columns(left_table_name,
                                                                  left_columns,
                                                                  right_table_name,
                                                                  right_columns))
    return 'select {} from {} left outer join {} on {} = {}'.format(select_columns,
                                                             left_table_name,
                                                             right_table_name,
                                                             left_table_name + '.' + left_key,
                                                             right_table_name + '.' + right_key)


def value_tuple_list_to_dict_list(value_tuple_list, keys):
    return map(lambda x: value_tuple_to_dict(x, keys), value_tuple_list)


def value_tuple_to_dict(value_tuple, keys):
    result = {}
    for i, key in enumerate(keys):
        result[key] = value_tuple[i]
    return result


if __name__ == '__main__':
    pass
