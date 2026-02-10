# 🖥️ gddc (Monitor Control)

**gddc** is a lightweight GTK 4 application to control **brightness**, **contrast**, and **volume** of external monitors on Linux using the **DDC/CI** protocol, built on top of the command-line tool [`ddccontrol`](https://github.com/ddccontrol/ddccontrol).

## Preview

<video src="https://github.com/user-attachments/assets/2f964fe6-c302-4f34-b213-06dcf82bdb82" controls title="GUI Preview"></video>

## 📦 Installation Instructions

### 1. Install the Application

Run the following command to download and install the `.deb` package:

```bash
wget -qO /tmp/myapp.deb https://github.com/lightRajat/monitor-control/releases/download/v1.0-1/gddc_1.0-1_all.deb && sudo apt install /tmp/myapp.deb -y
```

### 2. Grant i2c Permissions

Add your current user to the `i2c` group so the app can communicate with your monitor:

```bash
sudo usermod -aG i2c $USER
```

### 3. Apply Changes

**Log out and log back in** (or restart your computer) for the permission changes to take effect.

## 🧩 Compatibility

* **Target OS:** Designed for **Debian-based Linux distributions** (Ubuntu, Linux Mint, Pop!_OS, Kali, etc.) using the `apt` package manager.
* **Desktop Environment:** Requires support for **GTK 4** libraries (`gir1.2-gtk-4.0`).
* **Kernel:** Relies on a standard Linux kernel with the `i2c-dev` module enabled for hardware communication.
* **Unsupported Platforms:** Not compatible with Windows (including WSL), macOS, or non-Debian Linux distros (Arch, Fedora, RPM-based) without manual adaptation.

## ✨ Features

* Built with **GTK 4**
* Live control of **Brightness**, **Contrast**, and **Volume**
* Smooth sliders with acceleration and jump-override behavior
* Automatic external monitor detection and correct I²C bus selection

## 🛠️ Development

### Clone the repository

```bash
git clone https://github.com/lightRajat/monitor-control.git
cd monitor-control
```

### Run locally

```bash
src/main
```

## 🐞 Contributions & Bug Reports

Contributions, bug reports, and suggestions are welcome on the [GitHub repository](https://github.com/lightRajat/monitor-control).

## 📜 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it.

## 🙏 Credits

App icon created by [Freepik – Flaticon](https://www.flaticon.com/free-icons/setup)
