import xlrd

def read_excel(file_path,sheet_name,case_name):
    list = []
    work_book = xlrd.open_workbook(file_path,formatting_info=True)
    sheet_book = work_book.sheet_by_name(sheet_name)

    index = 0
    for one in sheet_book.col_values(0):
        if case_name in one:
            req_body = sheet_book.cell(index,6)
            res = sheet_book.cell(index,7)

            list.append((req_body,res))

        index += 1

    return list

if __name__ == '__main__':
    result = read_excel('../data/exam.xls','test1','')
    print(result)