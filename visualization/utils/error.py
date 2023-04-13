# 定义一个映射
error = {}
# 成功的状态
error[200] = 'success'
# 失败的状态
error[500] = 'faile'
# 用户
error[1001] = '用户不存在'
error[1002] = '用户密码出错'
error[1003] = '用户已存在'
# 展示
error[2001] = '电影不存在'

# 获取错误状态
def getMsg(code:int)->str:
    return error[code]
