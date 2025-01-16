
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
