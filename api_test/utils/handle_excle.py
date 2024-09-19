'''
功能需求：获取excle文件指定数据
入参：
    -文件路径
    -指定sheet表
    -指定单元格
出参：
    -返回数据是什么
    -返回数据类型
'''
import json

import xlrd
def get_excel_data(file_path,sheet_name,case_name):
    # formatting_info=True   保持原样式
    res_list = []  #初始元组
    work_book = xlrd.open_workbook(file_path,formatting_info=True)
    work_sheet = work_book.sheet_by_name(sheet_name)


    row_index = 1
    for one in work_sheet.col_values(0):
        if case_name in one:
            # 请求体
            req_bady = work_sheet.cell(row_index,6).value
            # 显影结果
            exp_data = work_sheet.cell(row_index,7).value
            res_list.append((json.loads(req_bady),json.loads(exp_data)))
    row_index += 1


    return res_list

if __name__ == '__main__':
    res = get_excel_data('../data/exam.xls', 'test1', '')
    print(res)

