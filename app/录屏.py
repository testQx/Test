# coding=utf-8
import os
import subprocess
import time

while True:

    device = os.popen('adb devices').read().split('\n')[1].rstrip(' device')
    if not device:
        print
        '\033[1;33m找不到设备，请检查是否连接USB\033[0m'
        break

    else:
        print("\033[1;31m0、退出\033[0m")
        print("\033[1;31m1、截图\033[0m")
        print("\033[1;31m2、录屏\033[0m")
        print("\033[1;31m3、参数\033[0m")
        print("\033[1;31m4、清缓存\033[0m" + "\033[1;28m(打开App，保持在前台桌面)\033[0m")
        print("\033[1;31m5、WiFi\033[0m")
        print("\033[1;31m6、Unwifi\033[0m")
        print
        i = (input("请输入选项，回车: "))

        if i == 0:
            print
            os.popen('adb devices').read()
            break

        elif i == 1:
            os.popen(
                'adb -s ' + device + ' shell screencap -p /sdcard/test.png && adb pull /sdcard/test.png ~/Desktop/')
            print("\033[1;32m截图成功，保存至桌面test.png\033[0m")

        elif i == 2:
            print
            "录屏开始, 按 control+c 结束录屏"
            try:
                os.system('adb -s ' + device + ' shell screenrecord /sdcard/video.mp4')
            except KeyboardInterrupt:
                pass
            time.sleep(1)
            print("\033[1;32m录屏成功，保存至桌面test.mp4\033[0m")
            os.popen('adb pull /sdcard/video.mp4 ~/Desktop/')


        elif i == 3:
            cmd_1 = 'adb -s ' + device + ' shell getprop ro.product.model'
            cmd_2 = 'adb -s ' + device + ' shell getprop ro.build.version.release'
            cmd_3 = 'adb -s ' + device + ' shell wm size'
            print
            print
            '\033[1;32m机型:\033[0m', os.popen(cmd_1).read(), '\033[1;32m系统:\033[0m', os.popen(
                cmd_2).read(), '\033[1;32m分辨率:\033[0m', os.popen(cmd_3).read().split(':')[1]


        elif i == 4:

            apk_name = \
            os.popen('adb -s ' + device + ' shell "dumpsys window|grep mCurrentFocus"').readline().split('u0')[1].split(
                '/')[0]
            os.popen('adb -s ' + device + ' shell pm clear' + apk_name)
            print
            "\033[1;32m缓存清理成功\033[0m"
            print

        elif i == 5:
            device_2 = os.popen('adb devices').read().split('\n')[2]
            if not device_2:
                ip = os.popen('adb shell ifconfig wlan0').read().split('\n')[1].split(':')[1].split(' ')[0]
                time.sleep(1)
                info = os.popen('adb tcpip 6666 && adb connect ' + ip + ':6666').readline()
                print
                '\033[1;32mWiFi连接成功，可拔掉USB，继续使用\033[0m'
                print
            else:
                print
                '\033[1;33m存在多个设备号，请检测WiFi是否已连接\033[0m'

        elif i == 6:
            device_2 = os.popen('adb devices').read().split('\n')[2]
            if not device_2:
                ip = os.popen('adb shell ifconfig wlan0').read().split('\n')[1].split(':')[1].split(' ')[0]
                print
                os.system('adb disconnect ' + ip + ':6666')
                print
                '\033[1;32mWiFi已断开，请连接USB，继续使用\033[0m'
                print
            else:
                print
                '\033[1;33m存在多个设备号，请确认连接WiFi同时，要断开USB\033[0m'




