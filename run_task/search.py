import os , sys ,math

#查看目录底下文件大小
def lean_file_log(path,limitSize):
    filelist=[]
    for root, dirs,filesname in os.walk(path):
        for i in files:
            listpath=os.path.join(root,i)
            filelist.append(listpath)

    for file in fileList:
        filesize=os.path.getsize(file)/math.pow(1024,3)
        if fileSize >= limitSize:
            os.system("echo '' > {0}".format(file))
            # 字节bytes转化kb\m\g

def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)

import os
class  fileSize():

    def get_FileSize(self ,filePath):
        fsize = os.path.getsize(filePath)
        fsize = fsize / float(1024 * 1024)
        print (fsize)
        return round(fsize)

if __name__ == '__main__':
    size = fileSize().get_FileSize("/home/Python-3.6.8.tar")
    print("文件大小：%.2f MB" % (size))

