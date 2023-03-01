dirPath = "D:\\githubProject\\Graduation-Project\\comment\\"
def saveComment(name:str,content:str)->str:
    filePath = dirPath + name + '.txt'
    #打开文件
    with open(filePath,'w',encoding='utf-8') as f:
        f.write(content)
    return filePath