
# pyuic配置
$FileName$ -o $FileNameWithoutExtension$.py

# 信号 与 槽
- (sender, signal) ---------bind----------- (receiver, slot)
https://www.cnblogs.com/chenhaiming/p/9930628.html

# 资源文件配置
在qt designer工作目录添加文件 $filename$.qrc :<br>
`<rcc version="1.0>
    <qresource>
    </qresource>
</rcc>`
<br>
使用pyrcc5将文件 $filename$.qrc编译成.py文件
pyrcc5在pycharm中的配置:$FileName$ -o $FileNameWithoutExtension$_rc.py

# 信号 与 槽
https://www.cnblogs.com/chenhaiming/p/9930628.html

