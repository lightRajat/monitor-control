feature_codes: dict = {
    'brightness': 10,
    'contrast': 12,
    'volume': 62,
    'video_red': 16,
    'video_green': 18,
    'video_blue': '1A',

}

red_light_mode: dict = {
    'off': (50, 50, 50),
    'low': (65, 35, 10),
    'high': (65, 15, 0),
}

get_feature_command: str = "ddcutil getvcp {} | egrep -o 'current value = *[0-9]{{,2}}' | awk '{{print $4}}'"

set_feature_command: str = "ddcutil setvcp {} {}"