# Android User APP apk claim
这是一个使用adb命令提取所有用户app的脚本

编写原因
=======
因为要刷机备份应用，钛备份又不想装，也不想使用各种各样的手机助手。  
批处理也不会写。。。所以使用python提取已安装的用户apk应用。

使用方法
========

1. 开启手机usb调试模式

2. 安装好adb并配置好环境变量，即哪里都能打开adb

3. 在命令行输入 `adb devices` 确保连上了电脑

4. clone本项目后 使用 `python copyHere.py`

随后便会在目录下生成apk并复制手机中所有用户apk文件