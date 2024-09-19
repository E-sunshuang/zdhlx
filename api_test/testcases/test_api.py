import requests
from config.config import HOST


def test_api():
    urls = f'{HOST}/mcp/pc/pcsearch'
    data = {"invoke_info": {"pos_1": [{}], "pos_2": [{}], "pos_3": [{}]}}

    res = requests.post(url=urls,json=data)
    print(res.text)


if __name__ == '__main__':
    test_api()