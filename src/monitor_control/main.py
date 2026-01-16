import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from monitor_control.window import AppWindow
from monitor_control import init


def app__activate(app, target_val: dict, override: dict) -> None:
    window = AppWindow(app, target_val=target_val, override=override)
    window.present()

def main() -> None:
    target_val: dict = {'brightness': None, 'contrast': None, 'volume': None}
    current_val: dict = {'brightness': None, 'contrast': None, 'volume': None}
    override: dict = {'brightness': False, 'contrast': False, 'volume': False}

    for feature in target_val.keys():
        val = init.get_feature_value(feature)
        target_val[feature] = current_val[feature] = val


    app = Gtk.Application(application_id="org.example.hello")
    app.connect("activate", app__activate, target_val, override)

    app.run(None)

if __name__ == "__main__":
    main()