import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib
from monitor_control.window import AppWindow
from monitor_control import util
from monitor_control.const import UPDATE_DELAY, ACCELERATION


def update_feature(feature: str, target_val: dict, current_val: dict, override: dict, feature_velocity: dict) -> None:
    if current_val[feature] == target_val[feature]:
        feature_velocity[feature] = 0
        return True
    if override[feature]:
        new_val = target_val[feature]
        override[feature] = False
        feature_velocity[feature] = 0
    else:
        feature_velocity[feature] += ACCELERATION
        if target_val[feature] > current_val[feature]:
            new_val = min(current_val[feature] + feature_velocity[feature], target_val[feature])
        else:
            new_val = max(current_val[feature] - feature_velocity[feature], target_val[feature])

    util.set_feature_value(feature, new_val)
    current_val[feature] = new_val

    return True

def app__activate(app, target_val: dict, override: dict) -> None:
    window = AppWindow(app, target_val=target_val, override=override)
    window.present()

def main() -> None:
    target_val: dict = {'brightness': None, 'contrast': None, 'volume': None}
    current_val: dict = {'brightness': None, 'contrast': None, 'volume': None}
    override: dict = {'brightness': False, 'contrast': False, 'volume': False}
    feature_velocity: dict = {'brightness': 0, 'contrast': 0, 'volume': 0}

    for feature in target_val.keys():
        val = util.get_feature_value(feature)
        target_val[feature] = current_val[feature] = val


    app = Gtk.Application(application_id="org.example.hello")
    app.connect("activate", app__activate, target_val, override)

    # feature update loop
    for feature in target_val.keys():
        GLib.timeout_add(UPDATE_DELAY, update_feature, feature, target_val, current_val, override, feature_velocity)

    # gui loop
    app.run(None)

if __name__ == "__main__":
    main()