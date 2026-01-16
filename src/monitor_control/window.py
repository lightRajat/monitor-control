import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from monitor_control.const import UI_FILE_PATH

@Gtk.Template(filename=UI_FILE_PATH)
class AppWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "AppWindow"

    label_brightness = Gtk.Template.Child()
    label_contrast = Gtk.Template.Child()
    label_volume = Gtk.Template.Child()

    scale_brightness = Gtk.Template.Child()
    scale_contrast = Gtk.Template.Child()
    scale_volume = Gtk.Template.Child()

    def __init__(self, app, target_val: dict, override: dict) -> None:
        super().__init__(application=app)
        self.target_val = target_val
        self.override = override

        val = target_val['brightness']
        self.label_brightness.set_text(str(val))
        self.last_brightness = val
        self.scale_brightness.set_value(val)

        val = target_val['contrast']
        self.label_contrast.set_text(str(val))
        self.last_contrast = val
        self.scale_contrast.set_value(val)

        val = target_val['volume']
        self.label_volume.set_text(str(val))
        self.last_volume = val
        self.scale_volume.set_value(val)
    
    @Gtk.Template.Callback()
    def on_scale__value_changed(self, slider) -> None:
        value = int(slider.get_value())

        if slider is self.scale_brightness:
            self.label_brightness.set_text(str(value))
            self.target_val['brightness'] = value
            if abs(value - self.last_brightness) > 1:
                self.override['brightness'] = True
            self.last_brightness = value

        elif slider is self.scale_contrast:
            self.label_contrast.set_text(str(value))
            self.target_val['contrast'] = value
            if abs(value - self.last_contrast) > 1:
                self.override['contrast'] = True
            self.last_contrast = value

        elif slider is self.scale_volume:
            self.label_volume.set_text(str(value))
            self.target_val['volume'] = value
            if abs(value - self.last_volume) > 1:
                self.override['volume'] = True
            self.last_volume = value
