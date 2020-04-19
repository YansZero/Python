# 定義讀取txt

class FileTxt:
    #初始化涵式:
    def __init__(self,name):
        self.name = name
        self.File = None #開始檔案前是None

    #定義方法:
    def Open(self):
        self.File=open(self.name, mode="r",encoding="utf-8")
    def ReadData(self):
        return self.File.read()