'''
  常用命令：
  python -m pytest -v           详细模式：逐条显示用例名和 PASSED/FAILED（不加 -v 只显示 . 和 F）
  python -m pytest -k 关键字    只跑名字里含关键字的用例
  python -m pytest -s           显示用例里的 print 输出（默认被捕获不显示）
  python -m pytest -x           第一条失败就停
  python -m pytest -m 标记      只跑带该标记的用例（如 smoke）
'''

# ======================================加入fixture前===============================

# from pet_api import PetAPI
# import requests
#
# def test_httpbin_status():
#     url = 'https://httpbin.org/status/200'
#     r = requests.get(url,timeout=5)
#     assert r.status_code == 200
#
# api = PetAPI('https://petstore.swagger.io/v2')
#
# def test_pet_flow():
#     r1 =api.post({'id': 1, 'name': 'dog'})
#     assert r1['name'] == 'dog'
#
#     r2 =api.get(r1['id'])
#     assert r2['name'] == 'dog'
#
#     r3 = api.put({'id': 1, 'name': 'cat'})
#     assert r3['name'] == 'cat'
#
#     r4 = api.get(r1['id'])
#     assert r4['name'] == 'cat'
#
#     r5 = api.delete(r4['id'])
#     assert r5['code'] == 200
#
#     pet_id = r4['id']
#     url = f'https://petstore.swagger.io/v2/pet/{pet_id}'
#     r = requests.get(url)
#     assert r.status_code == 404


# =======================================改造=加入fixture==============================
import requests
import pytest
from pet_api import PetAPI

def test_httpbin_status():
    url = 'https://httpbin.org/status/200'
    r = requests.get(url,timeout=5)
    assert r.status_code == 200

@pytest.fixture
def api():
    return PetAPI('https://petstore.swagger.io/v2')

def test_pet_flow(api):
    r1 =api.post({'id': 1, 'name': 'dog'})
    assert r1['name'] == 'dog'

    r2 =api.get(r1['id'])
    assert r2['name'] == 'dog'

    r3 = api.put({'id': 1, 'name': 'cat'})
    assert r3['name'] == 'cat'

    r4 = api.get(r1['id'])
    assert r4['name'] == 'cat'

    r5 = api.delete(r4['id'])
    assert r5['code'] == 200

    pet_id = r4['id']
    url = f'https://petstore.swagger.io/v2/pet/{pet_id}'
    r = requests.get(url)
    assert r.status_code == 404

@pytest.mark.parametrize('code', [200,201,204,404])
def test_httpbin_status_codes(code):
    url = f'https://httpbin.org/status/{code}'
    r = requests.get(url,timeout=5)
    assert r.status_code == code