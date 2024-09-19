#初始化
import pytest
#自动化测试执行前的初始化操作
#自动化测试完成后，数据清除操作
@pytest.fixture(scope="session",autouse=True)
def start_running():
    print("开始")
    yield
    print("结束")