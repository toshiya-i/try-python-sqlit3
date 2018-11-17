# -*- coding: utf-8 -*-


class EndOfLifeViewer:

    def __init__(self, eol_list):
        self.eol_list = eol_list

    def view_for_cli(self):
        for eol_info in self.eol_list:
            print('\t'.join(eol_info))


if __name__ == '__main__':
    normal_case1 = [
        ["aa01", "bb01", "cc01", "2019-01-01", "bb01", "cc01"],
        ["aa02", "bb02", "none", "2019-01-02", "bb02", "cc02"],
        ["aa03", "bb03", u"cc三", "2019-01-03", "bb03", u"cc三"]
    ]
    EndOfLifeViewer(normal_case1).view_for_cli()
