# -*- coding: utf-8 -*-
import codecs


class ServerInfo:

    def __init__(self, sv_info_txt):
        self.sv_info_txt = sv_info_txt.split('\t')

    def get_dict(self):
        return {
            "asset_id": self.sv_info_txt[0],
            "server_id": self.sv_info_txt[1],
            "hogehoge": self.sv_info_txt[2]
        }


class ServerInfoList:

    def __init__(self, sv_info_file_path, encoding):
        self.sv_info_file_path = sv_info_file_path
        self.encoding = encoding

    def get_list(self):
        sv_info_list = []
        with codecs.open(self.sv_info_file_path, 'r', self.encoding) as sv_info_file:
            for sv_info_txt in sv_info_file:
                sv_info_list.append(ServerInfo(sv_info_txt.rstrip('\n')))
        return map(lambda x: x.get_dict(), sv_info_list)

    def get_id(self):
        return 'sv_info'

    def get_key(self):
        return 'asset_id'


if __name__ == '__main__':
    ServerInfoList('tests/sample_file/sv_info_file_eucjp_sample.tsv', 'euc_jp').get_list()
    ServerInfoList('tests/sample_file/sv_info_file_sjis_sample.tsv', 'shift_jis').get_list()
    ServerInfoList('tests/sample_file/sv_info_file_utf8_sample.tsv', 'utf_8').get_list()
