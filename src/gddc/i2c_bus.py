import os
import glob
import fcntl
import re

def get(debug: bool=False) -> str | None:
    """
    Detects the first connected external monitor and returns its I2C bus name.
    """
    
    # Constants for I2C probing
    I2C_SLAVE = 0x0703
    EDID_ADDRESS = 0x50

    def log(msg):
        if debug: print(f"[DEBUG] {msg}")

    def is_bus_responsive(bus_num):
        """Active Probe: Tries to read 1 byte from address 0x50."""
        dev_path = f"/dev/i2c-{bus_num}"
        fd = None
        try:
            fd = os.open(dev_path, os.O_RDWR)
            fcntl.ioctl(fd, I2C_SLAVE, EDID_ADDRESS)
            os.read(fd, 1)
            return True
        except PermissionError:
            log(f"PERMISSION DENIED on {dev_path} (Try running with sudo/admin)")
            return False
        except OSError:
            return False
        finally:
            if fd is not None: os.close(fd)

    # Helper: Find the PCI Parent directory by walking up the path
    def find_pci_parent(path):
        # We look for a folder name looking like 0000:01:00.0
        pci_pattern = re.compile(r'[0-9a-f]{4}:[0-9a-f]{2}:[0-9a-f]{2}\.[0-9]')
        head = os.path.realpath(path)
        while len(head) > 1:
            if pci_pattern.match(os.path.basename(head)):
                return head
            head = os.path.dirname(head)
        return None

    log("Scanning monitors...")

    for status_path in glob.glob("/sys/class/drm/*/status"):
        try:
            with open(status_path, "r") as f:
                if f.read().strip() != "connected":
                    continue
        except OSError:
            continue

        connector_dir = os.path.dirname(status_path)
        name = os.path.basename(connector_dir)
        
        # Filter Internal
        if any(x in name for x in ["eDP", "LVDS", "DSI"]):
            log(f"Skipping internal: {name}")
            continue

        log(f"Found External: {name}")

        # METHOD 1: Symlink (Easy)
        ddc_link = os.path.join(connector_dir, "ddc")
        if os.path.islink(ddc_link):
            real_i2c = os.path.basename(os.readlink(ddc_link))
            log(f"  -> Match via symlink: {real_i2c}")
            return real_i2c

        # METHOD 2: PCI Match (Hard)
        log("  -> No symlink. Trying PCI match...")
        
        # Find which GPU owns this HDMI port
        gpu_path = find_pci_parent(connector_dir)
        if not gpu_path:
            log("  -> Could not determine GPU PCI path.")
            continue
            
        log(f"  -> GPU Path: {gpu_path}")

        # Scan all I2C buses
        for i2c_entry in glob.glob("/sys/bus/i2c/devices/i2c-*"):
            # Find which GPU owns this I2C bus
            i2c_parent = find_pci_parent(i2c_entry)
            
            if i2c_parent == gpu_path:
                bus_name = os.path.basename(i2c_entry)
                bus_num = int(bus_name.replace("i2c-", ""))
                
                log(f"  -> Checking candidate {bus_name}...")
                
                if is_bus_responsive(bus_num):
                    log(f"  -> SUCCESS: Monitor active on {bus_name}")
                    return bus_name
                else:
                    log(f"  -> Failed probe on {bus_name}")

    log("No matching monitor found.")
    return None