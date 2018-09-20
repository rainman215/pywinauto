#! /usr/bin/env python
#coding=GB18030
import time
import os

#-------------��ȡ��ǰִ�к������Ʋ��ж�ִ���Ƿ�����-------------
def _getName(func):
    def wrapper(*args):
        path='../report'
        if not os.path.exists(path):
            os.chdir('report')
        _file='../report/log.txt'
        with open(_file,'a') as f:
            t=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))
            f.write('%s '%t)
            f.write(func.__name__)
            f.write(' ')
            print func.__name__
        func(*args)
        with open(_file,'a') as f:
            f.write('pass')
            f.write('\n')
    return wrapper

if __name__=='__main__':
    pass