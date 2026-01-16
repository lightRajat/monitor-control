from monitor_control.const import get_feature_cmd
import subprocess

def get_feature_value(feature: str) -> int:
    result = subprocess.run(get_feature_cmd(feature), capture_output=True, text=True)
    value = result.stdout.splitlines()[-1].split()[2].split('/')[1]
    return int(value)