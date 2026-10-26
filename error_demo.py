import requests

# r = requests.get('https://httpbin.org/get',
# params = {'q': 'test'},
# headers = {'X-Demo': 'w1d5'},
# timeout = 5)
#
# print(r.status_code)
# print(r.url)
# print(r.json()['args'])
# print(r.json()['headers']['X-Demo'])


# url = 'https://httpbin.org/post'
# params = {'pet_id': 1, 'name': 'doudou'}
# headers = {'X-Demo': 'w1d5'}
# timeout = 5
#
# re = requests.post(url, json=params, headers=headers, timeout=timeout)
# print(re.status_code)
# print(re.text)

# url = 'https://httpbin.org/delay/3'
# try:
#     re = requests.get(url, timeout=1)
#     print(re.status_code)
#
# except requests.exceptions.Timeout:
#     print(f'请求超时')

# url = 'https://httpbin.org/status/404'
# print(requests.get(url).status_code)
#
# url  = 'https://httpbin.org/status/500'
# print(requests.get(url).status_code)
# #
# url = 'https://httpbin.org/post'
# data = {'pet_id': 1}
# print(requests.post(url, data=data).status_code)
# print(requests.post(url, data=data).json()['form'])
# #
# url = 'https://httpbin.org/get'
# params = {'page': 2,'size':10}
# print(requests.get(url,params=params).json()['args'])
#
# url = 'https://httpbin.org/delay/1'
# r = requests.get(url,timeout=2)
# print(r.status_code)


url = 'https://httpbin.org/redirect/2'
# re = requests.get(url)
# print(re.status_code)
# print(re.url)

re = requests.get(url, allow_redirects=False)
print(re.status_code)
print(re.headers['Location'])

url = 'https://httpbin.org/basic-auth/user/pass'
re = requests.get(url, allow_redirects=True)
print(re.status_code)

url = 'https://jsonplaceholder.typicode.com/posts/1'
re = requests.get(url)
print(re.status_code,re.url)
print(re.json()['title'])