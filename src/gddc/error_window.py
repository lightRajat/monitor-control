import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from gddc.const import ERROR_UI_FILE_PATH

@Gtk.Template(filename=ERROR_UI_FILE_PATH)
class ErrorWindow(Gtk.Window):
    __gtype_name__ = "ErrorWindow"

    def __init__(self, app) -> None:
        super().__init__(application=app)
        self.set_icon_name("gddc")
    
    @Gtk.Template.Callback()
    def on_close__clicked(self, button) -> None:
        self.close()

def app__activate(app) -> None:
    window = ErrorWindow(app)
    window.present()

def main() -> None:
    app = Gtk.Application(application_id="io.github.lightRajat.gddc")
    app.connect("activate", app__activate)
    app.run(None)

if __name__ == "__main__":
    main()