import os
import platform
import datetime
import pymysql
import jieba

def versionshow():
    printlog("Current OS name is %s" % os.name)
    printlog("Current “python” version info is %s" % platform.python_version())
    printlog("Current “re” version info is %s" % platform.re.__version__)
    printlog("Current “pymysql3” version info is %s" % pymysql.__version__)
    printlog("Current “jieba” version info is %s" % jieba.__version__)

if __name__ == '__main__':
    try:
        print("====HelloWorld!==========")
        print("====Readdy?==========")#Let's go!
        starttime = datetime.datetime.now()
        versionshow()
        print("====Readdy!==========")
        endtime = datetime.datetime.now()
        printlog("==TimeCosts: " + str((endtime - starttime).seconds) + "Seconds")
        print("====The End.==========")
    except Exception as e:
        printlog('--任务执行失败！！！Error:%s' % str(e))
    finally:
        print("====MyGod!==========")
