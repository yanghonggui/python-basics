# =====================================================================
# pet_api.py —— 对照版（2026-10-24）
# 上半部分：改造前的原始代码（只有 print 占位，不发请求）
# 下半部分：今天的改造（真发请求 + assert 断言）
# 读法：先看上半部分昨天写了什么，再对照下半部分今天改了什么
# =====================================================================

# =====================================================================
# 上半部分 · 改造前的原始代码
# =====================================================================
class PetAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, pet_id):
        url = f'{self.base_url}/pet/{pet_id}'
        print('Get:', url)

    def post(self, pet_data):
        url = f'{self.base_url}/pet'
        print('Post:', url, pet_data)

    def delete(self, pet_id):
        url = f'{self.base_url}/pet/{pet_id}'
        print('Delete:', url)


api = PetAPI('https://petstore.swagger.io/v2')

# 原始版的调用：只为对照保留，注释掉，避免和下半部分输出混在一起
# api.get(1)
# api.post(1)
# api.delete(5)


# =====================================================================
# 下半部分 · 今天的改造（真发请求 + 断言）
'''
 Base：https://petstore.swagger.io/v2
  - POST https://petstore.swagger.io/v2/pet — 新增宠物  传参：JSON：id、name 等
  - GET https://petstore.swagger.io/v2/pet/{petId} — 按 id 查询宠物
  - PUT https://petstore.swagger.io/v2/pet — 更新宠物
  - DELETE https://petstore.swagger.io/v2/pet/{petId} — 删除宠物
'''
# =====================================================================
import requests

class PetAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, pet_id):
        # 改造：照 post 的样子，把 get 改成真请求,套路：拼 url → requests.get → assert 200 → print 状态码 → return r.json()
        url = f'{self.base_url}/pet/{pet_id}'
        r = requests.get(url)
        assert r.status_code == 200, f'请求失败:{r.status_code}'
        # print(f'函数内打印_Get:', re.status_code)
        return r.json()


        # 今天的改造要点：
        # 1. 拼出接口地址：f'{self.base_url}/pet'（self.base_url 只到 /v2，不带 /pet）
        # 2. requests.post(url, json=pet_data) 真发请求，结果存到 r
        # 3. assert r.status_code == 200, '创建失败' —— 条件不满足就抛 AssertionError，函数停下
        # 4. return r.json()
    def post(self, pet_data):
        url = f'{self.base_url}/pet'
        r = requests.post(url, json=pet_data)
        assert r.status_code == 200, '创建失败'
        # print(f'函数内打印_Post:', r.status_code)
        return r.json()

    def put(self, pet_data):
        url = f'{self.base_url}/pet'
        r = requests.put(url, json=pet_data)
        assert r.status_code == 200, f'更新失败:{r.status_code}'
        return r.json()

    def delete(self, pet_id):
        url = f'{self.base_url}/pet/{pet_id}'
        r = requests.delete(url)
        assert r.status_code == 200, f'删除失败:{r.status_code}'
        return r.json()


if __name__ == '__main__':
    api = PetAPI('https://petstore.swagger.io/v2')
    r1 = api.post({"id": 1, 'name': 'dog'},timeout =10)
    # 增加断言
    assert r1['name'] == 'dog'
    print(f'post 请求是：', r1)

    r2 = api.get(r1['id'],timeout =10)
    print(f'Get 请求的是：', r2)

    r3 = api.put({'id': r1['id'], 'name': 'dog2'},timeout =10)
    print(f'Put 更新后的数据是：', r3)

    r4 = api.get(r3['id'],timeout =10)
    assert r4['name'] == 'dog2', f'更新不成功，{r4["name"]}'
    print(f'Get 请求的是：', r4)

    r5 = api.delete(r4['id'],timeout =10)
    print(f'Delete 请求的是：', r5)

    # 删除后要证明真删掉了
    url = f'https://petstore.swagger.io/v2/pet/{r4['id']}'
    r = requests.get(url,timeout =10)
    assert r.status_code == 404
    print(f'请求的地址是：', url)
    print(f'删除成功')



