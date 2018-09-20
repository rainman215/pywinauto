#! /usr/bin/env python
#coding=GB18030
import ConfigParser
import logging
import os
import time
import xml.dom.minidom

from pywinauto import mouse as ms

import auto_lib as pywin 
import locFun as location
import exception as exp


app=pywin.Pywin()

@location._getName
def login(tl_dir,tl_name,uName,key):
    app.start(tl_dir,tl_name)
    window_name =u'��¼--�����Զ����Թ���ϵͳ'
    app._wait_child(window_name, u'�� ½', 'exists', 10, 2)
    app.connect(window_name)
#�����û���������
    app.input(window_name, 'Combox', uName)
    app.click(window_name, 'Edit1')
    app.input(window_name,'Edit1', key)
    app.click(window_name, u'�� ½')
#�ж�QuikLab3.0�Ƿ񵯳�    
    window_name =u'QuiKLab V3.0'
    app._wait(window_name,'active',10, 2)
    app.connect(window_name)
#     else:
#         print "try again!"
#         app.connect(window_name)

#�½���Ŀ
@location._getName 
def creat_pro(window_name,pro_name):
    app.click(window_name,u'�½���Ŀ')
    app._wait_child(window_name, u'����', 'active', 10, 2)
    app.click(window_name, 'Edit2')
    app.input(window_name, 'Edit2', '^a')
    app.input(window_name,'Edit2',pro_name)
    app.click(window_name,u'ȷ��') #ȷ��

#������Ŀ
@location._getName 
def load_pro(window_name,pro_name):
    app.click(window_name,u'������Ŀ')
    app.click(window_name, 'Edit1')
    app.input(window_name,'Edit1',pro_name)
    app.click(window_name, u'��������')
    app.click(window_name,u'ȷ��')
    time.sleep(2)
    
#�ж���Ŀ�Ƿ���سɹ�
    if pro_name in app.texts(window_name, 'statics2'):
        pass
    else:
        print "pro failed to load!!!"
        exit()
        
#--------------------ɾ����Ŀ--------------------------
def  delete_pro(window_name,pro_name):
    app.click(window_name,u'������Ŀ')
    app.click(window_name, 'Edit1')
    app.input(window_name,'Edit1',pro_name)
    ownerInfo = app.texts(window_name, "DataItem3")
    if ownerInfo != '':
        app.right_click(window_name, u'��������')
        app.Sendk("UP", 1)
        app.Sendk("ENTER", 1)
        app.click(window_name, u"ȷ��")
    app.right_click(window_name, u'��������')
    app.Sendk("DOWN", 2)
    app.Sendk("ENTER", 1)
    app.click(window_name, u"ȷ��")
    app.click(window_name, u"ȷ��")

#ж����Ŀ
@location._getName         
def unload_pro(window_name):
    app.click(window_name,u'ж����Ŀ')
    time.sleep(1)
    app.click(window_name,u'��')
    if len(app.texts(window_name, 'statics2')) != 0:
        print 'unload failed!!!'
        exit()

#�������
@location._getName
def add_Bus(window_name):
    app.click(window_name,u'��������') #���뻷������ 
    ms.right_click(coords=(1577, 492))
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
#�жϵ���"�������"���� 
    app._wait_child(window_name, u'�������', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.input(window_name, 'ComboBox1', 'tcp')#��� TCP/IPЭ��
    app.Sendk('ENTER',1)
    app.click(window_name, u'ȷ��') #ȷ��

#����豸  
@location._getName
def add_dev(window_name):
    app.right_click(window_name,'Pane2')
    app.Sendk('DOWN', 3)
    app.Sendk('ENTER',1) #ѡ������豸
    app._wait_child(window_name, u'����豸', 'ready', 10, 2)

#���Ŀ���
@location._getName
def add_tar(window_name,ip):
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)

#���IP
    app.click(window_name, 'Edit2')
    app.Sendk('RIGHT', 1)
    time.sleep(1)
    app.input(window_name, 'Edit2', '19')
    app.Sendk('2', 1)
    app.input(window_name, 'Edit3', '16')
    app.Sendk('8', 1)
    app.input(window_name, 'Edit4', '1')
    app.Sendk('.', 1)
    app.input(window_name, 'Edit5', ip[3])
    app.click(window_name, u'ȷ��')#ȷ��
    

@location._getName
def close(window_name,contorl):
    app.click(window_name,contorl)
    app.click(window_name,u"ȷ��")
    
def closeLogin(window_name,contorl):
    app.click(window_name,contorl)
    
#�����������ݿ������Ϣ
@location._getName
@exp._exception
def confDataBase(tl_dir,tl_name,ip):
    app.start(tl_dir,tl_name)
    time.sleep(3)
    window_name =u'��¼--�����Զ����Թ���ϵͳ'
    app.connect(window_name)
    app.click(window_name, u"����")     #������ð�ť
    app.click(window_name, u"���ݿ�")    #������ݿ�
#     time.sleep(2)
    app.click(window_name, 'Edit3')        #ѡ��IP��ַ�����ĵ�һλ����
    app.input(window_name, 'Edit3', '^a')  #ȫѡ�����ĵ�һλ����
    app.input(window_name, 'Edit3', '19')  #����IP��ַ�еĵ�һλ����
    app.Sendk('2', 1)
    app.click(window_name, 'Edit4')
    app.input(window_name, 'Edit4', '^a')
    app.input(window_name, 'Edit4', '16')
    app.Sendk('8', 1)
    app.click(window_name, 'Edit5')
    app.input(window_name, 'Edit5', '^a')
    app.input(window_name, 'Edit5', '1')
    app.click(window_name, 'Edit6')
    app.input(window_name, 'Edit6', '^a')
    app.input(window_name, 'Edit6', 226)
    app.Sendk('6', 1)
    app.click(window_name, u"Ӧ��")    #���Ӧ�ð�ť
    app.click(window_name, u"ȷ��")    #���ȷ����ť
    app.click(window_name, u"ȷ��")
    app.click(window_name, u'�˳�')    #����˳�
    
#----------------------------------------���Թ�������---------------------------------------------------
# �ж�Ԥ�ڽ����ʵ�ʽ���Ƿ����
@exp._exception 
def isNotEqual(expectResult,acutalResult,pyfilename,message):
    if expectResult != acutalResult:
        assert expectResult == acutalResult

# �ж�Ԥ�ڽ���Ƿ������ʵ�ʽ����
# @exp._exception 
def isNotIN(expectResult,acutalResult,pyfilename,message):
    if expectResult not in  acutalResult:
        logWriter(pyfilename,message);
        assert expectResult in acutalResult
        
#-------------ʵ�ʽ����Ԥ�ڽ���Ƚϣ�flagΪTrue��Ԥ��Ϊͨ������֮��Ԥ�ڲ�ͨ��-------------
#Example: isNotIn('��',logFile, True,'���Գɹ�') logFile����'��'��True����Ϊ�棬���Գɹ�
# @exp._exception        
def isNotIn(expectResult,logFile,flag,Msg):
    with open(logFile,'r') as f:
        actualResult=f.read()
    if expectResult not in actualResult:
        if flag is True:
            pass
        else:
            assert expectResult in actualResult
    
#----------------------------------------�ļ�/���ݿ����-------------------------------------------------
#��ȡ�����ļ�
def readIniConfig(softName):
#     print softName
    readini = ConfigParser.ConfigParser()
    _file = '../data/mainConfig.ini'
    if os.path.exists(_file):
        pass
    else:
        os.chdir('data')     
    readini.read(_file)
    section = readini.sections()
#     print section
    for sectionInfo in section:
        if sectionInfo in softName:
            softWindowName = readini.get(sectionInfo,"softWindowName")
            softSetupdir = readini.get(sectionInfo,"softSetupDir")
            softLabname = readini.get(sectionInfo,"softLabName")
            softUserName = readini.get(sectionInfo,"softUserName")
            softPwd = readini.get(sectionInfo,"softPwd")
            softProjectName = readini.get(sectionInfo,"softProjectName")
        _list=[softWindowName,softSetupdir,softLabname,softUserName,softPwd,softProjectName]
    return _list

#����xml�ļ�
def readXml(xmlFileUrl,elementName):
    elementData = []
    dom = xml.dom.minidom.parse(xmlFileUrl)  #��xml�ĵ�
    root = dom.documentElement   #��ȡ���нڵ����
    print root
    itemlist = root.getElementsByTagName(elementName)   #�ڼ����л�ȡ�ڵ�����ΪelementName�Ľڵ����
    for item in itemlist:
        un = item.firstChild.data
        elementData.append(un)    #��ȡ�Ա�ǩ֮�������
    return elementData

#��¼log�ļ�
def logWriter(pyfilename,message):
    LOG_FORMAT = "%(asctime)s " + str(pyfilename) + " %(message)s"         #����log�ļ����ݸ�ʽ���쳣������ʱ��/py�ļ�/��Ϣ��
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"                                      #�쳣����ʱ��ĸ�ʽ
    fileUrl = os.getcwd() + r'\report\test.log'
    if not os.path.exists(fileUrl):
        os.chdir('../')
        fileUrl=os.getcwd() + r'\report\test.log'
    logging.basicConfig(format = LOG_FORMAT,datefmt= DATE_FORMAT,filename=fileUrl,level = logging.DEBUG)  #ָ��Ҫ��¼��־�ļ�����־��ʽ�����ڸ�ʽ�����λ��
    logging.debug(message)
    logging.shutdown()             #�������Ϣ 
if __name__=='__main__':
    pass
    app=pywin.Pywin()
    tl_dir = r'D:\QuiKLab3.0'
    tl_name = r'D:\QuiKLab3.0\MainApp.exe'   
    login(tl_dir,tl_name,'default','1')
# #     time.sleep(5)
    window_name =u'QuiKLab V3.0'
    app.connect(window_name)
#     time.sleep(5)
#     creat_pro(window_name,'test_name120')
#     unload_pro(window_name)
    load_pro(window_name, 'test_name120')
#     add_Bus(window_name)
#     add_dev(window_name)
#     add_tar(window_name)
#     result=ckname.checkName('cl123')
#     print result
#     if result == 0:
#         print "ProName had exist������"
#         exit()
#     readIniConfig('QuikLab3.0')
#     logWriter()
