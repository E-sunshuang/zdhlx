#测试类
from libs.login import Login
import pytest
import allure,os

from utils.handle_excle import get_excel_data


class TestSearch:
    #定义测试方法
    #数据驱动
    @pytest.mark.parametrize('req_bady,exp_data',get_excel_data('../data/exam.xls', 'test1', ''))
    def test_search(self,req_bady,exp_data):
        res = Login().login(req_bady)
        assert res['errmsg'] == exp_data['errmsg']

if __name__ == '__main__':
    # __file__ :当前文件
    pytest.main(["test_search.py","-s","--alluredir","../report/tmp"])  # -s 打印 输出
    os.system("allure serve ../report/tmp")

