# name = '杨洪桂'
# years = 9
# goal = '成为一名自动化测试工程师'
#
# print(f'大家好，我的名字叫{name}，做了{years}年测试了，目标是{goal}。明年就是{years+1}年测试了！')
#
# import  json
# print(len(json.load(open('cases.json',encoding='utf-8'))))

# ===============================================================================

# products = [
#     {'name': 'Wireless Mouse', 'stock': 12},
#     {'name': 'Mechanical Keyboard', 'stock': 3},
#     {'name': 'wireless charger', 'stock': 0},
#     {'name': 'Usb-C Cable', 'stock': 25 }
# ]
#
# def search_stock(products, keyword):
#     if keyword == '':
#         return {'count': 0, 'total_stock': 0}
#     count = 0
#     total_stock = 0
#     for item in products:
#         if keyword.lower() in item['name'].lower():
#             count += 1
#             total_stock += item['stock']
#     return {'count': count, 'total_stock': total_stock}
#
#
# nums = search_stock(products, keyword='wireless')
# print(f'数量是：{nums}')

# nums = [3, 8, 1, 6, 10, 7],用 for + if 数出有几个偶数，最后打印： 偶数个数：3
# nums = [3, 8, 1, 6, 10, 7]
#
# count = 0
# for item in nums:
#     if item % 2 == 0:
#         count += 1
# print(f'偶数的个数是：{count}')


# codes = [200, 404, 500, 201, 403, 200, 302, 500]，数出其中 >= 400 的个数，最后打印 错误数：4。
codes = [200, 404, 500, 201, 403, 200, 302, 500]

# li = []
# for code in codes:
#     if code >= 400:
#         li.append(code)
# print(len(li))
#
# li =[c for c in codes if c >= 400]
# print(len(li))





# 必背内容------26.10.23
# 1、 1. codes = [200, 404, 500, 201, 403, 200, 302, 500]，数 >= 400 的个数
codes = [200, 404, 500, 201, 403, 200, 302, 500]

# num = []
# for code in codes:
#     if code >= 400:
#         num.append(code)
# print(len(num))

# 2. 把第 1 题包成函数 count_errors(codes)，返回计数；外面调用一次并 print
# def count_errors(codes):
#     errors = []
#     for code in codes:
#         if code >= 400:
#             errors.append(code)
#     return len(errors)
#
# print(count_errors(codes))

# 3.GET https://httpbin.org/delay/3，timeout=1，捕获超时后打印「请求超时」

import requests
# url = 'https://httpbin.org/delay/3'
# try:
#     response = requests.get(url,timeout=1)
#     print(response.status_code)
# except requests.exceptions.Timeout:
#     print(f'请求超时')


# 4. 写 class PetAPI：__init__(self, base_url) 把参数存成属性；一个方法 get_status(self) 返回 f-string 拼上 self.base_url

# class PetAPI:
#     def __init__(self,base_url):
#         self.base_url = base_url
#
#     def get_status(self):
#         return f'这个地址是：{self.base_url}'
#
# api = PetAPI('https://httpbin.org/status/')
# print(api.get_status())


#  5. GET https://jsonplaceholder.typicode.com/posts/1（带 headers、timeout=5）打印 status_code；
#    POST https://httpbin.org/post（json 传两个字段）打印响应里的 form/json

# url ='https://jsonplaceholder.typicode.com/posts/1'
# headers = {'User-Agent': 'Mozilla/5.0'}
# re = requests.get(url, headers=headers,timeout=5)
# print(re.status_code)

# url = 'https://httpbin.org/post'
# data = {'a': 1, 'b': 2}
# re = requests.post(url, data=data)
# print(re.json()['form'])

# 必背题默写---26.10.24
# 1. codes = [200, 404, 500, 201, 403, 200, 302, 500]，数出 >= 400 的个数（for + if）
# codes = [200, 404, 500, 201, 403, 200, 302, 500]

# li = []
# for code in codes:
#     if code >= 400:
#         li.append(code)
# print(len(li))

# 2. 第 1 题包成函数 count_errors(codes)，返回计数；外面调用一次并 print
# def count_errors(codes):
#     li = []
#     for code in codes:
#         if code >= 400:
#             li.append(code)
#     return len(li)
#
# print(count_errors(codes))

# 3. GET https://httpbin.org/delay/3，timeout=1，捕获超时后打印「请求超时」
import requests
# url = 'https://httpbin.org/delay/3'
# try:
#     re = requests.get(url,timeout=1)
#
# except requests.exceptions.Timeout:
#     print(f'请求超时')

#4. class PetAPI：__init__(self, base_url) 存属性；get_status(self) 返回 f-string 拼上 self.base_url
# class PetAPI:
#     def __init__(self,base_url):
#         self.base_url = base_url
#
#     def get_status(self):
#         return f'请求地址是：{self.base_url}'
#
# api = PetAPI(base_url='http://127.0.0.1:5000/')
# print(api.get_status())

#   5. GET https://jsonplaceholder.typicode.com/posts/1（带 headers、timeout=5）打印 status_code；
#      POST https://httpbin.org/post（json 传两个字段）打印响应里的 json

# url ='https://jsonplaceholder.typicode.com/posts/1'
# headers = {'User-Agent': 'Mozilla/5.0'}
# re = requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=5)
# print(re.status_code)

# url = 'https://httpbin.org/post'
# data = {'name': 'haha','age': 1}
# r = requests.post(url,data=data)    #data传参，对应postman里的 x-www-form-urlencoded 以form取json参数，json中数字类带引号
# print(r.json()['form'])
#
# json = {'name': 'haha','age': 1}
# re = requests.post(url,json=json)  #json传参，对应postman里的raw+json，以json取参数，json中不带引号
# print(re.json()['json'])
#



#  第二段热身题（独立小题，10 分钟）：
# orders = [
#       {'price': 30, 'count': 2},
#       {'price': 15, 'count': 1},
#       {'price': 8, 'count': 5},
#   ]
#   写函数 total_amount(orders)，返回总金额。先写合同四问，再动笔；

# orders = [
#       {'price': 30, 'count': 2},
#       {'price': 15, 'count': 1},
#       {'price': 8, 'count': 5},
#   ]
#
# def total_amount(orders):
#     total = 0
#     for order in orders:
#         total += order['price'] * order['count']
#     return total
#
# print(total_amount(orders))

# 热身题： 26.10.26
#   1. times = [120, 350, 890, 210, 1500, 640]（毫秒）：for + if 数出 > 500 的个数，打印「慢请求数：3」。
# times = [120, 350, 890, 210, 1500, 640]
# num = []
# for t in times:
#     if t > 500:
#         num.append(t)
# print(f'慢请求数：',len(num))

#   2. 把第 1 题包成函数 count_slow(times)，返回个数；外面调用一次并 print。
# def count_slow(times):
#     count = []
#     for t in times:
#         if t > 500:
#             count.append(t)
#     return  len(count)
#
# print (f'慢请求数:',count_slow(times))


#   3. 接口写法：
#- PUT https://petstore.swagger.io/v2/pet —— 更新宠物；json 传 id=7, name='cat'，断言 200。
#- DELETE https://petstore.swagger.io/v2/pet/7 —— 删除宠物；断言 200。
import requests
# url = 'https://petstore.swagger.io/v2/pet'
# data = {'id': 7, 'name': 'cat'}
# r = requests.put(url, json=data)
# assert r.status_code == 200, f'更新失败，{r.status_code}'
# print(r.json())
#
# url = 'https://petstore.swagger.io/v2/pet/7'
# r = requests.delete(url)
# assert r.status_code == 200,  f'删除失败，{r.status_code}'
# print(r.json())

#   第二段 · 独立小题（20 分钟）
#   写函数 count_by_code(codes)，返回统计每个状态码出现次数的字典（结果应含 200: 3）。
# codes = [200, 404, 500, 200, 403, 500, 200]
# def count_by_code(codes):
#     result = {}
#     for code in codes:
#         result[code] = result.get(code, 0) + 1
#     return result
# print(count_by_code(codes))



'''
一、首次推送（本次已走完）

  1. 新建 .gitignore，写入：
     .idea/
     pycache/
     *.pyc
  2. git init -b main
  3. git config --global user.name "yanghonggui"
  4. git config --global user.email "你的GitHub邮箱"
  5. git add .
  6. git status
  7. git commit -m "W1: Python 基础练习（petstore CRUD + 断言）"
  8. 浏览器建空仓库 python-basics，不勾 README / .gitignore / license
  9. git remote add origin https://github.com/yanghonggui/python-basics.git
  10. git push -u origin main
  11. 刷新仓库页，确认文件在

  二、以后新增内容（日常）

  1. git status
  2. git add .
  3. git commit -m "说明这次改了什么"
  4. git push

  注意

  1. git add 后面的点不能漏
  2. commit 前先 git status，别把 .idea、密码、token 提交进去
  3. 弹登录时 Username 填 yanghonggui，Password 填 PAT
'''

# 26.10.31
# 第一段 · 默写（换数据，3 题）
#   1. 函数收口：codes = [500, 200, 503, 404, 500, 201]，写 count_5xx(codes) 返回 >=500 的个数，外面调用一次并 print。
codes = [500, 200, 503, 404, 500, 201]
def count_500(codes):
    nums = []
    for code in codes:
        if code >= 500:
            nums.append(code)
    return nums

codes = count_500(codes)
print(len(codes))

#   2. 类：class OrderAPI，__init__(self, base_url) 存属性；get_orders(self) 返回 f-string 拼出 base_url + '/orders'。
class OrderAPI:
    def __init__(self,base_url):
        self.base_url = base_url

    def get_orders(self):
        return f'这个地址是：{self.base_url}/orders'


API  =OrderAPI('https:/www.baidu.com')
print(API.get_orders())


#  3. 接口：PUT https://petstore.swagger.io/v2/pet —— 更新宠物；json 传 id=9、name='rabbit'，断言状态码 200。
url = 'https://petstore.swagger.io/v2/pet'
data ={'id': 9, "name": "rabbit"}
response = requests.put(url, json=data)
assert response.status_code == 200
print(response.status_code)
print(response.json())


#  第二段 · 独立小题（上次留的）
pets = [
      {'name': 'dog',  'price': 120},
      {'name': 'cat',  'price': 80},
      {'name': 'bird', 'price': 200}
  ]
#   写 expensive_names(pets, limit)，返回价格 > limit 的名字列表，两条 assert 自测：
#   - limit=100 → ['dog', 'bird']
#   - limit=150 → ['bird']

def expensive_names(pets, limit):
    li = []
    for pet in pets:
        if pet['price'] > limit:
            li.append(pet['name'])
    return li

assert expensive_names(pets, 100) == ['dog', 'bird']
assert expensive_names(pets, 150) == ['bird']
print('通过')


