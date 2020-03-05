import os
from build_XML import BuildNewXML
class FishDB(BuildNewXML):
    def __init__(self,filename=None):
        super().__init__(filename=None)
        self.path = ''
    def check_path(self):
        try:
            if self.path =='':
                print('请先设置正确的路径名，再执行代码！')
                return
            elif not os.path.isdir(self.path):
                os.makedirs(self.path)
            self.filename = self.path + self.filename
        except:
            print('子文件夹%s建立出错！'%(self.path))
