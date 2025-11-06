# 🖥️ Monitor Control

A simple and intuitive **GUI application** to control your external monitor’s settings using the **DDC/CI protocol**.  
Perfect for adjusting brightness, contrast, and volume — right from your desktop!

---

## 🧩 Prerequisites

Before running this app, make sure you have the following installed:

- 🐍 **Python 3.x**
- 🪟 **tkinter** (usually comes bundled with Python)
- ⚙️ **ddcutil** command-line tool
- 🐧 **Linux operating system**

---

## ✨ Features

- 🔆 **Brightness control**
- 🎚️ **Contrast adjustment**
- 🔊 **Volume control**
- 🌙 **Red light filter** with modes: Off / Low / High  
  (helps reduce eye strain during night time)

---

## ⚙️ Installation

1. **Install `ddcutil`:**
    ```bash
    sudo apt install ddcutil
    ```

2. **Clone this repository and run the application:**

   ```bash
   git clone https://github.com/lightRajat/monitor-control.git
   cd monitor-control
   python main.py # while connected to an external monitor
   ```

---

## 🖱️ Usage

Once launched, the application provides:

* **Sliders** for:

  * Brightness (0–100%)
  * Contrast (0–100%)
  * Volume (0–100%)
* **Radio buttons** for red light filter:

  * Off / Low / High

### Buttons

* ✅ **Apply** — Save changes without closing
* 💾 **OK** — Save changes and close the app
* ❌ **Cancel** — Close without saving

---

## 💻 Supported Platforms

This application currently supports:

| Platform      | Supported | Notes                                                              |
| ------------- | --------- | ------------------------------------------------------------------ |
| 🐧 **Linux**   | ✅         | Fully supported (tested with `ddcutil`)                            |
| 🪟 **Windows** | ⚠️         | Not supported (DDC/CI handled differently)                         |
| 🍎 **macOS**   | ⚠️         | Not officially supported (may work with extra tools like `ddcctl`) |

> 🧠 **Note:**
> The DDC/CI protocol requires low-level monitor access.
> On Linux, `ddcutil` handles this seamlessly.
> Windows and macOS need driver-specific or manufacturer tools, so they’re currently not supported by default.

---

## 📝 Note

This application assumes the monitor is connected on **bus 7**.
If your monitor uses a different bus number, modify the value in `const.py`.

---

## 📜 License

This project is licensed under the **MIT License** — you’re free to modify and distribute it.

---

Made with ❤️ using Python and `tkinter`.
