import os
import subprocess
import time
from reuseable.configs import MobileConfig

def start_server():
    os.system(f" start /B start cmd.exe @cmd /k appium -p {MobileConfig.port} -a {MobileConfig.IP}")


def stop_server():
    cmd = f"netstat -ano -p tcp | findstr :{MobileConfig.port}"
    output = subprocess.check_output(cmd, shell=True)
    print(output.decode().strip().split()[-1])
    pid = int(output.decode().strip().split()[-1])
    # Kill the Appium server process with the PID
    cmd = f"taskkill /F /PID {pid}"
    subprocess.run(cmd, shell=True)
    time.sleep(5)
