import pytest


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    print('------------------------------------')

    # 获取钩子方法的调用结果
    out = yield
    print('用例执行结果', out)

    # 3. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    if report.when == "call":
        print('测试报告：%s' % report)
        print('步骤：%s' % report.when)
        print('nodeid：%s' % report.nodeid)
        print('description:%s' % str(item.function.__doc__))
        print(('运行结果: %s' % report.outcome))

