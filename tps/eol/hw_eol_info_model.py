# -*- coding: utf-8 -*-
import codecs
from datetime import datetime


class HardwareEOLInfo:

    def __init__(self, hw_eol_info_txt, date):
        self.hw_eol_info_txt = hw_eol_info_txt.split('\t')
        self.date = date

    def is_enable(self):
        limit = datetime.strptime(self.hw_eol_info_txt[3], '%Y/%m/%d')
        return (limit == self.date) or (limit < self.date)

    def get_dict(self):
        return {
            "asset_id": self.hw_eol_info_txt[0],
            "server_id": self.hw_eol_info_txt[1],
            "hardware_name": self.hw_eol_info_txt[2],
            "limit": datetime.strptime(self.hw_eol_info_txt[3], '%Y/%m/%d'),
            "hogehoge": self.hw_eol_info_txt[4]
        }


class HardwareEOLInfoList:

    def __init__(self, hw_eol_info_file_path, encoding, date=datetime.strptime('2999/12/31', '%Y/%m/%d')):
        self.hw_eol_info_file_path = hw_eol_info_file_path
        self.encoding = encoding
        self.date = date

    def get_list(self):
        hw_eol_info_list = []
        with codecs.open(self.hw_eol_info_file_path, 'r', self.encoding) as hw_eol_info_file:
            for hw_eol_info_txt in hw_eol_info_file:
                hw_eol_info_list.append(
                    HardwareEOLInfo(
                        hw_eol_info_txt.rstrip('\n'),
                        self.date
                    )
                )
        return map(lambda x: x.get_dict(), filter(lambda x: x.is_enable(), hw_eol_info_list))

    def get_id(self):
        return 'hw_eol_info'

    def get_key(self):
        return 'asset_id'


if __name__ == '__main__':
    HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_utf8_sample.tsv', 'utf_8').get_list()
    HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_utf8_sample.tsv', 'utf_8', '2018/01/01').get_list()
    HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_utf8_sample.tsv', 'utf_8', '2020/03/01').get_list()
    HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_eucjp_sample.tsv', 'euc_jp').get_list()
    HardwareEOLInfoList('tests/sample_file/hw_eol_info_file_sjis_sample.tsv', 'shift_jis').get_list()
