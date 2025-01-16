
# ShadowDeauth-DF

ShadowDeauth-DF is a powerful tool for executing cyberattacks like Deauth and DOS attacks. It is designed for educational purposes only, offering high efficiency and speed.

## Developer
**@A_Y_TR**

## Tool Features
1. **Massive Deauth Attack**:  
   Disconnects all devices connected to an Access Point (AP).
2. **DOS Attack on Router**:  
   Disables a router by sending a massive number of requests.
3. **Attack on Specific Camera**:  
   Targets and disconnects a specific camera from the network.

---

## Tool Installation Steps

### **Linux/macOS**
1. Open the terminal.
2. Download the tool and run the installer:
   ```bash
   git clone https://github.com/MohamedAbuAl-Saud/MAC-ADDRESS-ATTACK-/
   cd MAC-ADDRESS-ATTACK
   chmod +x install.sh
   sudo ./install.sh
   pip install -r requirements.txt
   sudo python3 shadowdeauth-DF.py
   ```

3. To run the tool:
   ```bash
   sudo python3 shadowdeauth-DF.py
   ```

### **Windows**
1. Install Python 3.
2. Open "Command Prompt" or "PowerShell."
3. Download the tool and run the installer:
   ```
   install.bat
   ```
4. To run the tool:
   ```
   python shadowdeauth-DF.py
   ```

---

# ShadowDeauth-DF WiFi USB Adapter

## **Using a WiFi USB Adapter with the Tool**

### **Why Do You Need a WiFi USB Adapter?**
1. **Monitor Mode Support:** Most built-in network cards in laptops do not support monitor mode, which is essential for performing wireless attacks.
2. **Packet Injection Support:** To ensure the attacks are performed efficiently, such as Deauthentication attacks.
3. **Compatibility:** Some built-in devices may be limited in terms of supported frequencies (only 2.4GHz), while some USB adapters also support 5GHz.

---

### **How to Connect and Use**
1. **Connect the WiFi USB Adapter:**
   - Plug the USB adapter into your computer's USB port.
   - Ensure that the device is recognized by running the command:
     ```bash
     lsusb
     ```
     The adapter name should appear if it's connected successfully.

2. **Switch the Adapter to Monitor Mode:**
   - Use the following command to identify the adapter interface name:
     ```bash
     iwconfig
     ```
   - After identifying the interface (e.g., `wlan0`), enable monitor mode with:
     ```bash
     sudo airmon-ng start wlan0
     ```
   - The interface will switch to `wlan0mon` (or a similar name).

3. **Test Monitor Mode:**
   - Ensure the adapter is in monitor mode by running:
     ```bash
     iwconfig
     ```
   - You should see "Mode: Monitor" listed.

4. **Run the Tool:**
   - Use the monitor interface (e.g., `wlan0mon`) when running the tool.

---

### **Best Compatible USB Adapters for the Tool**
The following adapters have been tested and work efficiently with the tool:

1. **Alfa AWUS036NHA**
   - Supports 2.4GHz.
   - Fully compatible with Linux, supports monitor mode and packet injection.

2. **Alfa AWUS036ACH**
   - Supports 2.4GHz and 5GHz.
   - High performance with full support for monitor mode and packet injection.

3. **TP-Link TL-WN722N (V1 only)**
   - Supports 2.4GHz.
   - A cost-effective, compatible option.

4. **Panda Wireless PAU09**
   - Supports 2.4GHz and 5GHz.
   - A small and easy-to-connect adapter.

5. **Edimax EW-7833UAC**
   - Supports 2.4GHz and 5GHz.
   - Very good performance with full support.

---

### **Common Issues and Solutions**
1. **Adapter Not Showing Up:**
   - Ensure the drivers for the adapter are installed:
     ```bash
     sudo apt install realtek-rtl88xxau-dkms
     ```
   
2. **Monitor Mode Not Working:**
   - Try stopping the network manager:
     ```bash
     sudo systemctl stop NetworkManager
     ```

3. **Packet Injection Not Working:**
   - Verify adapter compatibility with packet injection using:
     ```bash
     aireplay-ng --test wlan0mon
     ```

---

## Basic Commands in the Tool

1. **Massive Deauth Attack**: Enter the following:
   - Target device's MAC address or `ff:ff:ff:ff:ff:ff` to target all devices.
   - MAC address of the Access Point (Router).
   - Name of the network interface (Interface) being used.
   - Number of packets to send.

2. **DOS Attack on Router**: Enter the following:
   - IP address of the router.
   - Name of the network interface.
   - Duration of the attack (in seconds).

3. **Attack on Specific Camera**: Enter the following:
   - MAC address of the target camera.
   - MAC address of the Access Point.
   - Name of the network interface.
   - Number of packets to send.

4. **Exit**: To close the tool.

---

## Common Issues and Solutions

1. **Error in Library Installation**  
   Ensure Python and required libraries are installed using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Network Interface Not Found**  
   Ensure the interface name is entered correctly. Use:
   - `ifconfig` (Linux/macOS) or  
   - `ipconfig` (Windows)  
   to list available interfaces.

3. **Attack Failure**  
   Ensure the tool is run with root privileges (`sudo` on Linux/macOS).

---

## Notes

- **For educational purposes only**: This tool should be used responsibly and with caution.  
- **USB Wi-Fi Required**: Make sure you have a compatible USB Wi-Fi adapter.  
- **Disclaimer**: Any illegal use of this tool is your personal responsibility.
