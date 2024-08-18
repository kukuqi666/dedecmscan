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

1.添加各类检测功能：在 Check 类中实现了 SQL 注入、XSS、RCE、文件包含、重定向等检测。
2.更新 dedescan.py：确保它正确调用更新后的 Check 类。
3.测试和验证：运行脚本并检查输出和生成的报告文件。
通过在 poc 方法中添加更复杂的检测逻辑、处理和保存结果、以及增加异常处理，可以大大增强脚本的功能性和稳定性。这样的扩展不仅能提高脚本的实用性，还能让你在实际使用中更好地管理和分析检测结果。
在 Check 类中添加了多种检测功能，包括 SQL 注入、XSS、RCE、文件包含、重定向等。我们还更新了 dedescan.py 以确保它使用最新的 Check 类实现。这些更改使得工具能够检测更广泛的安全漏洞，并生成详细的报告。运行脚本并查看输出和生成的报告文件，以验证功能是否按预期工作。如果有任何问题或需要进一步的帮助，请告诉我！

## 其他说明

所有exp、poc均为网上收集，由于原作者删库，再次进行了二次更新并且完善一下功能

本程序依赖：

- requests
- re
- termcolor
- threading
- itertools


