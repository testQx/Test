#!/usr/bin/bash
echo "输入需要运行的py路径"
read input1
for i in $(adb devices | grep "devices$" | awk '{print $1}');
do
  echo "start: {$i}"
  udid=$i pytest -v -s --alluredir=/result/** $input1 &
done
