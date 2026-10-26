import json

'''1、导入用例'''
def load_cases(path):
    try:
        with open(path, encoding='utf-8') as f:
            cases = json.load(f)
            return cases
    except FileNotFoundError:
        print(f'找不到文件：{path}')
        return []
    except json.decoder.JSONDecodeError:
        print(f'json格式错误，请检查{path}')
        return []

'''2、取case中不同filed下的数量，如status'''
def count_by_status(cases, field):
    count = {}
    for case in cases:
        key = case[field]         #循环取值：pass / fail / block 把这几个类型的状态赋值给key
        count[key] = count.get(key, 0) + 1         #count 里有记录就 +1，没记录过按 0 算（0+1 就是第一次）,count["pass"] = count.get("pass", 0) + 1   # 第1轮
                                                          #count["fail"] = count.get("fail", 0) + 1   # 第2轮
    return count

'''3、执行通过率'''
def pass_rate(cases):
    status = count_by_status(cases, 'status')
    passed = status.get('pass', 0)
    failed = status.get('fail', 0)
    executed = passed + failed
    return passed/executed * 100


def count_p0(cases):
    '''4、P0用例数量'''
    count = 0
    for case in cases:
        if case['priority'] == 'P0':
            count += 1
    return count

cases = load_cases('cases.json')
if  not cases:
    raise SystemExit('没有可用用例，请检查用例文件')

rate = pass_rate(cases)
executed_result = count_by_status(cases,'status')
count = count_p0(cases)

print(f'用例执行结果是：{executed_result}')
print(f'用例执行通过率为：{rate:.1f}%')
print(f'P0用例数为：{count}')

