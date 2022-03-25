# 这是一个什么程序
用selenium写的一个自动连接河海大学健康打卡网站的小程序

因为最近一段时间学校天天要求健康打卡，但是作者本人经常会忘记这件事，所以最好有一个自动程序能帮我天天打卡

考虑到可能也有会一些同学不想每天都被辅导员催着，所以就写了这么一个简单的打卡小程序挂在电脑上帮助我处理这些麻烦事

# 一些注意事项的说明
在使用selenium驱动浏览器的时候，需要安装对应的webdriver

对于win10自带的Edge，下载的地址为：[Edge浏览器webdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

如果使用的是谷歌浏览器，下载的地址是一个淘宝镜像：[Chrome浏览器webdriver](http://npm.taobao.org/mirrors/chromedriver/)

当然这些东西在百度上都是能搜的到的，文件里面也提供了这两个浏览器对应的webdriver

使用的webdriver不同，在代码里面调用的函数也不同，以edge为例：

    driver = wb.Edge('.\msedgedriver.exe')

如果用的是谷歌浏览器，就可以写成：

    driver = wb.Chrome('.\chromedriver.exe')

`.\` 表示当前文件夹路径，`..\` 表示父文件夹路径

# 如何使用

在`账号信息.txt`文件里面输入自己的信息，程序就可以自动读取了

（当然你也可以根据自己的需要修改）

# 源代码如何打包

作者这里使用的是pyinstaller，因为selenium是安装在pip环境下面的，所以

    pip install pyinstaller

如果是在conda环境下，那就执行conda的安装命令

如果要打包程序的话，打开控制台程序后

    cd 程序所在的目录
    pyinstaller -F 程序名称.py

# 如何设定windows定时任务

在我的电脑里打开“管理”，找不到的也可以直接搜索“计算机管理”

选择“任务计划程序”

在右侧选择“创建基本任务”

剩下的跟着导航自行设定就可以了

# 写在最后
当然，考虑到本人目前水平有限，再加上学校的网络环境不稳定

有的时候可能会出现程序进行了点击操作，但是浏览器上面一直转圈圈啥也显示不出来的操作

这个时候程序一般会报错，需要自己手动处理啦
