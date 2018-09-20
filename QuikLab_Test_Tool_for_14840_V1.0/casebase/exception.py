#! /usr/bin/env python
#coding=GB18030
from PIL import ImageGrab
import time
import os
def _exception(func):
    def wrapper(*args):
        try:
            func(*args)
        except:
            path='../report'
            if not os.path.exists(path):
                os.chdir('casebase')
            _file='../report/log.txt'
            with open(_file,'a') as f:
                f.write('fail')
                f.write('\n')
            now=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))
            im = ImageGrab.grab()
            lists =[]
            fileNames = os.listdir(path)
            for fileName in fileNames:
                if os.path.isdir(os.path.join(path,fileName)):
                    lists.append(fileName)
                     
            lists.sort(key=lambda fn:os.path.getmtime(path +r"/" + fn))
            file_new = os.path.join(path,lists[-1])
            picFile= file_new + '/' + now+'.png'
            im.save(picFile)
            print "screenshot:" + picFile,len("screenshot:" + picFile)    #���ڲ��Ա��������ӽ�ͼ
            exit()

    return wrapper

if __name__=='__main__':
    pass