# UI_AUTOTEST_SHI 自动化ui测试框架
开发环境
python3.7 
selenum4.1.2   
ddt1.4.4    
unittest   
from package.HwTestReport_local import HTMLTestReport 
该测试报告无法将并发测试报告集合到一个HTML中,但是比最原始的 HTMLTestReport 好看很多，没有并发需求可自行修改run_main.py文件
为了解决并发执行用例生成多个测试报告的痛点所以引入了
unittestreport
可并发执行测试用例,并且可以将测试报告集成在一个HTML报告中，三种模板风格可选择...


