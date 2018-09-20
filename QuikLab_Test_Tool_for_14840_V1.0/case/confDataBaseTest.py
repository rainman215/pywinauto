#! /usr/bin/env python
#coding=GB18030
import getpass
import logging
import os
import socket
import unittest

import casebase.case_wrapper as case


configList = case.readIniConfig('QuikLab3.0')
pyfilename = os.path.basename(__file__)

ip=[]
host=socket.gethostname()
ip=socket.gethostbyname(host).split('.')


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def testConfDataBase(self):
        case.confDataBase(configList[1],configList[2],ip)
        username = getpass.getuser()
        xmlList = case.readXml('C:\Users\%s\QuiKLab3\config.xml'%username, 'hostname')
        case.isNotEqual('192.168.1.227', xmlList, "aaa","192.168.1.227����xml�ļ���")
            
    def tearDown(self):
        pass
#         case.closeLogin(u'��¼--�����Զ����Թ���ϵͳ', u"�˳�")        
        
        
if __name__ == "__main__":
#     pass
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
