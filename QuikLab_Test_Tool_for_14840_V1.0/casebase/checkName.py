#! /usr/bin/env python
#coding=GB18030
import re
import pymysql
class check(object):
    def __init__(self):
        self.db = pymysql.connect(host = '192.168.1.226',port = 3306,user = 'root',passwd = 'root',db = 'mydb',charset = 'utf8')
    
    def ckUname(self,uName):
        cur = self.db.cursor()
        cur.execute('SELECT Name FROM mydb.tbl_user;')
        data = cur.fetchall()
        for i in range(0,len(data)):
#             print data
            if uName == data[i][0]:
                print "find user"
                cur.close()
                return(1)
        cur.close()
        print "No user"
        return (0)        
    
    def ckProName(self,proName):
        if proName.strip() == '':
            print "No Project Name!"
            return (0)
        else:
            return (1)
    
    def getProName(self,proName):
        cur = self.db.cursor()
        cur.execute('SELECT Name FROM mydb.tbl_project;')
        data = cur.fetchall()
        for i in range(0,len(data)):
            if proName == data[i][0]:
                flag=proName[-1]
                if re.match('\d', flag):
                    flag=int(flag)+1
                    proName=proName[0:-1]+str(flag)
                else:
                    proName=proName+str(1)
                self.getProName(proName)
        cur.close()
        return proName
if __name__=='__main__':
    p=check()
    print p.getProName('1')