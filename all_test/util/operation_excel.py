# coding:utf-8
import xlrd
from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None, copy_file_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataConfig/interface.xlsx'
            self.sheet_id = 0
        if copy_file_name is None:
            self.data = self.get_data()
        else:
            # 如果是输出文件，则
            data = xlrd.open_workbook(copy_file_name)
            new_data = copy(data)
            new_data.save(self.file_name)
            self.data = self.get_data()

    def get_all_data(self):
        data = xlrd.open_workbook(self.file_name)
        return data

    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheets()[self.sheet_id]

        return table

    def get_lines(self):
        return self.data.nrows

    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的case_id找到对应行的内容
    def get_rows_data(self, case_id):
        return self.get_row_values(self.get_row_num(case_id))

    # 根据对应的case_id找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1

    # 根据行号，找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id is not None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_rows_data("test-002"))
    print(opers.get_cell_value(1, 1))

