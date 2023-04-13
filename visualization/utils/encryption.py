# 加密模块
import hashlib #导入加密需要的hashlib模块
def encryption(string:str)->str:
    #1.获得md5对象
    obj = hashlib.md5(b'md5secert')  #加盐 ，由于md5是不可逆的加密，但是有些时候，会发生撞库的情况，所以我们可以加盐，有效防止这种情况
    #2.对目标进行加密，必须转化成字节
    obj.update(string.encode("utf-8"))
    #3.获取加密后的结果
    return obj.hexdigest()