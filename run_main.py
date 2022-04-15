#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time
#原版报告风格
from package.HTMLTestRunner import HTMLTestRunner
#一个大佬写的更好看的报告
from package.HwTestReport_local import HTMLTestReport
from public.models.newReport import new_report
# from tomorrow import threads
#多线程组合报告
import unittestreport
# from BeautifulReport import BeautifulReport
# from public.models.sendmail import send_mail

# 测试报告存放文件夹，如不存在，则自动创建一个report目录
if not os.path.exists(setting.TEST_REPORT):os.makedirs(setting.TEST_REPORT + '/' + "screenshot")

def add_case(test_path=setting.TEST_DIR):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*_sta.py')

    return discover


# @threads(2)
def run_case(all_case,result_path = setting.TEST_REPORT + '/'):
    #不需要将并发用例放在一个html中可使用该方法
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = result_path + now + 'result.html'
    # fp = open(filename, 'wb')

    """执行所有的测试用例"""
    #旧版风格报告
    # runner = HTMLTestRunner(stream=fp,title='小京东自动化测试报告',
    #                         description='环境：windows 11 浏览器：chrome',
    #                         tester='shiyingzhi')
    #新版风格报告
    # runner = HTMLTestReport(stream=fp,
    #                             verbosity=2,
    #                             images=True,
    #                             title='小京东自动化测试报告',
    #                             description='环境：windows 11 浏览器：chrome',
    #                             tester='shiyingzhi')
    #并发执行报告
    runner = unittestreport.TestRunner(suite=all_case,
                                       tester = 'shiyingzhi',
                                       filename = filename,
                                       report_dir = result_path,
                                       title = '小京东自动化测试报告',
                                       desc = '登录模块测试',
                                       templates = 2
    )
    runner.run(thread_count=2)
    # runner.run(all_case)
    # fp.close()
    report = new_report(setting.TEST_REPORT) #调用模块生成最新的报告
    # send_mail(report) #调用发送邮件模块

if __name__ =="__main__":
    cases = add_case()
    run_case(cases)
    # for i,j in zip(cases,range(len(list(cases)))):
    #     run_case(i,j)