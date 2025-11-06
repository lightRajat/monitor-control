import tkinter as tk
import tkinter.font as tkFont
import init
import callbacks

widgets_reference = {}

# Root Controls Start
root = tk.Tk()
root.title("Monitor Control")
widgets_reference['root'] = root

## font
font = tkFont.nametofont("TkDefaultFont")
font.configure(family="Noto Sans", size=12)
root.option_add("*Font", font)

# Wrapper
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill='both', expand=True)

# Brightness
brightness_label = tk.Label(frame, text="Brightness:")
brightness_label.pack(anchor='w')
brightness_slider = tk.Scale(frame, from_=0, to=100, orient='horizontal', resolution=5)
brightness_slider.pack(fill='x')
brightness_slider.set(init.brightness)
widgets_reference['brightness'] = brightness_slider

# Contrast
contrast_label = tk.Label(frame, text="Contrast:")
contrast_label.pack(anchor='w')
contrast_slider = tk.Scale(frame, from_=0, to=100, orient='horizontal', resolution=5)
contrast_slider.pack(fill='x')
contrast_slider.set(init.contrast)
widgets_reference['contrast'] = contrast_slider

# Volume
volume_label = tk.Label(frame, text="Volume:")
volume_label.pack(anchor='w')
volume_slider = tk.Scale(frame, from_=0, to=100, orient='horizontal', resolution=5)
volume_slider.pack(fill='x')
volume_slider.set(init.volume)
widgets_reference['volume'] = volume_slider

# Red Light
red_label = tk.Label(frame, text="Red Light:")
red_label.pack(anchor='w')

radio_frame = tk.Frame(frame)
radio_frame.pack(anchor='w')

red_radio_var = tk.StringVar(value=init.red_light_mode)
widgets_reference['red_light_mode'] = red_radio_var
tk.Radiobutton(radio_frame, text="Off", variable=red_radio_var, value="off").pack(side='left')
tk.Radiobutton(radio_frame, text="Low", variable=red_radio_var, value="low").pack(side='left')
tk.Radiobutton(radio_frame, text="High", variable=red_radio_var, value="high").pack(side='left')

# Window Buttons
button_frame = tk.Frame(frame)
button_frame.pack(fill='x', side='bottom')

cancel_button = tk.Button(button_frame, text="Cancel", command=lambda: callbacks.close_window(widgets_reference))
cancel_button.pack(side='right', padx=5)

apply_button = tk.Button(button_frame, text="Apply", command=lambda: callbacks.on_clicked_apply(widgets_reference))
apply_button.pack(side='right', padx=5)

ok_button = tk.Button(button_frame, text="OK", command=lambda: callbacks.on_clicked_ok(widgets_reference))
ok_button.pack(side='right', padx=5)

# Root Controls End
root.update_idletasks()
window_height = root.winfo_height()
window_width = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
root.mainloop()