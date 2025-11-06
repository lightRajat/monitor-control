import const
import subprocess

def close_window(widgets):
    widgets['root'].destroy()

def set_feature(feature, feature_value):
    command = const.set_feature_command.format(const.feature_codes[feature], feature_value)
    subprocess.run(command, shell=True)

def on_clicked_apply(widgets):
    # get new values
    brightness = widgets['brightness'].get()
    contrast = widgets['contrast'].get()
    volume = widgets['volume'].get()

    # set new values
    set_feature('brightness', brightness)
    set_feature('contrast', contrast)
    set_feature('volume', volume)

    # set red light mode
    set_red_light_mode(widgets['red_light_mode'].get())

def on_clicked_ok(widgets):
    widgets['root'].withdraw()
    on_clicked_apply(widgets)
    close_window(widgets)

def set_red_light_mode(mode):
    # config color values
    red_value = const.red_light_mode[mode][0]
    green_value = const.red_light_mode[mode][1]
    blue_value = const.red_light_mode[mode][2]

    # set values
    set_feature('video_red', red_value)
    set_feature('video_green', green_value)
    set_feature('video_blue', blue_value)