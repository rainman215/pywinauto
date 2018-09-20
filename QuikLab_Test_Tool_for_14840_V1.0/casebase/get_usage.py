#! /usr/bin/env python
#coding=GB18030
import psutil
import os
import time
from casebase import getProcessID
import win32com.client
from pywinauto import application
import threading
#-----------------�жϽ����Ƿ����-------------------------
def check_exist(pro_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_process where Name="%s"'%pro_name)
    if len(processCodeCov) > 0:
        return 1
    else:
        print "%s is not exist"%pro_name
        return 0
    
#-----------------��ý���ID-------------------------
def get_PID():
    _list=getProcessID.process_get_modules()
    for i in range(len(_list)):
        if "MainApp" in _list[i][1]:
            PID=_list[i][0]
            return PID

#-----------------���CPU��MEMռ����-----------------------
def get_usage():
    app=application.Application(backend='uia')
    flag=0
#     print os.getcwd()
    time.sleep(15)
    with open('../appFile.txt','r') as f:
        for line in f:
            fileName=line.replace('exe','tmp')
#             print fileName
    while check_exist(fileName):
        time.sleep(2)
    with open('tag.txt','r') as f:
        for i in f:
            if i == '0':
                print i
#                 os._exit(0)
                exit()
    window_name = r'QuiKLab V3.0'
#-------------�ж�QuikLab3.0�Ƿ񵯳�������ִ��case���߳��Ƿ���ִ��------------------
    while flag == 0:
        mark=0
        try:
            for i in threading.enumerate():
                if 'Thread-1' in str(i):
                    mark=1
            if mark == 0:
                print "Quiklab exception!"
                os._exit(0)
            app.connect(title = window_name) 
            flag=1
        except:
            time.sleep(2)
            flag=0
    if os.path.exists('./CPUresult.txt'):
        os.remove('./CPUresult.txt')
        os.remove('./MEMresult.txt')
    PID=get_PID()
    if PID is None:
        print "QuikLab didn't start!"
        exit()
    c=[]
    m=[]
    try:
        def get_cpu_info():
            i = 0
            print "getting Usage... "
            while True:
                if check_exist('MainApp.exe')==0:
                    break
                i = i + 1
                cpucount = psutil.cpu_count(logical=True)   #CPU�˵ĸ���
                process = psutil.Process(int(PID))  #����PID���ӽ���
                cpupercent = process.cpu_percent(interval=1)
                cpu = int(cpupercent / cpucount)
                mem = process.memory_percent()
                now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                c.append(cpu)
                m.append(mem)
                Cpu_text = open('./CPUresult.txt', 'a')
                Mem_text = open('./MEMresult.txt', 'a')
                if cpu <= 50:
#                     print u'CPU usage is %s' % cpu + '         ' + now
#                     print u'MEM usage is %s' % mem + '         ' + now
                    print>> Cpu_text, 'CPUʹ����:%s%%' % cpu + '    ' + now
                    print>> Mem_text, 'MEMʹ����:%s%%' % mem + '    ' + now
                    Cpu_text.close()
                    Mem_text.close()
                else:
                    print 'CPUʹ����:%s%%,ռ���ʹ���' % cpu + '    ' + now
                    print 'MEMʹ����:%s%%' % mem + '    ' + now
                    print>> Cpu_text, 'CPUʹ����%s%%,ռ���ʹ���' % cpu + '    ' + now
                    print>> Mem_text, 'MEMʹ����:%s%%,ռ���ʹ���' % mem + '   ' + now
                    Cpu_text.close()
                    Mem_text.close()
#         print 'Result will be in result.txt'
        time.sleep(1)
        print "-------------------------------------------------"
        get_cpu_info()
    except:
        pass
    finally:
        if max(c) > 50:
            with open('./CPUresult.txt','a') as f:
                print "CPUռ�ù��ߣ�Performance Test Fail"
                f.write("CPUռ�ù��ߣ�Performance Test Fail")
        else:
            with open('./CPUresult.txt','a') as f:
                print "Performance Test Pass"
                f.write('Performance Test Pass')
        print  u'����%s' % PID + u'�Ѿ�����'
if __name__=='__main__':
    get_usage()