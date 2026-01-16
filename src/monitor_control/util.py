from monitor_control.const import get_feature_cmd, set_feature_cmd
import subprocess

proc = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True)

def get_feature_value(feature: str) -> int:
    result = subprocess.run(get_feature_cmd(feature), capture_output=True, text=True)
    value = result.stdout.splitlines()[-1].split()[2].split('/')[1]
    return int(value)

def set_feature_value(feature: str, value: int) -> None:
    global proc
    if proc.poll() is not None:
        proc = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    proc.stdin.write(set_feature_cmd(feature, value))
    proc.stdin.flush()