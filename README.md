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

用法： python3 dedescan.py

然后直接输入域名即可

## 已实现的功能

- 后台查找（win）
- 版本探测
- 短路经检测
- 路径检测
- trace检测
- advancedsearch.php SqlInject
- sql_class.php SqlInject
- feedback_js.php SqlInject
- getpage xss
- guestbook.php SqlInject
- infosearch.php SqlInject
- jump.php xss
- login.php xss
- recommend.php SQL 
- redirect
- reg_new.php SqlInject
- search.php sqlinject
- V5order by SqlInject
- article_keyword_select.php xss
- catelog_tree.php xss
- content_list.php xss
- file_pic_vie.php xss
- pic_view.php xss
- select_images.php xss
- writebook getshell
- digg_frame.php  rce
- list.php xss
- login.php xss
- config.php xss
- flash xss

## 部分截图

![](http://ww1.sinaimg.cn/large/007F8GgBly1g61fkee3tnj30pf0cdjta.jpg)

## 其他说明



所有exp、poc均为网上收集，原作者由于特殊原因删库了，可以克隆这个库使用

本程序依赖：

- requests
- re
- termcolor
- threading
- itertools

因为本程序编写只是为了自己使用，未加入批量功能，连多线程都是很随意（甚至都不能算是多线程），有时间再重构吧.....


