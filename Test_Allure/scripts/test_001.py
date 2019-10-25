# coding:utf-8
import pytest,allure
class Test_Abc:
    @pytest.mark.parametrize("a",[1,2,3])
    @allure.step(title="第一个测试用例")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_001(slef,a):
        allure.attach("这是一个描述","测试描述")
        assert a == 2

    @pytest.mark.parametrize("a", [8,9,4])
    @allure.step(title="第二个测试用例")#写标题
    @allure.severity(allure.severity_level.TRIVIAL)#设置严重级别
    @allure.testcase("https://baidu.com/test_001")#测试用例的描述链接
    @allure.issue("https://qq.com/test")#BUG地址的链接
    def test_002(slef, a):
        allure.attach("这是一个描述 %s" %a, "测试描述")#描述
        assert a/2 == 2
if __name__ == '__main__':
    pytest.main(["--alluredir report test_001.py"])