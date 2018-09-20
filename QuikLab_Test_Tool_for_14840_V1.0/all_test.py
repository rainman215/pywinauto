#! /usr/bin/env python
#coding=GB18030
import os
import shutil
import threading
import time
import unittest

import allcase
import casebase.HTMLTestRunner as HTMLTestRunner
import casebase.get_usage as cpuUsage


def start():
    testunit = unittest.TestSuite()
    alltestnames = allcase.caseData()
    print alltestnames
    for test in alltestnames:
        testunit.addTest(unittest.makeSuite(test))
    
    now = time.strftime("%Y%m%d%H%M%S",time.localtime())
    filedir =  os.getcwd() + r'\report'
    if not os.path.exists(filedir):
        os.chdir('../')
        filedir=os.getcwd() + r'\report'
    
    file_dir = filedir + r'\result' + now 
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)      #ʱ����Ϊ�ļ����������ļ���
      
    fileUrl = filedir + r'\result' + now +".html" 
    fp = file(fileUrl ,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'QuikLab3.0�Զ������Ա���',description=u'QuikLab3.0�Զ������Ա���')
    runner.run(testunit)
    fp.close()
     
    fileNames = os.listdir(filedir)
    for fileName in fileNames:
        if os.path.isfile(os.path.join(filedir,fileName)):
            if os.path.splitext(fileName)[1] != ".py":
                fp = os.path.join(filedir,fileName)
                shutil.move(fp, file_dir)
                

start() 
 
# threads=[]
# t1 = threading.Thread(target=start)
# threads.append(t1)
# t2 = threading.Thread(target=cpuUsage.get_usage)
# threads.append(t2)
# for t in threads:
# #     print t.getName()
#     t.setDaemon(True)
#     t.start()
# for n in threads:
#     t.join()
