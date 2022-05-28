
from appium.webdriver import Remote
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
    'app': r'E:\apk\Future-release-2018.apk',
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
# driver.find_element(By.ID, '').click()
# 查找元素
driver.find_element('id',)
driver.find_element('xpath',)
# 这是通过安卓原生的定位方式，我们需要写java语言，没有提示。
# UiSelector()元素定位器
locator = 'new UiSelector().'
driver.find_element_by_android_uiautomator(locator)
# tagname 不能用
# class_name ,可以，但是相当于原来的tag_name,不能精确定位
driver.quit()
