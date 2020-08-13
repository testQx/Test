import subprocess


def cpu_time(devices):
    user = nice = system = idle = iowait = irq = softirq = 0
    cmd = "adb -s " + devices + " shell cat /proc/stat"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    res = output.split()
    for info in res:
        if info.decode() == "cpu":
            user = res[1].decode()
            nice = res[2].decode()
            system = res[3].decode()
            idle = res[4].decode()
            iowait = res[5].decode()
            irq = res[6].decode()
            softirq = res[7].decode()
    result = int(user) + int(nice) + int(system) + int(idle) + int(iowait) + int(irq) + int(softirq)
    return result


def pid_cpu_time(pid, devices):
    utime = stime = cutime = cstime = 0
    cmd = "adb -s " + devices + " shell cat /proc/" + pid + "/stat"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    res = output.split()
    utime = res[13].decode()
    stime = res[14].decode()
    cutime = res[15].decode()
    cstime = res[16].decode()
    result = int(utime) + int(stime) + int(cutime) + int(cstime)
    return result