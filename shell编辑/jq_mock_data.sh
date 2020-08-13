#!/bin/bash
if [ `brew list | grep jq` ];
then echo "jq已安装完毕"
else
brew install jq
fi
echo '请输入需要替换的json路径'
read input1
echo '需要倍增的jq目标'
read input2
echo '需要倍增的次数'
read input3
stockdata=$(cat $input1)
echo $stockdata
for ((i=1;i<=$input3;i++))
do
stockdata=$(echo $stockdata | jq $input2+=$input2)
#i=$(($i+1))
done
echo $stockdata >$input1
echo $stockdata
