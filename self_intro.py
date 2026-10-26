name = '杨洪桂'
years = 9
goal = '成为一名自动化测试工程师'

print(f'大家好，我的名字叫{name}，做了{years}年测试了，目标是{goal}。明年就是{years+1}年测试了！')

import  json
print(len(json.load(open('cases.json',encoding='utf-8'))))