# dedecmscan



dedescan是一款可以扫描所有已公开的dedecms漏洞的扫描器。

```
        ...                 ...                                                     
        ...                 ...                                                     
        ...                 ...                                                     
        ...                 ...                                                     
        ...                 ...                                                     
   ........  .......   ........   .......   .......    ......    ......   ........  
  ...  .... .... ....  ... ....  .... ...  .... ...   ... ....  ...  ...  .... .... 
 ....  .... ...   ... ...   ...  ...   ... ...       ...   ...  .    ...  ...   ... 
 ....   ... ......... ...   ... ..........  ....     ...           .....  ...   ... 
 ....   ... ...       ...   ... ....         ......  ...        ........  ...   ... 
 ....  .... ...       ...   ... ....            .... ...   ... ....  ...  ...   ... 
  ...  .... ....  ... ....  ...  ...  .... ...   ... ....  ... ....  ...  ...   ... 
  .........  ........  ........   .......  ........   ........  ........  ...   ... 
    .......   .....     .......    .....     .....      ....     ........ ...   ... 

```


用法： python dedescan.py

然后直接输入域名即可

## 已实现的功能

 info 和 script 目录现在包含了多个功能脚本。这些脚本涵盖了 SQL 注入、XSS 漏洞、远程代码执行等多种漏洞检测功能，以及后台管理面板查找、版本信息获取等功能。
 
新增脚本解释
1. FindAdmin.py: 用于查找后台管理界面。可以添加更多路径以增强功能。

2. GetVersion.py: 用于获取版本信息。可以添加更多路径以增强功能。

3. passwordrest.py, path.py, shortpath.py, trace.py: 这些脚本可以根据需求进一步整合到 Check 类中。具体功能可以根据这些脚本的内容来决定如何使用。

## 部分截图

![](http://ww1.sinaimg.cn/large/007F8GgBly1g61fkee3tnj30pf0cdjta.jpg)

## 其他说明


所有exp、poc均为网上收集，原作者由于特殊原因删库了，本仓库在原来的基础下进行二次更新并且完善


本程序依赖：

- requests
- re
- termcolor
- threading
- itertools

