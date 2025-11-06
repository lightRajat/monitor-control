import subprocess
import const

def get_feature(feature):
    feature = subprocess.run(const.get_feature_command.format(const.feature_codes[feature]), shell=True, capture_output=True, text=True).stdout.strip()
    return feature

def get_red_light_mode():
    video_blue = get_feature('video_blue')

    if video_blue == '0':
        return "high"
    elif video_blue == '10':
        return 'low'
    else:
        return 'off'

# features
brightness = get_feature('brightness')
contrast = get_feature('contrast')
volume = get_feature('volume')
red_light_mode = get_red_light_mode()
print("volume:", volume)
print("brightness:", brightness)
print("contrast:", contrast)
print("red_light_mode:", red_light_mode)