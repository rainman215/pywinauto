#! /usr/bin/env python
#coding=utf-8
from case import tcpIpSmoke, confDataBaseTest

def caseData():
#     print "ss"
    alltestsnames = [tcpIpSmoke.Test,
                     confDataBaseTest.Test]
    print "success read case list"
    return alltestsnames

if __name__ == "_main_":
    print caseData()
