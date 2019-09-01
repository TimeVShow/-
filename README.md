# QuickGetClassRoom
## 1.主要作用
  配合小程序，来快速地获取教学楼课表并处理成json文件
## 2.环境要求
  1.python版本我所使用的是python3.7
  2.需要的包有requests,bs4(用来解析html文件），json（python自带），os（自带）
## 3.使用方法
  -> 1.在file文件夹中建立对应地点的文件夹
  -> 2.在地点文件夹中创建class_messege文件夹，json文件夹，以及地点名称（此处为自己设置的地点名称）.txt文件（txt文件中存放对应教学楼全部的可用教室）
  -> 3.在class_messege存入教学楼的课表信息（只要html文件）同时按周一到周五命名为1.html 2.html 3.html 4.html 5.html
  -> 4.首先执行getclasssdata.py文件生成第一次的json文件
  -> 5.接着执行fix_errors.py文件这里会修补可用但是课程表中不显示的教室的信息
  -> 6.getclassdata.py只能处理常见的信息例如(1-9),(1-10),(11-15)。对于不常见的信息，需要自己手工处理，会在json文件中special处标注error
