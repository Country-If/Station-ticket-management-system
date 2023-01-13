# Station-ticket-management-system

- 安全状态

[![Security Status](https://www.murphysec.com/platform3/v3/badge/1612483228867276800.svg?t=1)](https://www.murphysec.com/accept?code=931f0b2a6e7b87fcd38d52242a6e52f1&type=1&from=2&t=2)

## 写在前面
- 本系统是本学期的数据库课程设计，写次文档便于理清后台配置，尤其是数据库的配置
- 该系统数据库部署在阿里云服务器上，账号信息在代码中可见，请勿攻击本人的服务器以及利用服务器做非法的事情
- 如果对你有用的话给个star吧

## 配置说明
- Python环境：Python 3.7
- Python依赖

    使用`pipreqs ./ --encoding=utf8`对项目文件生成依赖文件[requirements.txt](requirements.txt)。UI界面开发选用**PySide2**，具体环境配置请自行百度

- 后台说明

    本系统后台部署在本人阿里云服务器的 Linux 系统上，Linux 使用的是 Ubuntu 20.04，数据库为 MySQL 8.0

    数据库配置见[booking_information.sql](sql/structure/booking_information.sql)、[seat_information.sql](sql/structure/seat_information.sql)、[train_information.sql](sql/structure/train_information.sql)、[user_information.sql](sql/structure/user_information.sql)

    [make_data.py](make_data.py)提供了批量生成数据的方法，初始数据见[ticket_management_system.sql](sql/all_data/ticket_management_system.sql)

## 关于程序打包的问题

- 问题
  
    如果直接使用`pyinstaller`对程序进行打包的话，打包出来的可执行文件移植后可能会出现`This application failed to start because no Qt platform plugin could be initialized.`的问题，如下图：
        
    ![](https://cdn.jsdelivr.net/gh/Country-If/Typora-images/img/20220110181354.png)

- 解决

    - 我的解决办法是程序打包前先在代码开头加上一段代码：
    
      ```python
      import os
      
      os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'platforms'
      ```
    
    - 之后再使用 `pyinstaller` 进行打包，打包后需要去找自己 `pyside2` 的安装路径，找到 `platforms`，将整个文件夹拷贝至与可执行文件相同的目录下，例如我的 platforms 放在`D:\anaconda3\envs\py3.7\Lib\site-packages\PySide2\plugins\platforms`，建议使用 everything 搜索查找比较快

    - 这个方法我自己用虚拟机试过，移植到虚拟机后程序可以正常打开不报错了

    - 另外，这段代码只用于打包可执行文件时使用，若自己本机已经配置好了 PySide2 的环境，加上这段话后在 pycharm 上运行反而会报错，所以在 pycharm 上运行或调试时需要将这段代码注释掉，只在打包时取消注释

