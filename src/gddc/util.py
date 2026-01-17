from gddc import const
from gddc import i2c_bus
import subprocess

proc = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True)

def get_feature_value(feature: str) -> int:
    result = subprocess.run(const.get_feature_cmd(feature), capture_output=True, text=True)
    value = result.stdout.splitlines()[-1].split()[2].split('/')[1]
    return int(value)

def set_feature_value(feature: str, value: int) -> None:
    global proc
    if proc.poll() is not None:
        proc = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    proc.stdin.write(const.set_feature_cmd(feature, value))
    proc.stdin.flush()

def detect_monitor() -> bool:
    bus = i2c_bus.get()
    if bus is None:
        return False

    const.I2C_BUS = bus
    return True