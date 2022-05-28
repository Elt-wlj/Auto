#### 主要目的：
 - 上手appium工具使用
 - appium思想执行流程
 - appium 调试技巧 app不太稳定
 - 非常核心和基础：元素定位

#### caps信息：
http://appium.io/docs/en/writing-running-appium/caps/

```
1、[Appium] Welcome to Appium v1.13.0
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
appium 服务在 4723 端口已经开启，
```

```
2、[HTTP] --> POST /wd/hub/session
[HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:platformVersion":"8.0","appium:deviceName":"emulator-5554","appium:appPackage":"com.lemon.lemonban","appium:appActivity":"com.lemon.lemonban.activity.WelcomeActivity"}]},"desiredCapabilities":{"platformName":"Android","platformVersion":"8.0","deviceName":"emulator-5554","appPackage":"com.lemon.lemonban","appActivity":"com.lemon.lemonban.activity.WelcomeActivity"}}
[W3C] Calling AppiumDriver.createSession() with args:

是 python 代码访问了 appium 服务提供的 /wd/hub/session 这个接口， 开启一个会话

```
```
3、w3c 校验

```

```
4、appium接收参数
```

```
5、appium 服务启动了 adb 程序，获取电脑上的手机设备， 如果参数不通过，就返回给客户端。
```

```
6、[ADB] Running 'D:\adt-bundle-windows-x86_64-20140702\sdk\platform-tools\adb.exe -P 5037 -s emulator-5554 shell am start -W -n com.lemon.lemonban/com.lemon.lemonban.activity.WelcomeActivity -S'
手动通过 adb 启动 app

adb shell ： 进入手机的shell
android 是一个 linux 系统的发行版。 deepin, ubuntu, centos
```