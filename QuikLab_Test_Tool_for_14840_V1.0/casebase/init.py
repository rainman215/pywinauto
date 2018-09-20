#! /usr/bin/env python
#coding=GB18030
import os
from checkName import check
import case_wrapper
import getpass
import time
def _init():
#�����־�ļ��Ƿ����
    path='../report'
    if not os.path.exists(path):
        os.chdir('report')
    files=os.listdir(path)
    for i in files:
        d_path=os.path.join(path,i)
#         print d_path
        log='../report/log.txt'
        if os.path.exists(log):
            os.remove(log)
    username = getpass.getuser()
    filePath='C:\Users\%s\QuiKLab3\\runtime\\'%username
    fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'
    fileRes=filePath+fileName
    if os.path.exists(fileRes):
        os.remove(fileRes)
 
#����û����͹������Ƿ����
    tpList=case_wrapper.readIniConfig('QuikLab3.0')
    ck=check()
    if ck.ckUname(tpList[3]) == 1 and ck.ckProName(tpList[5]) == 1:
        pass
    else:
        exit()
    print "Init finish!"
if __name__=='__main__':
    _init()


