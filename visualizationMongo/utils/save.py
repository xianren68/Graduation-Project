import os
dir_url = os.path.dirname(os.path.abspath(__file__))
dir_url = os.path.dirname(dir_url)
base_url = dir_url + "\\static"+"\\avatar\\"
# 存储图片
def saveProfile(fileName,file):
    with open(base_url+fileName,"wb") as f:
        f.write(file)

# 判断图片是否存在
def isExists(fileName):
    if os.path.exists(base_url+fileName) :
        return True
    else:
        return False