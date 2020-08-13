shell语法编写规则：
同一个shell中编写函数a， function a() ，不需要事先定义有多少个变量
需要调用函数时，直接传参 a  123  ，则此"123" 想要在function a 中体现时，则echo $1 ，参数由1开始计数

调用函数返回值，则在执行完函数时，echo $? 则输出上一个运算的返回值

编写循环语句：
(1)while xxx; do  xxxxx done 结构
(2)for i in {0..9};do xxx done  或者 for i  in((i=1;i<=j;i++))
编写条件判断语句：
if [ "xxx" = "xxx" ];  then xxxxx  fi  注意[ ]中间各个空格必须隔开
多重判断： if [ "xxxx" = "xxxxx" ];then  xxxxx elif [ "xxxx" = "xxxx" ];then   else xxxxx  fi
判断条件逻辑符号：   && 与  || 或 ！非
判断条件数值大小符号： -eq 等于 -ne 不相等 -gt 大于 -ge 大于等于   -lt 小于 -le 小于等于

跟踪shell执行：sh +x xxxx.sh (会将可能输出的结果进行打印)

a='123'
想要输出a的变量 尽量使用${a} 而不是$a ，避免拼接变量时搞错值
$( )与` `等同，执行里面的程序命令
执行一串命令，可用()和{}   当使用（xxxx;xxx）中间使用;隔开   使用{ xxx;xxxx;}中间，尾部必须使用;隔开，且第一个命令前必须有空格
$(( ))表示进行整数计算
条件语句中[ ] 表示匹配中括号的字符  [!...]表示不匹配中括号的字符
=代表赋值  ==代表判断



![image-20200813153708615](/Users/bytedance/Library/Application Support/typora-user-images/image-20200813153708615.png)

