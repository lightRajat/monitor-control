from os.path import join, dirname

FEATURE_CODE: dict = {
    'brightness': '0x10',
    'contrast': '0x12',
    'volume': '0x62',
}
I2C_BUS: str = None
UI_FILE_PATH: str = join(dirname(__file__), 'ui', 'window.ui')
ABOUT_UI_FILE_PATH: str = join(dirname(__file__), 'ui', 'about.ui')
ERROR_UI_FILE_PATH: str = join(dirname(__file__), 'ui', 'error.ui')
UPDATE_DELAY = 50 # milliseconds
ACCELERATION = 2 # steps
CHECK_CONNECTION_INTERVAL = 3 # seconds

def get_feature_cmd(feature: str) -> list[str]:
    cmd = ['ddccontrol', '-r', FEATURE_CODE[feature], f'dev:/dev/{I2C_BUS}']
    return cmd

def set_feature_cmd(feature: str, value: int) -> str:
    cmd = f'ddccontrol -r {FEATURE_CODE[feature]} -w {value} dev:/dev/{I2C_BUS}\n'
    return cmd