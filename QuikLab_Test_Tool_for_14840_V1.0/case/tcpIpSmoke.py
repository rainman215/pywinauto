#! /usr/bin/env python
#coding=GB18030
import os
import casebase.case_wrapper as case
import unittest
from casebase.checkName import check
import casebase.TCP_Component as tcp
import casebase.init as init
import casebase.QuikLab_Install as install
import socket
configList = case.readIniConfig('QuikLab3.0')
ip=[]
host=socket.gethostname()
ip=socket.gethostbyname(host).split('.')
print ip

class Test(unittest.TestCase):
    def setUp(self):
        init._init()
        install._checkInstall()
        flag='tag.txt'
        with open(flag,'r') as f:
            for i in f:
                if i == '0':
                    exit()
        case.confDataBase(configList[1],configList[2],ip)
        case.login(configList[1],configList[2],configList[3],configList[4])


    def tearDown(self):
        os.system('taskkill /IM MainApp.exe /F')

    def testName(self):
        window_name =configList[0]
        getName=check()
        proName=getName.getProName(configList[5])
        case.creat_pro(window_name,proName)
        case.unload_pro(window_name)
        case.load_pro(window_name, proName)
        case.add_Bus(window_name)
        case.add_dev(window_name)
        case.add_tar(window_name,ip)
        tcp.add_TCP_Client_Interface(window_name)
        tcp.add_TCP_Service_Interface(window_name)
        tcp.add_TCP_Signal(window_name)
        tcp.add_TCP_Case(window_name)
        tcp.run_case(window_name)
        tcp.compareRes()
    
if __name__ == "__main__":
    unittest.main()