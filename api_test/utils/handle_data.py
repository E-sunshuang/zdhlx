# utils工具包
# 处理数据：加密方法
'''
入参：需加密的明文
出参：已加密的密文
'''
import hashlib


def get_md5_data(data:str):
    #实例化
    md5 =hashlib.md5()
    #加密
    md5.update(data.encode('utf-8'))
    #返回加密结果
    return md5.hexdigest()