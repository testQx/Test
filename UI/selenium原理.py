# 初始化了一个service对象，然后调用了start()方法
# ->启动了chromedriver.exeChrome浏览器的驱动程序(去寻找系统环境变量的浏览器驱动)
# ->端口号为9515的进程->继续调用父类RemoteWebDriver 的初始化方法
# ->self.start_session(capabilities, browser_profile) 向地址localhost:9515/session发送了一个post请求，新建一个seesionid，打开浏览器
# ->操作浏览器，通过请求url中含有$sessionid变量关联在一起
# ->程序告诉RemoteWebDriver打开一个浏览器(发送post请求，带上请求参数)，然后再向remote server发送执行浏览器动作的请求



# selenium原理：
# 1.selenium client(python等语言编写的自动化测试脚本)初始化一个service服务，通过Webdriver启动浏览器驱动程序chromedriver.exe
#
# 2.通过RemoteWebDriver向浏览器驱动程序发送HTTP请求，浏览器驱动程序解析请求，打开浏览器，并获得sessionid，如果再次对浏览器操作需携带此id
#
# 3.打开浏览器，绑定特定的端口，把启动后的浏览器作为webdriver的remote server
#
# 3.打开浏览器后，所有的selenium的操作(访问地址，查找元素等)均通过RemoteConnection链接到remote server，
# 然后使用execute方法调用_request方法通过urlib3向remote server发送请求
#
# 4.浏览器通过请求的内容执行对应动作
#
# 5.浏览器再把执行的动作结果通过浏览器驱动程序返回给测试脚本