from monitor_control import i2c_bus
from os.path import join, dirname

FEATURE_CODE: dict = {
    'brightness': '0x10',
    'contrast': '0x12',
    'volume': '0x62',
}
I2C_BUS: str = i2c_bus.get()
UI_FILE_PATH: str = join(dirname(__file__), 'window.ui')
UPDATE_DELAY = 50 # milliseconds
ACCELERATION = 2 # steps

def get_feature_cmd(feature: str) -> list[str]:
    cmd = ['ddccontrol', '-r', FEATURE_CODE[feature], f'dev:/dev/{I2C_BUS}']
    return cmd

def set_feature_cmd(feature: str, value: int) -> str:
    cmd = f'ddccontrol -r {FEATURE_CODE[feature]} -w {value} dev:/dev/{I2C_BUS}\n'
    return cmd