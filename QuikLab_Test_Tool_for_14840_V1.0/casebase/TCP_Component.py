#! /usr/bin/env python
#coding=GB18030
from pywinauto import mouse as ms
import casebase.case_wrapper as case
import getpass
import auto_lib as pywin 
import time
import locFun as location
import pyautogui as py
import SendKeys
import os
app=pywin.Pywin()

#��ӿͻ��˽ӿ�
def get_pos(pos,x_dis,y_dis):
    window_name=r'QuiKLab V3.0'
    app.click(window_name,pos)
#     print py.position()
    x1=py.position()[0]
    y1=py.position()[1]
    checkbox_x=x1+x_dis
    checkbox_y=y1+y_dis
#     py.moveTo(checkbox_x, checkbox_y)
    py.click(checkbox_x,checkbox_y)
    
@location._getName
def add_TCP_Client_Interface(window_name):
    app.connect(window_name)
    app._wait_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)
#���IP
    app.click(window_name, 'Edit11')
    app.Sendk('RIGHT', 1)
    time.sleep(1)
    app.input(window_name, 'Edit11', '19')
    app.Sendk('2', 1)
    app.input(window_name, 'Edit12', '16')
    app.Sendk('8', 1)
    app.input(window_name, 'Edit13', '1')
    app.Sendk('.', 1)
    app.input(window_name, 'Edit14', '5')

#���ö˿�
    app.click(window_name, 'Edit9')
    app.input(window_name, 'Edit9', '^a')
    app.input(window_name, 'Edit9', '6060')
    app.click(window_name, u'ȷ��')   #ȷ��
    app._wait_not_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    
#��ӷ���˽ӿ�
@location._getName
def add_TCP_Service_Interface(window_name):
    ms.right_click(coords=(923,510))
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app._wait_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app.click(window_name, u'ȷ��')   #ȷ��
    app._wait_not_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    
#����ź�
@location._getName
def add_TCP_Signal(window_name):
    ms.press(button='left', coords=(902, 456))
    ms.move(coords=(940, 456))
    ms.release(button='left', coords=(940, 456))
    app._wait_child(window_name, u'�༭__�ź�__signal', 'ready', 10, 2)
    app.click(window_name, 'ComboBox5')
    time.sleep(1)
    app.input(window_name, 'ComboBox5', 'i_block')  #������ݽṹ
    app.click(window_name, u'ȷ��')   #ȷ��
    app._wait_not_child(window_name, u'�༭__�ź�__signal', 'ready', 10, 2)

#�½���������
@location._getName
def add_TCP_Case(window_name):
    app.click(window_name, 'TreeItem11')
#     app.click(window_name, 'TreeItem6') #14421
    app._wait_child(window_name, u'����������', 'ready', 10, 2)
    app.right_click(window_name, 'TreeView2')
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'�½���������', 'ready', 10, 2)
    app.click(window_name, u'ȷ��')
#     app._wait_not_child(window_name, u'�½���������', 'ready', 10, 2)
    app._wait_child(window_name, u'��������', 'ready', 10, 2)
    app.right_click(window_name,u'��������')    #��������root
    time.sleep(1)
    app.Sendk('DOWN',3)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'�½���������', 'ready', 10, 2)
#     app.Sendk('TAB',2)
    app.input(window_name, 'Edit1', 'content2')     #����������
    app.click(window_name,u'ȷ��')
    app.click(window_name,u'��������')
    app.Sendk('RIGHT',1)
    app.Sendk('DOWN',1)
    app._wait_child(window_name, 'content2', 'ready', 10, 2)
     
 
#����ź�
    app.click(window_name, u'������������')
    app.click(window_name, u'����źű���')
    app._wait_child(window_name, u'ѡ���źŶԻ���', 'ready', 10, 2)
    get_pos('signal',-90,0)
#     ms.click(coords=(602,450))      #ѡ���ź�
    app.click(window_name, u'ȷ��')
    app._wait_child(window_name, 'signal', 'ready', 10, 2)
# 
# 
# #���������༭    
#--------------------�����ź�����-------------------------------
    app.click(window_name, u'���������༭')
    app.right_click(window_name, 'TreeItem18')      #�Ҽ�"������"
#     app.right_click(window_name, 'TreeItem12') #14421
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)   #��������
    app._wait_child(window_name, u'ɾ��', 'ready', 10, 2)
    app.click(window_name, 'ComboBox0')
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)
    app.click(window_name, 'Edit1')
    SendKeys.SendKeys("^a")
    app.input(window_name, 'Edit1', 10)
    app.click(window_name, 'Signal')
    get_pos(u'������',-30,35)
    app.click(window_name, u'ȷ��')

#--------------------�޸��źŸ�ֵ-------------------------------
    app.click(window_name,'TreeItem18')
#     app.right_click(window_name, 'TreeItem12') #14421
    app.Sendk('DOWN', 2)
    get_pos('TreeItem18', 0, 40)
#     get_pos('TreeItem12', 0, 40) #14421
    py.doubleClick()
    get_pos(u'����ֵ�ı���', 0, 30)
    py.rightClick()
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app.click(window_name, u'ȷ��')
    get_pos(u'���ʽ', 0, 30)
    py.doubleClick()
    time.sleep(1)
    SendKeys.SendKeys("^a")
    SendKeys.SendKeys("15")
    app.click(window_name, u'�Զ����ö�������')
    app.click(window_name, u'ȷ��')

#--------------------�����ź�-------------------------------
    app.right_click(window_name,u'ѭ��[10000��]')
    app.Sendk('DOWN', 1)
    app.Sendk('RIGHT', 1)
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)
    get_pos('signal', -85, 0)
    app.click(window_name, u'�Զ����ö�������')
    app.click(window_name, u'ȷ��')

#--------------------�Ƚ�����ֵ-------------------------------
    app.right_click(window_name,u'ѭ��[10000��]')
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)
    app._wait_child(window_name, u'ɾ��', 'ready', 10, 2)
    app.click(window_name, 'ComboBox0')
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app.click(window_name, 'signal')
    get_pos(u'������',-30,35)
    app.click(window_name, 'Edit0')
    app.input(window_name, 'Edit0', 15)
    app.click(window_name, u'ȷ��')
    
#     ms.press(button='left',coords=(600,229))
#     ms.move(coords=(661, 646))
#     ms.release(button='left', coords=(661, 646))
#     app.click(window_name, u'ȷ��')
#     app._wait_child(window_name, u'����[signal]', 'ready', 10, 2)

#------------------��������--------------------------
@location._getName
def run_case(window_name):
    app.click(window_name,u'��ʼ')
    app._wait_child(window_name, u'��ʼ�²���', 'ready', 10, 2)
    app.click(window_name, 'content2*')
    app.click(window_name, 'ComboBox4')
    time.sleep(1)
    app.Sendk('UP', 2)
    app.Sendk('ENTER', 1)    
    app.click(window_name, u'��ʼ')
    time.sleep(2)
    app.click(window_name, u'��')
#     app._wait_child(window_name, u'����', 'ready', 10, 2)
    time.sleep(10)
    app._wait_not_child(window_name, u'����', 'ready', 10, 2)
    time.sleep(2)
    app.click(window_name,u'��������')
    time.sleep(2)
    app.click(window_name, u'����ģʽ')
#     times=-2
    while True:
        try:
            app._wait_child_nor(window_name, u'��һ��', 'enabled', 10, 1)
            app.click(window_name, u'��һ��')
        except:
            break
#         time.sleep(0.5)

#------------------�ȶԵ��Խ��--------------------------
@location._getName
def compareRes():
    username = getpass.getuser()
    filePath='C:\Users\%s\QuiKLab3\\runtime\\'%username
#     os.chdir(filePath)
    fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'
    logFile=filePath+fileName
    print logFile
    case.isNotIn('��',logFile, True,'���Գɹ�')
    os.chdir('../report')
    despath=os.getcwd()
    os.system('copy %s %s'%(logFile,despath))

    
if __name__=='__main__':
    pass
    app=pywin.Pywin()
    window_name =u'QuiKLab V3.0'
#     time.sleep(2)
#     app.connect(window_name)
#     add_TCP_Client_Interface(window_name)
#     add_TCP_Service_Interface(window_name)
#     add_TCP_Signal(window_name)
    add_TCP_Case(window_name)
#     run_case(window_name)
#     compareRes()