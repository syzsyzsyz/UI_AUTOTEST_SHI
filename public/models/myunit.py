#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from  .driver import browser
import unittest

class MyTest(unittest.TestCase):
    """
    自定义MyTest类
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):

        cls.driver.close()