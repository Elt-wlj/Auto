from appium.webdriver import Remote

# 得到一个driver
# 1.确定手机在线
# 2.启动appium服务
# (默认是启动4444端口),如果启用4444就可以直接访问.因为Remote,设置了默认的参数
# 3.Remote提供的参数端口号和appium的服务端口号保持一致

# 4.平台名称、明确连接那个手机、操作那个app

# 三个变量key不能变的

# caps = {
#     'platformName': 'Android',
#     'deviceName': 'emulator-5554',
#     # 方式一
#     'app': r'E:\apk\nmb-lemon_app_webview_debug.apk'
# }
# driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
#                 desired_capabilities=caps)

# 方式二
# 可以不提供app的路径，而是提供 app 的包名和 activity
# 包名: （相当于在手机上的appid）
# activity: app当中的那个页面
caps = {
    'platformName': 'Android',
    # 校验系统的版本
    # 'platformVersion': '8.0',
    # 'automationName': 'Uiautomator2',
    'deviceName': 'emulator-5554',
    # 'appPackage': 'com.ibox.calculators',
    # 'appActivity': 'com.ibox.calculators.CalculatorActivity',
    'app': r'E:\apk\qcd-Future-release-2018.apk',
    # 会使用缓存数据
    'noReset': 'True',
    # 'chromedriverExecutable':r'手机的浏览器驱动',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True
    # 'autoGrantPermissions': True


}
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=caps)

# 等待
driver.implicitly_wait(10)
# driver.find_element(By.ID,'').click()
driver.quit()