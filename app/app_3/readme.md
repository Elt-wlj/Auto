##### app定位元素问题:
 - 1.xpath 用的是绝对路径
 - 2.id

工具一:
 - 安卓自带提供的 uiautomatorviewer
   - 直接点击tools下的 D:\soft-t\Android\tools\uiautomatorviewer.bat 即可

工具三:
 - atx: weditor 元素定位辅助工具
 - pip install weditor
 - weditor(版本查看)[https://pypi.org/project/weditor/#history]
   - 注意：若是安装出错：降低版本即可：(参考这篇文章)[https://blog.csdn.net/qq_43911915/article/details/123718924]
 - weditor的使用方法:
   - python -m weditor

##### 三种工具
 - weditor : 优势在path,但是起冲突
 - uiautomator : 升级版的工具，升级path表达式
 - appium自带的。

#### 总结元素定位方式
 - 优先使用id
 - xpath 方便获取
 - android_uiautomator 原生模式
 - content-desc
 - className 基本不用
 