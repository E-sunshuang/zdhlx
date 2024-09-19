# 业务层
import requests
from config.config import HOST
class Login:
     def login(self,body_data):
         # 1.准备：请求路径，请求参数等数据
         urls =  f'{HOST}/mcp/pc/pcsearch'
         payload = body_data
         # 2.发送请求
         resp= requests.post(url=urls,json=payload)

         return resp.json()

if __name__ == '__main__':
    #传参：实参
    test_data= {"invoke_info": {"pos_1": [{}], "pos_2": [{}], "pos_3": [{}]}}
    #创建实例
    login = Login()
    res = login.login(test_data)
    print(res)