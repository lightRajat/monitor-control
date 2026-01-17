import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib
from gddc.const import UI_FILE_PATH, UPDATE_DELAY, CHECK_CONNECTION_INTERVAL, ABOUT_UI_FILE_PATH
from gddc import util

@Gtk.Template(filename=UI_FILE_PATH)
class AppWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "AppWindow"

    label_brightness = Gtk.Template.Child()
    label_contrast = Gtk.Template.Child()
    label_volume = Gtk.Template.Child()

    scale_brightness = Gtk.Template.Child()
    scale_contrast = Gtk.Template.Child()
    scale_volume = Gtk.Template.Child()

    stack = Gtk.Template.Child()

    def __init__(self, app, current_val: dict, target_val: dict, override: dict, feature_velocity: dict, update_feature) -> None:
        super().__init__(application=app)
        self.set_icon_name("gddc")

        self.current_val = current_val
        self.target_val = target_val
        self.override = override
        self.feature_velocity = feature_velocity
        self.update_feature = update_feature

        self.is_timer_set = False

        self.stack.set_visible_child_name("loading_page")

    def init_main_page(self) -> None:
        val = self.target_val['brightness']
        self.label_brightness.set_text(str(val))
        self.last_brightness = val
        self.scale_brightness.set_value(val)

        val = self.target_val['contrast']
        self.label_contrast.set_text(str(val))
        self.last_contrast = val
        self.scale_contrast.set_value(val)

        val = self.target_val['volume']
        self.label_volume.set_text(str(val))
        self.last_volume = val
        self.scale_volume.set_value(val)

        self.stack.set_visible_child_name("main_page")
    
    def refresh_app(self) -> None:
        self.stack.set_visible_child_name("loading_page")
        success: bool = util.detect_monitor()
        if success:
            for feature in self.target_val.keys():
                val = util.get_feature_value(feature)
                self.target_val[feature] = self.current_val[feature] = val
            
            self.init_main_page()

            if not self.is_timer_set:
                for feature in self.target_val.keys():
                    GLib.timeout_add(UPDATE_DELAY, self.update_feature, feature, self.target_val, self.current_val, self.override, self.feature_velocity, self.stack.get_visible_child_name())
                
                GLib.timeout_add_seconds(CHECK_CONNECTION_INTERVAL, self.check_connected)
                self.is_timer_set = True
            
            self.stack.set_visible_child_name("main_page")
        else:
            self.stack.set_visible_child_name("error_page")
    
    def check_connected(self):
        if self.stack.get_visible_child_name() != "main_page":
            return True
        success: bool = util.detect_monitor()
        if not success:
            self.stack.set_visible_child_name("error_page")
        return True
    
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

    @Gtk.Template.Callback()
    def on_close_button__clicked(self, button) -> None:
        self.get_application().quit()

    @Gtk.Template.Callback()
    def on_refresh_button__clicked(self, button) -> None:
        self.refresh_app()
    
    @Gtk.Template.Callback()
    def on_info_clicked(self, button):
        builder = Gtk.Builder.new_from_file(ABOUT_UI_FILE_PATH)

        close_btn = builder.get_object("close_button")
        close_btn.connect("clicked", lambda e: close_btn.get_root().close())

        about_win = builder.get_object("about_window")
        about_win.set_transient_for(self)
        about_win.set_modal(True)

        about_win.present()
